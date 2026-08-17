import base64
import re

with open("one_piece_small.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

b64_str = f"data:image/jpeg;base64,{encoded_string}"

# Read from local clone
with open("temp_repo/megha-banner.svg", "r", encoding="utf-8") as f:
    banner = f.read()

banner = banner.replace('Megha Mittal - Frontend Developer', 'Bharath G Devadiga - ECE Engineer')

# Replace image
img_pattern = r'<image x="722" y="152" width="558" height="522" href="data:image/png;base64,[^"]+"/>'
new_img = f'<image x="722" y="152" width="558" height="522" preserveAspectRatio="xMidYMid slice" href="{b64_str}"/>'
banner = re.sub(img_pattern, new_img, banner)

# Replace the name group properly
name_start = banner.find('<g transform="translate(48,196)" fill="url(#nameg)" filter="url(#glow)">')
next_g = banner.find('<g class="hb"', name_start)

new_name_html = '''<g transform="translate(48,196)" fill="url(#nameg)" filter="url(#glow)">
<text x="0" y="60" font-family="Arial, sans-serif" font-size="70" font-style="italic" font-weight="bold" letter-spacing="2">Bharath G Devadiga</text>
</g>
'''

banner = banner[:name_start] + new_name_html + banner[next_g:]

# Text replacements
banner = banner.replace("&lt; Frontend Developer /&gt;", "&lt; ECE &amp; Embedded /&gt;")
banner = banner.replace("&lt; JavaScript Enthusiast /&gt;", "&lt; VLSI &amp; FPGA Design /&gt;")
banner = banner.replace("&lt; SQL • SAP Workflows /&gt;", "&lt; C++ • ESP32 • IoT /&gt;")
banner = banner.replace("&lt; Anime Website Creator /&gt;", "&lt; Android App Developer /&gt;")

banner = banner.replace("megha@frontend-developer", "bharath@ece-engineer")
banner = banner.replace(">HTML<", ">Verilog<")
banner = banner.replace(">CSS<", ">C++<")
banner = banner.replace(">JavaScript<", ">Java<")
banner = banner.replace(">React<", ">ESP32<")
banner = banner.replace(">SAP<", ">VLSI<")
banner = banner.replace(">SQL<", ">IoT<")
banner = banner.replace(">Responsive UI<", ">Android Studio<")

banner = banner.replace("I build responsive, user-friendly and impactful web experiences.", "I bridge the gap between hardware and software systems.")
banner = banner.replace("Always learning, always building.", "Building the future, one circuit at a time.")
banner = banner.replace("Turning ideas into real world solutions.", "I design the hardware logic that runs the software.")

banner = banner.replace("I don't watch anime,", "I don't just build software,")
banner = banner.replace("code</tspan><tspan fill=\"#e6edf3\"> anime.</tspan>", "design</tspan><tspan fill=\"#e6edf3\"> the hardware.</tspan>")

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(banner)

print("Fixed banner generated")
