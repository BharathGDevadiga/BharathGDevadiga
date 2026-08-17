import base64
import os
import re

# Load One Piece Image
if os.path.exists("one_piece_small.jpg"):
    with open("one_piece_small.jpg", "rb") as f:
        img_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')
elif os.path.exists("one_piece_banner.jpg"):
    with open("one_piece_banner.jpg", "rb") as f:
        img_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode('utf-8')
else:
    with open("bharath-banner.svg", "r", encoding="utf-8") as f:
        m = re.search(r'href="(data:image/[^"]+)"', f.read())
        img_b64 = m.group(1) if m else ""

print(f"Loaded image b64 (length: {len(img_b64)})")

# =========================================================================
# 1. POLISHED DARK BANNER
# =========================================================================
DARK_BANNER = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 720" width="1280" height="720" role="img" aria-label="Bharath G Devadiga - ECE Engineer &amp; Logic Designer">
<title>Bharath G Devadiga &#8212; ECE Engineer</title>
<defs>
<style type="text/css"><![CDATA[
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
text { font-family: 'JetBrains Mono', 'SFMono-Regular', Consolas, Menlo, monospace; }
.title-t { font-family: 'Plus Jakarta Sans', 'Segoe UI', -apple-system, sans-serif; font-weight: 800; }
.sans-t { font-family: 'Plus Jakarta Sans', 'Segoe UI', -apple-system, sans-serif; }

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
@keyframes floatArt { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-7px); } }
@keyframes neonPulse { 0%, 100% { opacity: .75; filter: drop-shadow(0 0 4px #22d3ee); } 50% { opacity: 1; filter: drop-shadow(0 0 10px #22d3ee); } }
@keyframes scanSweep { 0% { transform: translateX(-100%); } 100% { transform: translateX(200%); } }

.fl-art { animation: floatArt 6s ease-in-out infinite; }
.np { animation: neonPulse 3s ease-in-out infinite; }
.pill { transition: transform .2s ease; cursor: pointer; }
.pill:hover { transform: translateY(-2px); }
]]></style>

<!-- BACKGROUND GRADIENTS -->
<linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#080e1a"/>
  <stop offset="50%" stop-color="#0c1626"/>
  <stop offset="100%" stop-color="#060b14"/>
</linearGradient>

<linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#38bdf8"/>
  <stop offset="50%" stop-color="#22d3ee"/>
  <stop offset="100%" stop-color="#f59e0b"/>
</linearGradient>

<linearGradient id="borderGrad" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".6"/>
  <stop offset="50%" stop-color="#f59e0b" stop-opacity=".3"/>
  <stop offset="100%" stop-color="#0284c7" stop-opacity=".6"/>
</linearGradient>

<linearGradient id="artBorder" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#38bdf8" stop-opacity=".8"/>
  <stop offset="50%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="100%" stop-color="#f59e0b" stop-opacity=".8"/>
</linearGradient>

<!-- AMBIENT GLOWS -->
<radialGradient id="glowCyan"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".15"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="glowAmber"><stop offset="0%" stop-color="#f59e0b" stop-opacity=".12"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>

<!-- FILTERS -->
<filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
  <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000000" flood-opacity=".6"/>
</filter>

<!-- PATTERN -->
<pattern id="gridDots" width="32" height="32" patternUnits="userSpaceOnUse">
  <circle cx="16" cy="16" r=".8" fill="rgba(34,211,238,.12)"/>
</pattern>

<!-- CLIPS -->
<clipPath id="artClip"><rect x="670" y="44" width="560" height="600" rx="20"/></clipPath>
<clipPath id="cPrompt"><rect x="48" y="44" width="0" height="28"><animate attributeName="width" from="0" to="580" dur="0.9s" begin=".2s" fill="freeze"/></rect></clipPath>
<clipPath id="cRoles"><rect x="48" y="196" width="0" height="34"><animate attributeName="width" values="0;0;450;450;0;0" keyTimes="0;.02;.12;.24;.28;1" dur="20s" repeatCount="indefinite" begin="1.2s"/></rect></clipPath>
<clipPath id="cRoles2"><rect x="48" y="196" width="0" height="34"><animate attributeName="width" values="0;0;450;450;0;0" keyTimes="0;.30;.40;.52;.56;1" dur="20s" repeatCount="indefinite" begin="1.2s"/></rect></clipPath>
<clipPath id="cRoles3"><rect x="48" y="196" width="0" height="34"><animate attributeName="width" values="0;0;450;450;0;0" keyTimes="0;.58;.68;.80;.84;1" dur="20s" repeatCount="indefinite" begin="1.2s"/></rect></clipPath>
<clipPath id="cRoles4"><rect x="48" y="196" width="0" height="34"><animate attributeName="width" values="0;0;450;450;0;0" keyTimes="0;.86;.94;.99;.99;1" dur="20s" repeatCount="indefinite" begin="1.2s"/></rect></clipPath>
</defs>

<!-- ============ BACKGROUND ============ -->
<rect width="1280" height="720" rx="22" fill="url(#bgGrad)"/>
<rect width="1280" height="720" rx="22" fill="url(#gridDots)"/>
<rect x="1" y="1" width="1278" height="718" rx="22" fill="none" stroke="url(#borderGrad)" stroke-width="1.5"/>

<!-- Ambient orbs -->
<circle cx="200" cy="240" r="280" fill="url(#glowCyan)"/>
<circle cx="600" cy="500" r="220" fill="url(#glowAmber)"/>
<circle cx="1000" cy="300" r="320" fill="url(#glowCyan)"/>

<!-- ============ LEFT: CONTENT ============ -->

<!-- Terminal Prompt -->
<text clip-path="url(#cPrompt)" x="48" y="66" font-size="13.5">
  <tspan fill="#4ade80" font-weight="bold">bharath@ece-eng</tspan><tspan fill="#64748b">:~$ </tspan><tspan fill="#94a3b8">cat </tspan><tspan fill="#38bdf8">engineering_manifest.v</tspan>
</text>

<!-- Greeting -->
<text class="sans-t" x="48" y="112" font-size="22" font-weight="bold" fill="#94a3b8">Hi there, I'm <tspan fill="#f59e0b">👋</tspan></text>

<!-- Name -->
<text class="title-t" x="48" y="172" font-size="46" fill="url(#nameGrad)" filter="url(#glow)" letter-spacing="-0.5">
  Bharath G Devadiga
</text>

<!-- Dynamic Cycling Roles -->
<g>
  <text clip-path="url(#cRoles)" x="48" y="218" font-size="16.5" font-weight="bold" fill="#38bdf8">&lt; VLSI &amp; Physical Design Engineer /&gt;</text>
  <text clip-path="url(#cRoles2)" x="48" y="218" font-size="16.5" font-weight="bold" fill="#f59e0b">&lt; FPGA &amp; RTL Hardware Architect /&gt;</text>
  <text clip-path="url(#cRoles3)" x="48" y="218" font-size="16.5" font-weight="bold" fill="#4ade80">&lt; C++ &amp; Embedded Systems Developer /&gt;</text>
  <text clip-path="url(#cRoles4)" x="48" y="218" font-size="16.5" font-weight="bold" fill="#38bdf8">&lt; Android Native App Developer /&gt;</text>
</g>

<!-- Engineering Quote Card -->
<g style="animation: fadeIn .6s ease 0.8s forwards;">
  <rect x="48" y="246" width="580" height="68" rx="10" fill="#0d1829" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="48" y="246" width="4" height="68" rx="2" fill="#38bdf8"/>
  <text x="68" y="275" font-size="13.5" fill="#e2e8f0">
    "Hardware is my canvas, Logic is my superpower —
  </text>
  <text x="68" y="298" font-size="13.5" fill="#94a3b8">
    I don't just write software, <tspan fill="#38bdf8" font-weight="bold">I design the silicon that runs it.</tspan>"
  </text>
</g>

<!-- Tech Stack Pills -->
<text class="sans-t" x="48" y="348" font-size="14" font-weight="bold" fill="#f59e0b">⚙️ TECH ARSENAL &amp; TOOLS</text>

<g transform="translate(48, 362)">
  <!-- Row 1 -->
  <g class="pill"><rect x="0" y="0" width="82" height="26" rx="13" fill="rgba(56,189,248,.12)" stroke="#38bdf8" stroke-width="1"/><text x="41" y="17" text-anchor="middle" font-size="11.5" fill="#7dd3fc" font-weight="bold">Verilog</text></g>
  <g class="pill" transform="translate(90,0)"><rect x="0" y="0" width="70" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="35" y="17" text-anchor="middle" font-size="11.5" fill="#86efac" font-weight="bold">C / C++</text></g>
  <g class="pill" transform="translate(168,0)"><rect x="0" y="0" width="62" height="26" rx="13" fill="rgba(245,158,11,.12)" stroke="#f59e0b" stroke-width="1"/><text x="31" y="17" text-anchor="middle" font-size="11.5" fill="#fcd34d" font-weight="bold">Java</text></g>
  <g class="pill" transform="translate(238,0)"><rect x="0" y="0" width="74" height="26" rx="13" fill="rgba(129,140,248,.12)" stroke="#818cf8" stroke-width="1"/><text x="37" y="17" text-anchor="middle" font-size="11.5" fill="#a5b4fc" font-weight="bold">ESP32</text></g>
  <g class="pill" transform="translate(320,0)"><rect x="0" y="0" width="64" height="26" rx="13" fill="rgba(56,189,248,.12)" stroke="#38bdf8" stroke-width="1"/><text x="32" y="17" text-anchor="middle" font-size="11.5" fill="#7dd3fc" font-weight="bold">VLSI</text></g>
  <g class="pill" transform="translate(392,0)"><rect x="0" y="0" width="74" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="37" y="17" text-anchor="middle" font-size="11.5" fill="#86efac" font-weight="bold">Vivado</text></g>
  <g class="pill" transform="translate(474,0)"><rect x="0" y="0" width="86" height="26" rx="13" fill="rgba(245,158,11,.12)" stroke="#f59e0b" stroke-width="1"/><text x="43" y="17" text-anchor="middle" font-size="11.5" fill="#fcd34d" font-weight="bold">RTL-GDS</text></g>

  <!-- Row 2 -->
  <g class="pill" transform="translate(0, 34)"><rect x="0" y="0" width="58" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="29" y="17" text-anchor="middle" font-size="11.5" fill="#86efac" font-weight="bold">IoT</text></g>
  <g class="pill" transform="translate(66, 34)"><rect x="0" y="0" width="130" height="26" rx="13" fill="rgba(245,158,11,.12)" stroke="#f59e0b" stroke-width="1"/><text x="65" y="17" text-anchor="middle" font-size="11.5" fill="#fcd34d" font-weight="bold">Android Studio</text></g>
  <g class="pill" transform="translate(204, 34)"><rect x="0" y="0" width="68" height="26" rx="13" fill="rgba(129,140,248,.12)" stroke="#818cf8" stroke-width="1"/><text x="34" y="17" text-anchor="middle" font-size="11.5" fill="#a5b4fc" font-weight="bold">FPGA</text></g>
  <g class="pill" transform="translate(280, 34)"><rect x="0" y="0" width="70" height="26" rx="13" fill="rgba(56,189,248,.12)" stroke="#38bdf8" stroke-width="1"/><text x="35" y="17" text-anchor="middle" font-size="11.5" fill="#7dd3fc" font-weight="bold">Linux</text></g>
  <g class="pill" transform="translate(358, 34)"><rect x="0" y="0" width="76" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="38" y="17" text-anchor="middle" font-size="11.5" fill="#86efac" font-weight="bold">Python</text></g>
  <g class="pill" transform="translate(442, 34)"><rect x="0" y="0" width="68" height="26" rx="13" fill="rgba(56,189,248,.12)" stroke="#38bdf8" stroke-width="1"/><text x="34" y="17" text-anchor="middle" font-size="11.5" fill="#7dd3fc" font-weight="bold">Git</text></g>
</g>

<!-- Core Engineering Focus -->
<text class="sans-t" x="48" y="456" font-size="14" font-weight="bold" fill="#38bdf8">💡 CORE ENGINEERING FOCUS</text>
<g font-size="12.5" transform="translate(48, 474)">
  <text y="0"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cbd5e1">Bridging digital hardware design with intelligent software stacks.</tspan></text>
  <text y="22"><tspan fill="#f59e0b">⚡ </tspan><tspan fill="#cbd5e1">Synthesizing RTL architectures &amp; ASIC physical VLSI flows.</tspan></text>
  <text y="44"><tspan fill="#38bdf8">🚀 </tspan><tspan fill="#cbd5e1">Crafting custom hardware integrations, IoT nodes &amp; mobile apps.</tspan></text>
</g>

<!-- Live Stats Ribbon -->
<g transform="translate(48, 552)">
  <rect width="580" height="66" rx="12" fill="#0d1829" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="145" y1="12" x2="145" y2="54" stroke="#1e293b" stroke-width="1"/>
  <line x1="290" y1="12" x2="290" y2="54" stroke="#1e293b" stroke-width="1"/>
  <line x1="435" y1="12" x2="435" y2="54" stroke="#1e293b" stroke-width="1"/>

  <!-- Col 1 -->
  <text x="72" y="26" text-anchor="middle" font-size="11" fill="#64748b">📦 Repositories</text>
  <text class="title-t" x="72" y="52" text-anchor="middle" font-size="19" fill="#38bdf8">10+</text>

  <!-- Col 2 -->
  <text x="217" y="26" text-anchor="middle" font-size="11" fill="#64748b">💻 Total Commits</text>
  <text class="title-t" x="217" y="52" text-anchor="middle" font-size="19" fill="#f59e0b">500+</text>

  <!-- Col 3 -->
  <text x="362" y="26" text-anchor="middle" font-size="11" fill="#64748b">⭐ Stars Earned</text>
  <text class="title-t" x="362" y="52" text-anchor="middle" font-size="19" fill="#4ade80">50+</text>

  <!-- Col 4 -->
  <text x="507" y="26" text-anchor="middle" font-size="11" fill="#64748b">👥 Followers</text>
  <text class="title-t" x="507" y="52" text-anchor="middle" font-size="19" fill="#818cf8">25+</text>
</g>

<!-- ============ RIGHT: FRAMED ARTWORK & CODE WINDOW ============ -->

<!-- Artwork Card -->
<g class="fl-art" filter="url(#cardShadow)">
  <!-- Glow Frame -->
  <rect x="668" y="42" width="564" height="604" rx="22" fill="none" stroke="url(#artBorder)" stroke-width="2"/>
  
  <!-- Image -->
  <g clip-path="url(#artClip)">
    <image x="670" y="44" width="560" height="600" preserveAspectRatio="xMidYMid slice" href="__IMG__"/>
    
    <!-- Subtle dark vignette over top & bottom for overlay clarity -->
    <rect x="670" y="44" width="560" height="120" fill="url(#bgGrad)" opacity=".3"/>
    <rect x="670" y="524" width="560" height="120" fill="url(#bgGrad)" opacity=".6"/>
  </g>

  <!-- Floating Glassmorphic Badge on Artwork: DESIGN IT / BUILD IT -->
  <g transform="translate(980, 64)">
    <rect width="230" height="64" rx="14" fill="#0c1626" fill-opacity=".85" stroke="#38bdf8" stroke-width="1.2" filter="url(#glow)"/>
    <text class="sans-t np" x="115" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#38bdf8" letter-spacing="2.5">⚡ SILICON &amp; CODE</text>
    <text class="title-t" x="115" y="49" text-anchor="middle" font-size="14" fill="#f59e0b" letter-spacing="2">DESIGN • BUILD</text>
  </g>

  <!-- Bottom Artwork Caption -->
  <g transform="translate(690, 600)">
    <rect width="260" height="32" rx="16" fill="#080e1a" fill-opacity=".8" stroke="#1e293b" stroke-width="1"/>
    <text x="130" y="21" text-anchor="middle" font-size="11.5" fill="#e2e8f0">🏴‍☠️ Set Sail on the Grand Line of Tech</text>
  </g>
</g>

<!-- ============ FOOTER ============ -->
<line x1="48" y1="662" x2="1232" y2="662" stroke="#1e293b" stroke-width="1"/>

<g transform="translate(48, 680)" font-size="12" fill="#94a3b8">
  <!-- GitHub -->
  <g transform="translate(0, -2) scale(.75)">
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#94a3b8"/>
  </g>
  <text x="24" y="12">BharathGDevadiga</text>

  <!-- Email -->
  <g transform="translate(180, -2) scale(.75)">
    <rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <path d="M2.5 5.5 12 13l9.5-7.5" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="204" y="12">bharathgdudupi@gmail.com</text>

  <!-- Status -->
  <g transform="translate(420, 0)">
    <circle cx="6" cy="9" r="4" fill="#4ade80"/>
    <text x="18" y="12" fill="#cbd5e1">Open to collaborative hardware &amp; software projects</text>
  </g>
</g>

</svg>"""

DARK_BANNER = DARK_BANNER.replace("__IMG__", img_b64)

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(DARK_BANNER)

# =========================================================================
# 2. POLISHED LIGHT BANNER
# =========================================================================
LIGHT_BANNER = DARK_BANNER

# Backgrounds
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#080e1a"', 'stop-color="#f8fafc"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#0c1626"', 'stop-color="#ffffff"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#060b14"', 'stop-color="#f1f5f9"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(34,211,238,.12)"', 'fill="rgba(2,132,199,.10)"')

# Borders & Cards
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#22d3ee" stop-opacity=".6"', 'stop-color="#0284c7" stop-opacity=".5"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#0284c7" stop-opacity=".6"', 'stop-color="#0369a1" stop-opacity=".5"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#0d1829"', 'fill="#ffffff"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#1e293b"', 'stroke="#e2e8f0"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#0c1626"', 'fill="#ffffff"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#080e1a"', 'fill="#ffffff"')

# Text Colors
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#e2e8f0"', 'fill="#0f172a"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#cbd5e1"', 'fill="#334155"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#94a3b8"', 'fill="#64748b"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#64748b"', 'fill="#475569"')

# Accent Replacements
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#38bdf8"', 'stop-color="#0284c7"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#22d3ee"', 'stop-color="#0369a1"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#f59e0b"', 'stop-color="#d97706"')

LIGHT_BANNER = LIGHT_BANNER.replace('fill="#38bdf8"', 'fill="#0284c7"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#22d3ee"', 'fill="#0284c7"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#f59e0b"', 'fill="#d97706"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#fcd34d"', 'fill="#b45309"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#4ade80"', 'fill="#16a34a"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#86efac"', 'fill="#15803d"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#818cf8"', 'fill="#4f46e5"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#a5b4fc"', 'fill="#4338ca"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#7dd3fc"', 'fill="#0369a1"')

LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#38bdf8"', 'stroke="#0284c7"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#22d3ee"', 'stroke="#0284c7"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#f59e0b"', 'stroke="#d97706"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#4ade80"', 'stroke="#16a34a"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#818cf8"', 'stroke="#4f46e5"')

# Pill Backgrounds for Light Mode
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(56,189,248,.12)"', 'fill="rgba(2,132,199,.12)"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(74,222,128,.12)"', 'fill="rgba(22,163,74,.12)"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(245,158,11,.12)"', 'fill="rgba(217,119,6,.12)"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(129,140,248,.12)"', 'fill="rgba(79,70,229,.12)"')

with open("bharath-banner-light.svg", "w", encoding="utf-8") as f:
    f.write(LIGHT_BANNER)

print("Generated cohesive, framed dark and light banners!")
