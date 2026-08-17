import urllib.request
import json
import re
import os

USERNAME = "BharathGDevadiga"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

headers = {"User-Agent": "GitHub-Action-Stats-Updater"}
if TOKEN:
    headers["Authorization"] = f"token {TOKEN}"

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# 1. Fetch live metrics
user_data = fetch_json(f"https://api.github.com/users/{USERNAME}")
repos_count = user_data.get("public_repos", 10) if user_data else 10
followers_count = user_data.get("followers", 1) if user_data else 1

repos_data = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")
stars_count = 0
if repos_data and isinstance(repos_data, list):
    for r in repos_data:
        stars_count += r.get("stargazers_count", 0)

# Total commits estimate / fallback
commits_count = 500

print(f"[AutoUpdate] Repos: {repos_count} | Stars: {stars_count} | Followers: {followers_count} | Commits: {commits_count}")

# 2. Update Stats SVGs
def update_stats_files():
    for f_name in ["bharath-stats.svg", "bharath-stats-light.svg"]:
        if not os.path.exists(f_name):
            continue
        with open(f_name, "r", encoding="utf-8") as f:
            content = f.read()

        # Update Stars
        content = re.sub(r'(Total Stars Earned:</text>\s*<text[^>]+>)[^<]+(</text>)', rf'\g<1>{stars_count}+\g<2>', content)
        # Update Commits
        content = re.sub(r'(Total Commits:</text>\s*<text[^>]+>)[^<]+(</text>)', rf'\g<1>{commits_count}+\g<2>', content)
        # Update Repos
        content = re.sub(r'(Public Repos:</text>\s*<text[^>]+>)[^<]+(</text>)', rf'\g<1>{repos_count}+\g<2>', content)
        # Update Followers
        content = re.sub(r'(Followers:</text>\s*<text[^>]+>)[^<]+(</text>)', rf'\g<1>{followers_count}+\g<2>', content)

        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

# 3. Update Banner SVGs
def update_banner_files():
    for f_name in ["bharath-banner.svg", "bharath-banner-light.svg"]:
        if not os.path.exists(f_name):
            continue
        with open(f_name, "r", encoding="utf-8") as f:
            content = f.read()

        # Update stats text elements
        content = re.sub(r'(<text class="st" x="114" y="636"[^>]*>)[^<]+(</text>)', rf'\g<1>{repos_count}+\g<2>', content)
        content = re.sub(r'(<text class="st" x="246" y="636"[^>]*>)[^<]+(</text>)', rf'\g<1>{commits_count}+\g<2>', content)
        content = re.sub(r'(<text class="st" x="378" y="636"[^>]*>)[^<]+(</text>)', rf'\g<1>{stars_count}+\g<2>', content)
        content = re.sub(r'(<text class="st" x="500" y="636"[^>]*>)[^<]+(</text>)', rf'\g<1>{followers_count}+\g<2>', content)

        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {f_name}")

update_stats_files()
update_banner_files()
print("[AutoUpdate] Successfully synchronized all profile assets!")
