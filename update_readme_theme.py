import re

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace Stats
stats_old = '<img src="./bharath-stats.svg?v=1" alt="GitHub Stats" width="48%" />'
stats_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-stats.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-stats-light.svg?v=2">
    <img src="./bharath-stats.svg?v=2" alt="GitHub Stats" width="48%" />
  </picture>'''
readme = readme.replace(stats_old, stats_new)

# Replace Langs
langs_old = '<img src="./bharath-langs.svg?v=1" alt="Top Languages" width="48%" />'
langs_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-langs.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-langs-light.svg?v=2">
    <img src="./bharath-langs.svg?v=2" alt="Top Languages" width="48%" />
  </picture>'''
readme = readme.replace(langs_old, langs_new)

# Replace Trophies
trophies_old = '<img src="./bharath-trophies.svg?v=1" alt="Trophies" width="100%" />'
trophies_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./bharath-trophies.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="./bharath-trophies-light.svg?v=2">
    <img src="./bharath-trophies.svg?v=2" alt="Trophies" width="100%" />
  </picture>'''
readme = readme.replace(trophies_old, trophies_new)

# Replace Streak (Dark: #0d1e30 bg, #22d3ee ring, #f59e0b fire. Light: #ffffff bg, #0284c7 ring, #d97706 fire)
streak_old = '<img src="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=170e28&ring=ff7eb6&fire=e879f9&currStreakLabel=c084fc" alt="GitHub Streak" width="100%" />'
streak_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=0d1e30&ring=22d3ee&fire=f59e0b&currStreakLabel=4ade80">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=ffffff&ring=0284c7&fire=d97706&currStreakLabel=16a34a&labels=0f172a&dates=334155&stat=0f172a">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=BharathGDevadiga&theme=radical&hide_border=true&background=0d1e30&ring=22d3ee&fire=f59e0b&currStreakLabel=4ade80" alt="GitHub Streak" width="100%" />
  </picture>'''
readme = readme.replace(streak_old, streak_new)

# Replace Activity Graph (Dark: #0d1e30 bg, #22d3ee line, #f59e0b point. Light: #ffffff bg, #0284c7 line, #d97706 point)
act_old = '<img src="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=170e28&color=ff7eb6&line=8b5cf6&point=e879f9&area=true&area_color=8b5cf6&hide_border=true&custom_title=bharath\'s%20Contribution%20Graph%20%F0%9F%93%88" alt="Activity Graph" width="100%" />'
act_new = '''<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=0d1e30&color=22d3ee&line=22d3ee&point=f59e0b&area=true&area_color=22d3ee&hide_border=true&custom_title=Bharath's%20Contribution%20Graph%20%F0%9F%93%88">
    <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=ffffff&color=0284c7&line=0284c7&point=d97706&area=true&area_color=0284c7&hide_border=true&title_color=0f172a&custom_title=Bharath's%20Contribution%20Graph%20%F0%9F%93%88">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=BharathGDevadiga&bg_color=0d1e30&color=22d3ee&line=22d3ee&point=f59e0b&area=true&area_color=22d3ee&hide_border=true&custom_title=Bharath's%20Contribution%20Graph%20%F0%9F%93%88" alt="Activity Graph" width="100%" />
  </picture>'''
readme = readme.replace(act_old, act_new)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Updated README.md with full light/dark mode support!")
