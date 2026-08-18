with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

tools_section = """---

<h2 align="center">🧰 EDA, Hardware &amp; Development Toolchain</h2>

<div align="center">

<p>
  <b>⚡ EDA &amp; VLSI Design</b><br/>
  <img src="https://img.shields.io/badge/Xilinx_Vivado-000000?style=for-the-badge&logo=amd&logoColor=white" alt="Xilinx Vivado"/>
  <img src="https://img.shields.io/badge/Synopsys-5C2D91?style=for-the-badge&logo=c&logoColor=white" alt="Synopsys"/>
  <img src="https://img.shields.io/badge/KiCad-31469C?style=for-the-badge&logo=kicad&logoColor=white" alt="KiCad"/>
  <img src="https://img.shields.io/badge/KLayout_(GDSII)-0284C7?style=for-the-badge&logo=diagram-next&logoColor=white" alt="KLayout"/>
  <img src="https://img.shields.io/badge/Yosys_Synthesis-1B2A4A?style=for-the-badge&logo=yosys&logoColor=white" alt="Yosys"/>
  <img src="https://img.shields.io/badge/NI_Multisim-004F9E?style=for-the-badge&logo=circuitverse&logoColor=white" alt="NI Multisim"/>
</p>

<p>
  <b>🔌 Embedded &amp; Firmware</b><br/>
  <img src="https://img.shields.io/badge/ESP--IDF_/_ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white" alt="ESP-IDF"/>
  <img src="https://img.shields.io/badge/Keil_µVision_5-0091BD?style=for-the-badge&logo=arm&logoColor=white" alt="Keil uVision"/>
  <img src="https://img.shields.io/badge/Icarus_Verilog-2C3E50?style=for-the-badge&logo=terminal&logoColor=white" alt="Icarus Verilog"/>
  <img src="https://img.shields.io/badge/Linux_/_Bash-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
</p>

<p>
  <b>💻 Software Engineering &amp; IDEs</b><br/>
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code"/>
  <img src="https://img.shields.io/badge/Android_Studio-3DDC84?style=for-the-badge&logo=androidstudio&logoColor=white" alt="Android Studio"/>
  <img src="https://img.shields.io/badge/IntelliJ_IDEA-000000?style=for-the-badge&logo=intellijidea&logoColor=white" alt="IntelliJ IDEA"/>
  <img src="https://img.shields.io/badge/Git_&_GitHub_Actions-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
</p>

</div>
"""

# Insert right before GitHub Analytics & Achievements
target = '<h2 align="center">📊 GitHub Analytics &amp; Achievements</h2>'
if target in readme:
    readme = readme.replace(target, tools_section + "\n" + target)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Successfully added curated EDA and Hardware Tools section to README.md!")
