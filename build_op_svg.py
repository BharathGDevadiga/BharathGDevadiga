import re
import urllib.request
import base64

# Base64 encode the One Piece image
with open("one_piece_banner.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

b64_str = f"data:image/jpeg;base64,{encoded_string}"

# Download Megha's banner
banner_url = "https://raw.githubusercontent.com/Meghamittal0920/Meghamittal0920/main/megha-banner.svg"
req = urllib.request.urlopen(banner_url)
banner = req.read().decode('utf-8')

# Replace the image
# We look for the image tag that has href="data:image/png;base64,...
# Since the regex might be tricky, we'll find the image tag by its coordinates
img_tag_pattern = r'<image x="722" y="152" width="558" height="522" href="data:image/png;base64,.*?"/>'
new_img_tag = f'<image x="722" y="152" width="558" height="522" preserveAspectRatio="xMidYMid slice" href="{b64_str}"/>'
banner = re.sub(img_tag_pattern, new_img_tag, banner, flags=re.DOTALL)

# Replace the name paths with text
name_group_pattern = r'(<g transform="translate\(48,196\)" fill="url\(#nameg\)" filter="url\(#glow\)">).*?(</g>)'
new_name = r'\1\n<text x="0" y="60" font-family="Arial, sans-serif" font-size="70" font-style="italic" font-weight="bold" letter-spacing="2">Bharath G Devadiga</text>\n\2'
banner = re.sub(name_group_pattern, new_name, banner, flags=re.DOTALL)

# Replace roles
banner = banner.replace("&lt; Frontend Developer /&gt;", "&lt; ECE &amp; Embedded /&gt;")
banner = banner.replace("&lt; JavaScript Enthusiast /&gt;", "&lt; VLSI &amp; FPGA Design /&gt;")
banner = banner.replace("&lt; SQL • SAP Workflows /&gt;", "&lt; C++ • ESP32 • IoT /&gt;")
banner = banner.replace("&lt; Anime Website Creator /&gt;", "&lt; Android App Developer /&gt;")

# Replace terminal prompt
banner = banner.replace("megha@frontend-developer", "bharath@ece-engineer")

# Replace Tech I Know section
banner = banner.replace(">HTML<", ">Verilog<")
banner = banner.replace(">CSS<", ">C++<")
banner = banner.replace(">JavaScript<", ">Java<")
banner = banner.replace(">React<", ">ESP32<")
banner = banner.replace(">SAP<", ">VLSI<")
banner = banner.replace(">SQL<", ">IoT<")
banner = banner.replace(">Responsive UI<", ">Android Studio<")

# Replace About Me
banner = banner.replace("I build responsive, user-friendly and impactful web experiences.", "I bridge the gap between hardware and software systems.")
banner = banner.replace("Turning ideas into real world solutions.", "I design the hardware logic that runs the software.")

# Replace quote
banner = banner.replace("I don't watch anime,", "I don't just build software,")
banner = banner.replace("code</tspan><tspan fill=\"#e6edf3\"> anime.</tspan>", "design</tspan><tspan fill=\"#e6edf3\"> the hardware.</tspan>")

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(banner)

print("One Piece banner generated successfully!")
