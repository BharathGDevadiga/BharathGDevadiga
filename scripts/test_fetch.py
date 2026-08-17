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

# 1. User Profile Data
user_data = fetch_json(f"https://api.github.com/users/{USERNAME}")
if user_data:
    public_repos = user_data.get("public_repos", 12)
    followers = user_data.get("followers", 25)
else:
    public_repos = 12
    followers = 25

# 2. Fetch User Repositories & Language Breakdown
repos_data = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100")
total_stars = 0
lang_bytes = {}

if repos_data and isinstance(repos_data, list):
    for repo in repos_data:
        total_stars += repo.get("stargazers_count", 0)
        lang = repo.get("language")
        if lang:
            lang_bytes[lang] = lang_bytes.get(lang, 0) + 1

print(f"User: {USERNAME} | Repos: {public_repos} | Followers: {followers} | Stars: {total_stars}")
print(f"Languages: {lang_bytes}")
