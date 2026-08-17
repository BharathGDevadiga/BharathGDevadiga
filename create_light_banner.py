import re

with open("bharath-banner.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# Backgrounds
svg = svg.replace('#090e1b', '#f1f5f9')
svg = svg.replace('#0c1222', '#ffffff')
svg = svg.replace('#070b16', '#f8fafc')

# Panels and strokes
svg = svg.replace('#1e2a3a', '#cbd5e1')
svg = svg.replace('#0d1e30', '#ffffff')
svg = svg.replace('#1a3a5c', '#cbd5e1')
svg = svg.replace('#07111e', '#f8fafc')
svg = svg.replace('#0f1e30', '#e2e8f0')

# Text Colors
svg = svg.replace('#e6edf3', '#0f172a')
svg = svg.replace('#cdd3dd', '#334155')
svg = svg.replace('#9aa4b2', '#64748b')
svg = svg.replace('#c9d1d9', '#334155')
svg = svg.replace('#8b949e', '#64748b')

# For light theme, some glowing elements might need slightly darker text 
# (but the accents cyan #22d3ee, amber #f59e0b, green #4ade80 are usually visible enough on white).
# However, cyan #22d3ee on white is 1.34 contrast. We should probably darken the cyan/amber/green text a bit.
# #22d3ee -> #0284c7 (darker cyan/blue)
# #f59e0b -> #d97706 (darker amber)
# #4ade80 -> #16a34a (darker green)
# #818cf8 -> #4f46e5 (darker indigo)

# Let's replace only the solid fills, not the glow stops (if we can help it), but doing a global replace is easier.
# Actually, global replace is fine because the gradients will just transition between darker colors.
# Wait, if we darken the gradients, they won't look like glowing lights anymore.
# Let's just create a new SVG for light mode.

replacements = {
    '#090e1b': '#e2e8f0',
    '#0c1222': '#ffffff',
    '#070b16': '#f1f5f9',
    
    '#1e2a3a': '#cbd5e1',
    '#0d1e30': '#ffffff',
    '#1a3a5c': '#cbd5e1',
    '#07111e': '#f8fafc',
    '#0f1e30': '#e2e8f0',
    
    '#e6edf3': '#0f172a',
    '#cdd3dd': '#334155',
    '#9aa4b2': '#64748b',
    '#c9d1d9': '#334155',
    '#8b949e': '#64748b',

    # Darker accents for light mode visibility
    '#22d3ee': '#0284c7', 
    '#38bdf8': '#0369a1',
    '#06b6d4': '#0284c7',
    
    '#f59e0b': '#d97706',
    '#fcd34d': '#b45309',
    
    '#4ade80': '#16a34a',
    '#86efac': '#15803d',
    
    '#818cf8': '#4f46e5',
    '#a5b4fc': '#4338ca',
    
    'rgba(34,211,238,.10)': 'rgba(2,132,199,.15)',
    'rgba(74,222,128,.12)': 'rgba(22,163,74,.15)',
    'rgba(245,158,11,.10)': 'rgba(217,119,6,.15)',
    'rgba(129,140,248,.12)': 'rgba(79,70,229,.15)'
}

for old, new in replacements.items():
    svg = svg.replace(old, new)

with open("bharath-banner-light.svg", "w", encoding="utf-8") as f:
    f.write(svg)
    
print("Created bharath-banner-light.svg!")
