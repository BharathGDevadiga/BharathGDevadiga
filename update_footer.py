import re

with open("bharath-banner.svg", "r", encoding="utf-8") as f:
    banner = f.read()

# Socials
banner = banner.replace('Meghamittal0920', 'BharathGDevadiga')
banner = banner.replace('meghamittal563@gmail.com', 'bharathgdevadiga@gmail.com')
banner = banner.replace('meghamittal92000', 'bharath-devadiga')

# Quote
banner = banner.replace('Code is my art, Logic is my superpower.', 'Hardware is my canvas, Logic is my superpower.')
banner = banner.replace('❤', '⚡')

# Code block
banner = banner.replace('buildDreams', 'designHardware')
banner = banner.replace('dreams.jsx', 'hardware.v')
banner = banner.replace('className', 'module')
banner = banner.replace('="dreams"', '="future"')
banner = banner.replace('>Code<', '>Design<')
banner = banner.replace('>Repeat<', '>Simulate<')
banner = banner.replace('>Success<', '>Tapeout<')

# Neon sign
banner = banner.replace('KEEP CODING', 'KEEP DESIGNING')
banner = banner.replace('KEEP GROWING', 'KEEP BUILDING')

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(banner)

print("Footer updated!")
