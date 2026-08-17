import os

files = ["README.md", "bharath-banner.svg", "bharath-banner-light.svg", "redesign_banner.py"]
old_emails = ["myasuslaptop45@gmail.com", "your.email@example.com"]
new_email = "bharathgdudupi@gmail.com"

for file in files:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        
        for old in old_emails:
            content = content.replace(old, new_email)
            
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file}")
