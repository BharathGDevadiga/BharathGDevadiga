import os

files = ["bharath-stats.svg", "bharath-langs.svg", "bharath-trophies.svg"]

dark_replacements = {
    # Replace pink/purple with cyan/amber/green for the dark theme
    '#ff7eb6': '#22d3ee',
    '#c084fc': '#f59e0b',
    '#e879f9': '#4ade80',
    '#8b5cf6': '#0284c7',
    '#170e28': '#0d1e30',
    '#30224b': '#1a3a5c',
    '#0c0617': '#090e1b'
}

light_replacements = {
    # Base backgrounds
    '#090e1b': '#f1f5f9',
    '#0d1e30': '#ffffff',
    '#1a3a5c': '#cbd5e1',
    # Text colors
    '#e6edf3': '#0f172a',
    '#cdd3dd': '#334155',
    '#8b949e': '#64748b',
    # Accents (darker for light mode visibility)
    '#22d3ee': '#0284c7', 
    '#f59e0b': '#d97706',
    '#4ade80': '#16a34a',
    '#0284c7': '#0369a1',
    # Shine effects
    '#fff': '#000',
    'stop-opacity=".07"': 'stop-opacity=".03"'
}

for file in files:
    if not os.path.exists(file):
        continue
        
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Update Dark mode to new palette
    for old, new in dark_replacements.items():
        content = content.replace(old, new)
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Generate Light mode
    light_content = content
    for old, new in light_replacements.items():
        light_content = light_content.replace(old, new)
        
    light_file = file.replace(".svg", "-light.svg")
    with open(light_file, "w", encoding="utf-8") as f:
        f.write(light_content)

print("Updated stats and created light versions!")
