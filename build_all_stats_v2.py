# Build professional Stats, Languages, and Trophies SVGs for Bharath

# =========================================================================
# 1. BHARATH GITHUB STATS (Dark & Light)
# =========================================================================
STATS_SVG_DARK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="460" height="260" role="img" aria-label="Bharath G Devadiga's GitHub Stats">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeSlide{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rankPulse{0%,100%{opacity:.85}50%{opacity:1}}
@keyframes shineX{0%{transform:translateX(-160px) skewX(-15deg)}60%,100%{transform:translateX(560px) skewX(-15deg)}}
.row{opacity:0;animation:fadeSlide .5s ease forwards}
.rk{animation:rankPulse 2.4s ease-in-out infinite}
.sh{animation:shineX 4.5s ease-in-out 2.4s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#f59e0b;#22d3ee" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#f59e0b;#22d3ee;#f59e0b" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#f59e0b"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".06"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="458" height="258" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="1" y="1" width="458" height="258" rx="14" fill="#0d1e30" stroke="url(#tg)" stroke-width="1.5"/>
<text x="24" y="38" font-size="16" font-weight="bold" fill="url(#tg)">⚡ Bharath's GitHub Stats</text>

  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="76" font-size="14">⭐</text>
    <text x="52" y="76" font-size="13.5" fill="#cdd3dd">Total Stars Earned:</text>
    <text x="270" y="76" text-anchor="end" font-size="14" font-weight="bold" fill="#fde047">50+</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="110" font-size="14">💻</text>
    <text x="52" y="110" font-size="13.5" fill="#cdd3dd">Total Commits:</text>
    <text x="270" y="110" text-anchor="end" font-size="14" font-weight="bold" fill="#7dd3fc">500+</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="144" font-size="14">📦</text>
    <text x="52" y="144" font-size="13.5" fill="#cdd3dd">Public Repos:</text>
    <text x="270" y="144" text-anchor="end" font-size="14" font-weight="bold" fill="#4ade80">12+</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="178" font-size="14">👥</text>
    <text x="52" y="178" font-size="13.5" fill="#cdd3dd">Followers:</text>
    <text x="270" y="178" text-anchor="end" font-size="14" font-weight="bold" fill="#f59e0b">25+</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="212" font-size="14">⚙️</text>
    <text x="52" y="212" font-size="13.5" fill="#cdd3dd">Hardware / VLSI:</text>
    <text x="270" y="212" text-anchor="end" font-size="14" font-weight="bold" fill="#22d3ee">6+</text>
  </g>

<!-- Rank ring -->
<g transform="translate(366,146)">
  <circle r="46" fill="none" stroke="#1a3a5c" stroke-width="8"/>
  <circle r="46" fill="none" stroke="url(#ringg)" stroke-width="8" stroke-linecap="round"
    stroke-dasharray="225.2 289" stroke-dashoffset="225.2" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="225.2" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk" y="12" text-anchor="middle" font-size="36" font-weight="bold" fill="#22d3ee" filter="url(#g)">A+</text>
  <text y="68" text-anchor="middle" font-size="10.5" fill="#9aa4b2" opacity="0" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>
<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="90" height="260" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>"""

STATS_SVG_LIGHT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="460" height="260" role="img" aria-label="Bharath G Devadiga's GitHub Stats">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeSlide{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rankPulse{0%,100%{opacity:.85}50%{opacity:1}}
@keyframes shineX{0%{transform:translateX(-160px) skewX(-15deg)}60%,100%{transform:translateX(560px) skewX(-15deg)}}
.row{opacity:0;animation:fadeSlide .5s ease forwards}
.rk{animation:rankPulse 2.4s ease-in-out infinite}
.sh{animation:shineX 4.5s ease-in-out 2.4s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#0284c7;#d97706;#0284c7" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#d97706;#0284c7;#d97706" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#d97706"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#000" stop-opacity="0"/><stop offset="50%" stop-color="#000" stop-opacity=".03"/><stop offset="100%" stop-color="#000" stop-opacity="0"/></linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="458" height="258" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="1.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="1" y="1" width="458" height="258" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
<text x="24" y="38" font-size="16" font-weight="bold" fill="url(#tg)">⚡ Bharath's GitHub Stats</text>

  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="76" font-size="14">⭐</text>
    <text x="52" y="76" font-size="13.5" fill="#334155">Total Stars Earned:</text>
    <text x="270" y="76" text-anchor="end" font-size="14" font-weight="bold" fill="#b45309">50+</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="110" font-size="14">💻</text>
    <text x="52" y="110" font-size="13.5" fill="#334155">Total Commits:</text>
    <text x="270" y="110" text-anchor="end" font-size="14" font-weight="bold" fill="#0284c7">500+</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="144" font-size="14">📦</text>
    <text x="52" y="144" font-size="13.5" fill="#334155">Public Repos:</text>
    <text x="270" y="144" text-anchor="end" font-size="14" font-weight="bold" fill="#16a34a">12+</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="178" font-size="14">👥</text>
    <text x="52" y="178" font-size="13.5" fill="#334155">Followers:</text>
    <text x="270" y="178" text-anchor="end" font-size="14" font-weight="bold" fill="#d97706">25+</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="212" font-size="14">⚙️</text>
    <text x="52" y="212" font-size="13.5" fill="#334155">Hardware / VLSI:</text>
    <text x="270" y="212" text-anchor="end" font-size="14" font-weight="bold" fill="#0284c7">6+</text>
  </g>

<!-- Rank ring -->
<g transform="translate(366,146)">
  <circle r="46" fill="none" stroke="#e2e8f0" stroke-width="8"/>
  <circle r="46" fill="none" stroke="url(#ringg)" stroke-width="8" stroke-linecap="round"
    stroke-dasharray="225.2 289" stroke-dashoffset="225.2" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="225.2" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk" y="12" text-anchor="middle" font-size="36" font-weight="bold" fill="#0284c7" filter="url(#g)">A+</text>
  <text y="68" text-anchor="middle" font-size="10.5" fill="#64748b" opacity="0" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>
<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="90" height="260" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>"""

with open("bharath-stats.svg", "w", encoding="utf-8") as f:
    f.write(STATS_SVG_DARK)
with open("bharath-stats-light.svg", "w", encoding="utf-8") as f:
    f.write(STATS_SVG_LIGHT)

# =========================================================================
# 2. TOP LANGUAGES (Dark & Light) - Height: 260 (Identical to stats!)
# =========================================================================
LANGS_SVG_DARK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="460" height="260" role="img" aria-label="Bharath G Devadiga's Top Languages">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes shineX{0%{transform:translateX(-140px)}60%,100%{transform:translateX(500px)}}
.row{opacity:0;animation:fadeUp .5s ease forwards}
.sh{animation:shineX 4s ease-in-out 2.2s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#f59e0b;#22d3ee" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#f59e0b;#22d3ee;#f59e0b" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".06"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cardc"><rect x="1" y="1" width="458" height="258" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="52" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="420" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
</defs>
<rect x="1" y="1" width="458" height="258" rx="14" fill="#0d1e30" stroke="url(#tg)" stroke-width="1.5"/>
<text x="20" y="34" font-size="16" font-weight="bold" fill="url(#tg)">📊 Top Languages</text>

<!-- Progress Bar Stack (Verilog: 45%, C/C++: 25%, Java: 18%, Python: 12%) -->
<g clip-path="url(#stackc)">
  <rect x="20" y="52" width="189" height="11" fill="#22d3ee"/>
  <rect x="209" y="52" width="105" height="11" fill="#38bdf8"/>
  <rect x="314" y="52" width="75.6" height="11" fill="#f59e0b"/>
  <rect x="389.6" y="52" width="50.4" height="11" fill="#4ade80"/>
</g>

  <!-- Row 1: Verilog -->
  <g class="row" style="animation-delay:0.80s">
    <circle cx="28" cy="88" r="5" fill="#22d3ee"/>
    <text x="42" y="93" font-size="13" fill="#e6edf3" font-weight="bold">Verilog / RTL</text>
    <text x="436" y="93" text-anchor="end" font-size="13" fill="#22d3ee" font-weight="bold">45.0%</text>
    <rect x="42" y="100" width="300" height="8" rx="4" fill="#1a3a5c"/>
    <rect x="42" y="100" width="135" height="8" rx="4" fill="#22d3ee">
      <animate attributeName="width" from="0" to="135" dur="1.1s" begin="0.95s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Row 2: C / C++ -->
  <g class="row" style="animation-delay:1.10s">
    <circle cx="28" cy="128" r="5" fill="#38bdf8"/>
    <text x="42" y="133" font-size="13" fill="#e6edf3" font-weight="bold">C / C++ (Embedded)</text>
    <text x="436" y="133" text-anchor="end" font-size="13" fill="#38bdf8" font-weight="bold">25.0%</text>
    <rect x="42" y="140" width="300" height="8" rx="4" fill="#1a3a5c"/>
    <rect x="42" y="140" width="75" height="8" rx="4" fill="#38bdf8">
      <animate attributeName="width" from="0" to="75" dur="1.1s" begin="1.25s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Row 3: Java / Android -->
  <g class="row" style="animation-delay:1.40s">
    <circle cx="28" cy="168" r="5" fill="#f59e0b"/>
    <text x="42" y="173" font-size="13" fill="#e6edf3" font-weight="bold">Java / Android</text>
    <text x="436" y="173" text-anchor="end" font-size="13" fill="#f59e0b" font-weight="bold">18.0%</text>
    <rect x="42" y="180" width="300" height="8" rx="4" fill="#1a3a5c"/>
    <rect x="42" y="180" width="54" height="8" rx="4" fill="#f59e0b">
      <animate attributeName="width" from="0" to="54" dur="1.1s" begin="1.55s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Row 4: Python / Web -->
  <g class="row" style="animation-delay:1.70s">
    <circle cx="28" cy="208" r="5" fill="#4ade80"/>
    <text x="42" y="213" font-size="13" fill="#e6edf3" font-weight="bold">Python / Web Tech</text>
    <text x="436" y="213" text-anchor="end" font-size="13" fill="#4ade80" font-weight="bold">12.0%</text>
    <rect x="42" y="220" width="300" height="8" rx="4" fill="#1a3a5c"/>
    <rect x="42" y="220" width="36" height="8" rx="4" fill="#4ade80">
      <animate attributeName="width" from="0" to="36" dur="1.1s" begin="1.85s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="90" height="260" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>"""

LANGS_SVG_LIGHT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" width="460" height="260" role="img" aria-label="Bharath G Devadiga's Top Languages">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes shineX{0%{transform:translateX(-140px)}60%,100%{transform:translateX(500px)}}
.row{opacity:0;animation:fadeUp .5s ease forwards}
.sh{animation:shineX 4s ease-in-out 2.2s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#0284c7;#d97706;#0284c7" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#d97706;#0284c7;#d97706" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#000" stop-opacity="0"/><stop offset="50%" stop-color="#000" stop-opacity=".03"/><stop offset="100%" stop-color="#000" stop-opacity="0"/></linearGradient>
<clipPath id="cardc"><rect x="1" y="1" width="458" height="258" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="52" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="420" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
</defs>
<rect x="1" y="1" width="458" height="258" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
<text x="20" y="34" font-size="16" font-weight="bold" fill="url(#tg)">📊 Top Languages</text>

<g clip-path="url(#stackc)">
  <rect x="20" y="52" width="189" height="11" fill="#0284c7"/>
  <rect x="209" y="52" width="105" height="11" fill="#0369a1"/>
  <rect x="314" y="52" width="75.6" height="11" fill="#d97706"/>
  <rect x="389.6" y="52" width="50.4" height="11" fill="#16a34a"/>
</g>

  <g class="row" style="animation-delay:0.80s">
    <circle cx="28" cy="88" r="5" fill="#0284c7"/>
    <text x="42" y="93" font-size="13" fill="#0f172a" font-weight="bold">Verilog / RTL</text>
    <text x="436" y="93" text-anchor="end" font-size="13" fill="#0284c7" font-weight="bold">45.0%</text>
    <rect x="42" y="100" width="300" height="8" rx="4" fill="#e2e8f0"/>
    <rect x="42" y="100" width="135" height="8" rx="4" fill="#0284c7">
      <animate attributeName="width" from="0" to="135" dur="1.1s" begin="0.95s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <g class="row" style="animation-delay:1.10s">
    <circle cx="28" cy="128" r="5" fill="#0369a1"/>
    <text x="42" y="133" font-size="13" fill="#0f172a" font-weight="bold">C / C++ (Embedded)</text>
    <text x="436" y="133" text-anchor="end" font-size="13" fill="#0369a1" font-weight="bold">25.0%</text>
    <rect x="42" y="140" width="300" height="8" rx="4" fill="#e2e8f0"/>
    <rect x="42" y="140" width="75" height="8" rx="4" fill="#0369a1">
      <animate attributeName="width" from="0" to="75" dur="1.1s" begin="1.25s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <g class="row" style="animation-delay:1.40s">
    <circle cx="28" cy="168" r="5" fill="#d97706"/>
    <text x="42" y="173" font-size="13" fill="#0f172a" font-weight="bold">Java / Android</text>
    <text x="436" y="173" text-anchor="end" font-size="13" fill="#d97706" font-weight="bold">18.0%</text>
    <rect x="42" y="180" width="300" height="8" rx="4" fill="#e2e8f0"/>
    <rect x="42" y="180" width="54" height="8" rx="4" fill="#d97706">
      <animate attributeName="width" from="0" to="54" dur="1.1s" begin="1.55s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <g class="row" style="animation-delay:1.70s">
    <circle cx="28" cy="208" r="5" fill="#16a34a"/>
    <text x="42" y="213" font-size="13" fill="#0f172a" font-weight="bold">Python / Web Tech</text>
    <text x="436" y="213" text-anchor="end" font-size="13" fill="#16a34a" font-weight="bold">12.0%</text>
    <rect x="42" y="220" width="300" height="8" rx="4" fill="#e2e8f0"/>
    <rect x="42" y="220" width="36" height="8" rx="4" fill="#16a34a">
      <animate attributeName="width" from="0" to="36" dur="1.1s" begin="1.85s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="90" height="260" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>"""

with open("bharath-langs.svg", "w", encoding="utf-8") as f:
    f.write(LANGS_SVG_DARK)
with open("bharath-langs-light.svg", "w", encoding="utf-8") as f:
    f.write(LANGS_SVG_LIGHT)

# =========================================================================
# 3. TROPHIES (Dark & Light)
# =========================================================================
TROPHIES_SVG_DARK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes popCell{0%{opacity:0;transform:translateY(16px) scale(.85)}70%{opacity:1;transform:translateY(-3px) scale(1.03)}100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes rankGlow{0%,100%{opacity:.75}50%{opacity:1}}
@keyframes shineX2{0%{transform:translateX(-200px) skewX(-15deg)}60%,100%{transform:translateX(1172px) skewX(-15deg)}}
.cell{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}
.rk{animation:rankGlow 2.2s ease-in-out infinite}
.sh2{animation:shineX2 5s ease-in-out 2s infinite}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
</defs>

  <!-- Cell 1: Hardware Artisan -->
  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#22d3ee" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="96.0" y="52" text-anchor="middle" font-size="30">⚙️</text>
    <text class="rk" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#22d3ee" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Silicon Dev</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">VLSI &amp; FPGA x6</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#22d3ee">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 2: Starstruck -->
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#fde047" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="276.0" y="52" text-anchor="middle" font-size="30">🌟</text>
    <text class="rk" x="344" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#fde047" style="animation-delay:0.88s">S</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Starstruck</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">GitHub Badge</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#fde047">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 3: Stargazer -->
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#4ade80" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="456.0" y="52" text-anchor="middle" font-size="30">⭐</text>
    <text class="rk" x="524" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#4ade80" style="animation-delay:1.06s">A</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Stargazer</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Stars 50+</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#4ade80">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 4: Hardware Innovator -->
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#f59e0b" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="636.0" y="52" text-anchor="middle" font-size="30">⚡</text>
    <text class="rk" x="704" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#f59e0b" style="animation-delay:1.24s">A</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Hardware Pro</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">IoT &amp; Embedded</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#f59e0b">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 5: Committer -->
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#38bdf8" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="816.0" y="52" text-anchor="middle" font-size="30">💻</text>
    <text class="rk" x="884" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#38bdf8" style="animation-delay:1.42s">S</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">Committer</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Commits 500+</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#38bdf8">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 6: Builder -->
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="#0d1e30" stroke="#818cf8" stroke-opacity=".55" stroke-width="1.3"/>
    <text x="996.0" y="52" text-anchor="middle" font-size="30">📱</text>
    <text class="rk" x="1064" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#818cf8" style="animation-delay:1.60s">A</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#e6edf3">App Builder</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#9aa4b2">Android Apps</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#1a3a5c"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#818cf8">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="120" height="168" fill="url(#shg2)" transform="skewX(-15)"/></g>
</svg>"""

TROPHIES_SVG_LIGHT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes popCell{0%{opacity:0;transform:translateY(16px) scale(.85)}70%{opacity:1;transform:translateY(-3px) scale(1.03)}100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes rankGlow{0%,100%{opacity:.75}50%{opacity:1}}
@keyframes shineX2{0%{transform:translateX(-200px) skewX(-15deg)}60%,100%{transform:translateX(1172px) skewX(-15deg)}}
.cell{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}
.rk{animation:rankGlow 2.2s ease-in-out infinite}
.sh2{animation:shineX2 5s ease-in-out 2s infinite}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#000" stop-opacity="0"/><stop offset="50%" stop-color="#000" stop-opacity=".03"/><stop offset="100%" stop-color="#000" stop-opacity="0"/></linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
</defs>

  <!-- Cell 1: Hardware Artisan -->
  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="96.0" y="52" text-anchor="middle" font-size="30">⚙️</text>
    <text class="rk" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#0284c7" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Silicon Dev</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">VLSI &amp; FPGA x6</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#0284c7">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 2: Starstruck -->
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="276.0" y="52" text-anchor="middle" font-size="30">🌟</text>
    <text class="rk" x="344" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#b45309" style="animation-delay:0.88s">S</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Starstruck</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">GitHub Badge</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#d97706">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 3: Stargazer -->
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="456.0" y="52" text-anchor="middle" font-size="30">⭐</text>
    <text class="rk" x="524" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#16a34a" style="animation-delay:1.06s">A</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Stargazer</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">Stars 50+</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#16a34a">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 4: Hardware Innovator -->
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="636.0" y="52" text-anchor="middle" font-size="30">⚡</text>
    <text class="rk" x="704" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#d97706" style="animation-delay:1.24s">A</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Hardware Pro</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">IoT &amp; Embedded</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#d97706">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 5: Committer -->
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="816.0" y="52" text-anchor="middle" font-size="30">💻</text>
    <text class="rk" x="884" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#0369a1" style="animation-delay:1.42s">S</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">Committer</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">Commits 500+</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#0369a1">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 6: Builder -->
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
    <text x="996.0" y="52" text-anchor="middle" font-size="30">📱</text>
    <text class="rk" x="1064" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#4f46e5" style="animation-delay:1.60s">A</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">App Builder</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#64748b">Android Apps</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#e2e8f0"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#4f46e5">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="120" height="168" fill="url(#shg2)" transform="skewX(-15)"/></g>
</svg>"""

with open("bharath-trophies.svg", "w", encoding="utf-8") as f:
    f.write(TROPHIES_SVG_DARK)
with open("bharath-trophies-light.svg", "w", encoding="utf-8") as f:
    f.write(TROPHIES_SVG_LIGHT)

print("Generated all updated dark and light stats SVGs!")
