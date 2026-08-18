import os

files_to_update = [
    "README.md",
    "build_readme_v2.py",
    "bharath-banner.svg",
    "bharath-banner-light.svg",
    "build_framed_banner.py",
    "redesign_banner.py"
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace placeholder LinkedIn links
        new_content = content.replace("YOUR_LINKEDIN", "bharathgdevadiga")
        new_content = new_content.replace("bharath-g-devadiga", "bharathgdevadiga")
        
        if new_content != content:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated LinkedIn link in {filename}")
        else:
            print(f"No changes needed for {filename}")

print("LinkedIn URL update complete!")
