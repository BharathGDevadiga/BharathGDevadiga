import urllib.request

files = [
    "megha-stats.svg",
    "megha-langs.svg",
    "megha-trophies.svg"
]

base_url = "https://raw.githubusercontent.com/BharathGD/bharath/main/"

for file in files:
    try:
        req = urllib.request.urlopen(base_url + file)
        content = req.read().decode('utf-8')
        
        # Replace Megha with Bharath
        content = content.replace("Megha Mittal's GitHub Stats", "Bharath's GitHub Stats")
        content = content.replace("Megha", "Bharath")
        content = content.replace("meghamittal0920", "BharathGDevadiga")
        
        # Replace anime stats with tech stats
        content = content.replace("Anime Sites Built:", "Hardware Projects:")
        
        out_name = file.replace("megha-", "bharath-")
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully processed {out_name}")
    except Exception as e:
        print(f"Failed to process {file}: {e}")
