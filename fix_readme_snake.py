import re

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# 1. Remove Snake section
snake_pattern = re.compile(r'<br/>\s*<div align="center">\s*<h3>.*?Watch the snake.*?</div>\s*---', re.DOTALL | re.IGNORECASE)
readme = re.sub(snake_pattern, '---', readme)

# 2. Fix Activity Graph
act_pattern = re.compile(r'<img src="https://github-readme-activity-graph\.vercel\.app/graph\?username=BharathGDevadiga&bg_color=170e28&color=ff7eb6&line=8b5cf6&point=e879f9&area=true&area_color=8b5cf6&hide_border=true&custom_title=[^"]+" alt="Activity Graph" width="100%" />')
act_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=0d1e30&color=22d3ee&line=22d3ee&point=f59e0b&area=true&area_color=22d3ee&hide_border=true&custom_title=Bharath's%20Contribution%20Graph">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=ffffff&color=0284c7&line=0284c7&point=d97706&area=true&area_color=0284c7&hide_border=true&title_color=0f172a&custom_title=Bharath's%20Contribution%20Graph">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=0d1e30&color=22d3ee&line=22d3ee&point=f59e0b&area=true&area_color=22d3ee&hide_border=true&custom_title=Bharath's%20Contribution%20Graph" alt="Activity Graph" width="100%" />
  </picture>'''
readme = re.sub(act_pattern, act_new, readme)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Updated README.md")
