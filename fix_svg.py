import base64
import re
import urllib.request

with open("one_piece_small.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

b64_str = f"data:image/jpeg;base64,{encoded_string}"

# 2. Re-download and modify Megha's banner
banner_url = "https://raw.githubusercontent.com/BharathGD/bharath/main/megha-banner.svg"
req = urllib.request.urlopen(banner_url)
banner = req.read().decode('utf-8')

# Fix aria label
banner = banner.replace('Megha Mittal - Frontend Developer', 'Bharath G Devadiga - ECE Engineer')

# Replace the girl image with One Piece image
img_tag_pattern = r'<image x="722" y="152" width="558" height="522" href="data:image/png;base64,.*?"/>'
new_img_tag = f'<image x="722" y="152" width="558" height="522" preserveAspectRatio="xMidYMid slice" href="{b64_str}"/>'
banner = re.sub(img_tag_pattern, new_img_tag, banner, flags=re.DOTALL)

# Name
name_group_pattern = r'(<g transform="translate\(48,196\)" fill="url\(#nameg\)" filter="url\(#glow\)">).*?(</g>)'
new_name = r'\1\n<text x="0" y="60" font-family="Arial, sans-serif" font-size="70" font-style="italic" font-weight="bold" letter-spacing="2">Bharath G Devadiga</text>\n\2'
banner = re.sub(name_group_pattern, new_name, banner, flags=re.DOTALL)

# Replace roles
banner = banner.replace("&lt; Frontend Developer /&gt;", "&lt; ECE &amp; Embedded /&gt;")
banner = banner.replace("&lt; JavaScript Enthusiast /&gt;", "&lt; VLSI &amp; FPGA Design /&gt;")
banner = banner.replace("&lt; SQL • SAP Workflows /&gt;", "&lt; C++ • ESP32 • IoT /&gt;")
banner = banner.replace("&lt; Anime Website Creator /&gt;", "&lt; Android App Developer /&gt;")

# Terminal prompt
banner = banner.replace("megha@frontend-developer", "bharath@ece-engineer")

# Tech
banner = banner.replace(">HTML<", ">Verilog<")
banner = banner.replace(">CSS<", ">C++<")
banner = banner.replace(">JavaScript<", ">Java<")
banner = banner.replace(">React<", ">ESP32<")
banner = banner.replace(">SAP<", ">VLSI<")
banner = banner.replace(">SQL<", ">IoT<")
banner = banner.replace(">Responsive UI<", ">Android Studio<")

# About Me
banner = banner.replace("I build responsive, user-friendly and impactful web experiences.", "I bridge the gap between hardware and software systems.")
banner = banner.replace("Always learning, always building.", "Building the future, one circuit at a time.")
banner = banner.replace("Turning ideas into real world solutions.", "I design the hardware logic that runs the software.")

# Quote
banner = banner.replace("I don't watch anime,", "I don't just build software,")
banner = banner.replace("code</tspan><tspan fill=\"#e6edf3\"> anime.</tspan>", "design</tspan><tspan fill=\"#e6edf3\"> the hardware.</tspan>")

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(banner)

print("SVG optimized and saved!")
