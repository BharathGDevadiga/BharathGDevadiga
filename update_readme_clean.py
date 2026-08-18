README_CONTENT = """<div align="center">

<!-- ✨ One Piece Animated Banner ✨ -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./bharath-banner.svg?v=5">
  <source media="(prefers-color-scheme: light)" srcset="./bharath-banner-light.svg?v=5">
  <img src="./bharath-banner.svg?v=5" alt="Bharath G Devadiga - ECE Engineer" width="100%"/>
</picture>

</div>

<br/>

<div align="center">
<table border="0" cellpadding="12" cellspacing="0" width="100%" style="border-collapse: collapse;">
  <tr>
    <td width="30%" valign="middle" align="center" style="border: none;">
      <img src="./avatar.jpg" alt="Bharath G Devadiga" width="250" style="border-radius: 16px;" />
      <br/><br/>
      <b>⚡ Hardware Logic Designer &amp; Builder</b>
    </td>
    <td width="70%" valign="top" style="border: none;">
      <h3>🚀 Featured Engineering Projects</h3>
      <ul>
        <li>
          <a href="https://github.com/BharathGDevadiga/bharath-VIVEQA"><b>⚙️ FPGA / Vivado Accelerator Projects (VIVEQA)</b></a><br/>
          <sub>30-day FPGA and Verilog HDL journey using Xilinx Vivado with modular hardware logic.</sub>
        </li>
        <br/>
        <li>
          <a href="https://github.com/BharathGDevadiga/RTL-GDS-FLOW"><b>⚡ RTL to GDS Flow (VLSI Physical Design)</b></a><br/>
          <sub>Complete ASIC design flow from UART digital simulation to CMOS layout in KLayout.</sub>
        </li>
        <br/>
        <li>
          <a href="https://github.com/BharathGDevadiga/fullstack-web-apps-suite"><b>💻 Fullstack &amp; Embedded Mobile Suite</b></a><br/>
          <sub>Interactive Android applications with secure paywalls and hardware integrations.</sub>
        </li>
      </ul>
      <br/>
      <blockquote>
        <i>"Hardware is my canvas, Logic is my superpower — I don't just write software, I design the silicon that runs it!"</i>
      </blockquote>
    </td>
  </tr>
</table>
</div>

<br/>

---

<h2 align="center">📊 GitHub Analytics &amp; Achievements</h2>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-stats.svg?v=4">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-stats-light.svg?v=4">
    <img src="./bharath-stats.svg?v=4" alt="GitHub Stats" width="48%" />
  </picture>
  &nbsp;
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-langs.svg?v=4">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-langs-light.svg?v=4">
    <img src="./bharath-langs.svg?v=4" alt="Top Languages" width="48%" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=0d1e30&ring=22d3ee&fire=f59e0b&currStreakLabel=4ade80">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=ffffff&ring=0284c7&fire=d97706&currStreakLabel=16a34a&labels=0f172a&dates=334155&stat=0f172a">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=0d1e30&ring=22d3ee&fire=f59e0b&currStreakLabel=4ade80" alt="GitHub Streak" width="100%" />
  </picture>
</div>

<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-trophies.svg?v=4">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-trophies-light.svg?v=4">
    <img src="./bharath-trophies.svg?v=4" alt="Trophies" width="100%" />
  </picture>
</div>

---

<h2 align="center">🤝 Let's Connect &amp; Collaborate</h2>

<div align="center">
  <a href="https://linkedin.com/in/bharathgdevadiga" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  &nbsp;
  <a href="mailto:bharathgdudupi@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
  &nbsp;
  <a href="https://github.com/BharathGDevadiga" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</div>

<br/>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README_CONTENT)

with open("build_readme_v2.py", "w", encoding="utf-8") as f:
    f.write(f'README_CONTENT = """{README_CONTENT}"""\nwith open("README.md", "w", encoding="utf-8") as f:\n    f.write(README_CONTENT)\n')

print("Updated README.md with clean layout and no redundant activity graphs!")
