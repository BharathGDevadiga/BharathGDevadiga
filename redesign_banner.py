import re

with open("bharath-banner.svg", "r", encoding="utf-8") as f:
    current = f.read()

match = re.search(r'href="(data:image/[^"]+)"', current)
img = match.group(1) if match else ""
print(f"Image: {'found (' + img[:50] + '...)' if img else 'NOT FOUND!'}")

NEW_BANNER = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Bharath G Devadiga - ECE Engineer &amp; Builder">
<title>Bharath G Devadiga &#8212; ECE Engineer</title>
<defs>
<style type="text/css"><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
.name-t{font-family:'Arial','Helvetica',sans-serif}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@keyframes floaty2{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-10px) rotate(5deg)}}
@keyframes heartBeat{0%,100%{transform:scale(1)}12%{transform:scale(1.25)}24%{transform:scale(1)}36%{transform:scale(1.18)}48%{transform:scale(1)}}
@keyframes neonFlicker{0%{opacity:0}5%{opacity:.7}7%{opacity:.1}10%{opacity:.9}12%{opacity:.3}16%,100%{opacity:1}}
@keyframes neonPulse{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes twinkle{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:1;transform:scale(1)}}
@keyframes rise{0%{transform:translateY(0);opacity:0}12%{opacity:.55}88%{opacity:.55}100%{transform:translateY(-46px);opacity:0}}
.pill{opacity:0;transition:transform .2s ease,filter .2s ease;transform-box:fill-box;transform-origin:center;cursor:pointer}
.pill:hover{transform:scale(1.08);filter:brightness(1.35)}
.cur{animation:blink 1s step-end infinite}
.tw{transform-box:fill-box;transform-origin:center;animation:twinkle 2.6s ease-in-out infinite}
.hb{transform-box:fill-box;transform-origin:center;animation:heartBeat 2.2s ease-in-out infinite}
.fl{animation:floaty 5s ease-in-out infinite}
.fl2{transform-box:fill-box;transform-origin:center;animation:floaty2 4.2s ease-in-out infinite}
.neon-on{animation:neonFlicker 2.4s ease 3.2s backwards}
.np{animation:neonPulse 2.6s ease-in-out infinite}
.rp{animation:rise linear infinite}
.sep{stroke:#1e2a3a;stroke-width:1;opacity:.7}
.ii,.pill,.soc,.st,.cl{opacity:0}
]]></style>

<!-- BACKGROUND: Dark navy (vs Megha's dark purple #120b20) -->
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#090e1b"/>
  <stop offset="55%" stop-color="#0c1222"/>
  <stop offset="100%" stop-color="#070b16"/>
</linearGradient>

<!-- NAME GRADIENT: Cyan-amber-green animation (vs Megha's pink-purple) -->
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#0ea5e9;#22d3ee" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="50%"><animate attributeName="stop-color" values="#f59e0b;#22d3ee;#38bdf8;#f59e0b" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#4ade80;#f59e0b;#22d3ee;#4ade80" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>

<!-- BORDER: Cyan/amber (vs Megha's pink/purple) -->
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#f59e0b" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#06b6d4" stop-opacity=".4"/>
</linearGradient>

<!-- IMAGE GLOW: Cyan (vs Megha's purple #c084fc) -->
<radialGradient id="imgGlow"><stop offset="0%" stop-color="#06b6d4" stop-opacity=".18"/><stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/></radialGradient>

<!-- ORB GRADIENTS: Cyan/amber/green palette -->
<radialGradient id="orbC"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".09"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="orbA"><stop offset="0%" stop-color="#f59e0b" stop-opacity=".10"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>
<radialGradient id="orbG"><stop offset="0%" stop-color="#4ade80" stop-opacity=".07"/><stop offset="100%" stop-color="#4ade80" stop-opacity="0"/></radialGradient>

<!-- FILTERS -->
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowC"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>

<!-- DOTS: Slightly larger spacing 36px (vs Megha's 30px) with cyan tint -->
<pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse">
  <circle cx="18" cy="18" r=".7" fill="rgba(34,211,238,.07)"/>
</pattern>

<!-- TEXT CLIP PATHS -->
<clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="520" dur="1s" begin=".3s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="200" dur=".5s" begin="1.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="400" dur=".7s" begin="3.4s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="400" dur=".6s" begin="4.2s" fill="freeze"/></rect></clipPath>

<!-- CYCLING ROLE CLIPS -->
<clipPath id="r1"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>

<!-- IMAGE REVEAL: HORIZONTAL left-to-right (vs Megha's vertical top-to-bottom) -->
<clipPath id="imgReveal"><rect x="722" y="152" width="0" height="522">
  <animate attributeName="width" from="0" to="558" dur="1.8s" begin=".5s" fill="freeze"/>
</rect></clipPath>
<clipPath id="imgBox"><rect x="722" y="152" width="558" height="522"/></clipPath>

<!-- SCAN GRADIENTS: Vertical bar that moves horizontally (different from Megha's horizontal bar moving vertically) -->
<linearGradient id="scanLineV" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
  <stop offset="18%" stop-color="#22d3ee"/>
  <stop offset="50%" stop-color="#38bdf8"/>
  <stop offset="82%" stop-color="#22d3ee"/>
  <stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>
</linearGradient>
<linearGradient id="scanTrailH" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
  <stop offset="100%" stop-color="#22d3ee" stop-opacity=".16"/>
</linearGradient>

<!-- FULL-BANNER SCANNER: Vertical line, horizontal movement (vs Megha's horizontal line, vertical movement) -->
<linearGradient id="fullScanV" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/>
  <stop offset="50%" stop-color="#22d3ee" stop-opacity=".55"/>
  <stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/>
</linearGradient>

<clipPath id="bannerBox"><rect x="1" y="1" width="1278" height="738" rx="22"/></clipPath>
</defs>

<!-- ============ BACKGROUND ============ -->
<rect width="1280" height="740" rx="22" fill="url(#bg)"/>
<rect width="1280" height="740" rx="22" fill="url(#dots)"/>

<!-- ORBS: Different positions (150,300), (1050,430), (620,90) vs Megha's (230,220), (1000,520), (700,120) -->
<circle cx="150" cy="300" r="280" fill="url(#orbC)"><animate attributeName="r" values="280;310;280" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1050" cy="430" r="260" fill="url(#orbA)"><animate attributeName="r" values="260;290;260" dur="7.5s" repeatCount="indefinite"/></circle>
<circle cx="620" cy="90" r="180" fill="url(#orbG)"><animate attributeName="r" values="180;200;180" dur="5s" repeatCount="indefinite"/></circle>

<!-- BORDER -->
<rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- CIRCUIT CORNER DECORATIONS: Unique to this design, absent in Megha's -->
<g stroke="#22d3ee" stroke-width="1.5" opacity=".45" fill="none">
  <polyline points="22,1 1,22"/>
  <polyline points="1258,1 1279,22"/>
  <polyline points="1,718 22,739"/>
  <polyline points="1279,718 1258,739"/>
</g>
<g fill="#22d3ee" opacity=".45">
  <circle cx="22" cy="2" r="3"/>
  <circle cx="1258" cy="2" r="3"/>
  <circle cx="22" cy="738" r="3"/>
  <circle cx="1258" cy="738" r="3"/>
</g>
<!-- Circuit trace lines from corners -->
<g stroke="#22d3ee" stroke-width="1" opacity=".25" fill="none">
  <line x1="24" y1="2" x2="60" y2="2"/>
  <line x1="2" y1="24" x2="2" y2="60"/>
  <line x1="1220" y1="2" x2="1256" y2="2"/>
  <line x1="1278" y1="24" x2="1278" y2="60"/>
  <line x1="24" y1="738" x2="60" y2="738"/>
  <line x1="2" y1="680" x2="2" y2="716"/>
  <line x1="1220" y1="738" x2="1256" y2="738"/>
  <line x1="1278" y1="680" x2="1278" y2="716"/>
</g>

<!-- RISING PARTICLES: Cyan/amber/green palette (vs Megha's pink/purple) -->
<circle class="rp" cx="120" cy="640" r="1.4" fill="#22d3ee" style="animation-duration:5s"/>
<circle class="rp" cx="380" cy="710" r="1.1" fill="#f59e0b" style="animation-duration:6.2s;animation-delay:1s"/>
<circle class="rp" cx="600" cy="670" r="1.3" fill="#4ade80" style="animation-duration:4.8s;animation-delay:2s"/>
<circle class="rp" cx="1160" cy="700" r="1.2" fill="#22d3ee" style="animation-duration:5.5s;animation-delay:.6s"/>
<circle class="rp" cx="1220" cy="380" r="1" fill="#f59e0b" style="animation-duration:6.4s;animation-delay:1.6s"/>
<circle class="rp" cx="60" cy="430" r="1" fill="#06b6d4" style="animation-duration:5.8s;animation-delay:2.4s"/>

<!-- CIRCUIT SPARKLES: Plus/cross shapes (vs Megha's star/diamond shapes) -->
<g class="tw" style="animation-delay:.4s"><path d="M468 103h-6v-6h-8v6h-6v8h6v6h8v-6h6z" fill="none" stroke="#22d3ee" stroke-width="1.5"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M882 110h-5v-5h-6v5h-5v6h5v5h6v-5h5z" fill="none" stroke="#f59e0b" stroke-width="1.5"/></g>
<g class="tw" style="animation-delay:2.6s"><path d="M1245 250h-5v-5h-6v5h-5v6h5v5h6v-5h5z" fill="none" stroke="#22d3ee" stroke-width="1.5"/></g>

<!-- ============ LEFT: CONTENT ============ -->

<!-- TERMINAL PROMPT: .v extension for Verilog (vs Megha's .md) -->
<text clip-path="url(#cPrompt)" x="48" y="69" font-size="14">
  <tspan fill="#4ade80" font-weight="bold">bharath@ece-eng</tspan><tspan fill="#8b949e">:~$ </tspan><tspan fill="#e6edf3">cat </tspan><tspan fill="#22d3ee">profile.v</tspan>
</text>
<rect x="500" y="56" width="8" height="16" fill="#4ade80" opacity="0">
  <animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" begin="1.35s"/>
</rect>

<!-- HI I'M -->
<text clip-path="url(#cHi)" x="48" y="114" font-size="24" font-weight="bold" fill="#e6edf3">Hi, I'm &#128075;</text>

<!-- NAME: Simple glowing gradient text (vs Megha's complex Pacifico path outlines) -->
<text class="name-t" x="48" y="190" font-size="52" font-weight="bold" font-style="italic" fill="url(#nameg)" filter="url(#glowC)" letter-spacing="1.5" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".7s" begin="1.4s" fill="freeze"/>
  Bharath G Devadiga
</text>

<!-- HEARTBEAT: Cyan color (vs Megha's pink) -->
<g class="hb" style="animation-delay:3s">
  <path d="M598 167 c-5-11-21-9-21 4 0 9 12 16 21 22 9-6 21-13 21-22 0-13-16-15-21-4z" fill="#22d3ee" opacity=".9"/>
</g>

<!-- CYCLING ROLES: ECE-focused content (vs Megha's frontend web roles) -->
<text clip-path="url(#r1)" x="48" y="241" font-size="17" fill="#22d3ee" filter="url(#glow)">&lt; VLSI &amp; Physical Design /&gt;</text>
<text clip-path="url(#r2)" x="48" y="241" font-size="17" fill="#22d3ee" filter="url(#glow)">&lt; FPGA &amp; RTL Engineering /&gt;</text>
<text clip-path="url(#r3)" x="48" y="241" font-size="17" fill="#22d3ee" filter="url(#glow)">&lt; C++ &amp; Embedded Systems /&gt;</text>
<text clip-path="url(#r4)" x="48" y="241" font-size="17" fill="#22d3ee" filter="url(#glow)">&lt; Android App Developer /&gt;</text>
<rect x="48" y="228" width="2.5" height="16" fill="#22d3ee" opacity="0">
  <animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="2.9s"/>
</rect>

<!-- QUOTE BOX: Cyan left accent (vs Megha's pink) -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="262" width="430" height="72" rx="8" fill="#0d1e30" stroke="#1a3a5c" stroke-width="1"/>
  <rect x="48" y="266" width="3.5" height="64" rx="1.5" fill="#22d3ee"/>
</g>
<text clip-path="url(#q1)" x="76" y="292" font-size="15" fill="#e6edf3">I don't just write code,</text>
<text clip-path="url(#q2)" x="76" y="318" font-size="15"><tspan fill="#e6edf3">I </tspan><tspan fill="#22d3ee" font-weight="bold">design</tspan><tspan fill="#e6edf3"> the silicon that runs it.</tspan></text>
<g class="tw" style="animation-delay:.9s"><path d="M457 285h-4v-4h-5v4h-4v5h4v4h5v-4h4z" fill="none" stroke="#22d3ee" stroke-width="1" opacity=".6"/></g>

<!-- TECH SECTION: Amber heading (vs Megha's purple) -->
<text class="ii" x="48" y="374" font-size="15" fill="#f59e0b" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">&#9881;&#65039; Tech Stack</text>

<!-- PILLS ROW 1: ECE tools, cyan/green/amber/indigo colors -->
<g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="388" width="82" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="89" y="405" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">Verilog</text></g>
<g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="138" y="388" width="64" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="170" y="405" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">C++</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="210" y="388" width="64" height="26" rx="13" fill="rgba(245,158,11,.10)" stroke="#f59e0b" stroke-width="1"/><text x="242" y="405" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">Java</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="282" y="388" width="72" height="26" rx="13" fill="rgba(129,140,248,.12)" stroke="#818cf8" stroke-width="1"/><text x="318" y="405" text-anchor="middle" font-size="12" fill="#a5b4fc" font-weight="bold">ESP32</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="362" y="388" width="64" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="394" y="405" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">VLSI</text></g>

<!-- PILLS ROW 2 -->
<g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="48" y="422" width="56" height="26" rx="13" fill="rgba(74,222,128,.10)" stroke="#4ade80" stroke-width="1"/><text x="76" y="439" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">IoT</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="112" y="422" width="135" height="26" rx="13" fill="rgba(245,158,11,.10)" stroke="#f59e0b" stroke-width="1"/><text x="179" y="439" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">Android Studio</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="255" y="422" width="72" height="26" rx="13" fill="rgba(129,140,248,.10)" stroke="#818cf8" stroke-width="1"/><text x="291" y="439" text-anchor="middle" font-size="12" fill="#a5b4fc" font-weight="bold">FPGA</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.6s forwards"><rect x="335" y="422" width="80" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="375" y="439" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">Linux</text></g>

<!-- ABOUT ME: Cyan heading -->
<text class="ii" x="48" y="490" font-size="15" fill="#22d3ee" font-weight="bold" style="animation:fadeIn .4s ease 5.7s forwards">&#128161; About Me</text>
<text class="ii" x="48" y="516" font-size="13.5" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">I bridge the gap between hardware and software systems.</tspan></text>
<text class="ii" x="48" y="540" font-size="13.5" style="animation:fadeIn .4s ease 6.1s forwards"><tspan fill="#f59e0b">&#9889; </tspan><tspan fill="#cdd3dd">Building the future, one circuit at a time.</tspan></text>
<text class="ii" x="48" y="564" font-size="13.5" style="animation:fadeIn .4s ease 6.3s forwards"><tspan fill="#22d3ee">&#128640; </tspan><tspan fill="#cdd3dd">I design the hardware logic that runs the software.</tspan></text>

<!-- STATS CARD: Darker navy bg (vs Megha's dark purple) -->
<g class="st" style="animation:fadeIn .5s ease 6.4s forwards">
  <rect x="48" y="586" width="560" height="66" rx="12" fill="#0d1e30" stroke="#1a3a5c" stroke-width="1"/>
  <line x1="188" y1="598" x2="188" y2="640" class="sep"/>
  <line x1="328" y1="598" x2="328" y2="640" class="sep"/>
  <line x1="468" y1="598" x2="468" y2="640" class="sep"/>
  <text x="118" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#128230; Repos</text>
  <text x="258" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#128187; Commits</text>
  <text x="398" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#11088; Stars</text>
  <text x="538" y="612" text-anchor="middle" font-size="11.5" fill="#9aa4b2">&#128101; Followers</text>
</g>
<!-- STATS VALUES: Bharath's stats in cyan/amber/green/indigo -->
<text class="st" x="118" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#22d3ee" filter="url(#glow)" style="animation:fadeIn .4s ease 6.6s forwards">12+</text>
<text class="st" x="258" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#f59e0b" filter="url(#glow)" style="animation:fadeIn .4s ease 6.75s forwards">300+</text>
<text class="st" x="398" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#4ade80" filter="url(#glow)" style="animation:fadeIn .4s ease 6.9s forwards">40+</text>
<text class="st" x="538" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#818cf8" filter="url(#glow)" style="animation:fadeIn .4s ease 7.05s forwards">15+</text>

<!-- ============ RIGHT: IMAGE ============ -->
<!-- AMBIENT GLOW: Cyan (vs Megha's purple) -->
<circle cx="1000" cy="440" r="270" fill="url(#imgGlow)"><animate attributeName="r" values="270;292;270" dur="5s" repeatCount="indefinite"/></circle>
<g class="fl">
  <g clip-path="url(#imgReveal)">
    <image x="722" y="152" width="558" height="522" preserveAspectRatio="xMidYMid slice" href="__IMG__"/>
  </g>
  <g clip-path="url(#imgBox)">
    <!-- SCAN LINE: Vertical bar moving left-to-right (vs Megha's horizontal bar top-to-bottom) -->
    <rect x="720" y="152" width="4" height="522" fill="url(#scanLineV)" filter="url(#glow)" opacity="0">
      <animate attributeName="opacity" values="0;.95;.95;0" keyTimes="0;.04;.9;1" dur="2s" begin=".5s" fill="freeze"/>
      <animate attributeName="x" from="720" to="1278" dur="1.8s" begin=".5s" fill="freeze"/>
    </rect>
  </g>
</g>

<!-- ============ VERILOG CODE CARD (after image so it renders on top) ============ -->
<!-- Positioned at x=516 (vs Megha's x=552) with Verilog content (vs JSX) -->
<g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
  <rect x="516" y="40" width="332" height="240" rx="12" fill="#07111e" fill-opacity=".97" stroke="#1a3a5c" stroke-width="1.2"/>
  <rect x="516" y="40" width="332" height="28" rx="12" fill="#0f1e30"/>
  <rect x="516" y="56" width="332" height="12" fill="#0f1e30"/>
  <circle cx="536" cy="54" r="4.5" fill="#ff5f57"/>
  <circle cx="552" cy="54" r="4.5" fill="#febc2e"/>
  <circle cx="568" cy="54" r="4.5" fill="#28c840"/>
  <text x="682" y="58" text-anchor="middle" font-size="11" fill="#8b949e">ece_module.v</text>
</g>
<g font-size="12.5">
  <text class="cl" x="534" y="88" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#818cf8">module </tspan><tspan fill="#22d3ee">bharath</tspan><tspan fill="#e6edf3"> #(</tspan></text>
  <text class="cl" x="552" y="107" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#f59e0b">parameter </tspan><tspan fill="#4ade80">SKILLS</tspan><tspan fill="#e6edf3"> = 8</tspan></text>
  <text class="cl" x="534" y="126" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#e6edf3">) (</tspan></text>
  <text class="cl" x="552" y="145" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#818cf8">output </tspan><tspan fill="#22d3ee">solutions</tspan><tspan fill="#e6edf3">,</tspan></text>
  <text class="cl" x="552" y="164" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#818cf8">input  </tspan><tspan fill="#f59e0b">problems</tspan></text>
  <text class="cl" x="534" y="183" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#e6edf3">);</tspan></text>
  <text class="cl" x="552" y="202" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#8b949e">// always solving</tspan></text>
  <text class="cl" x="552" y="221" style="animation:fadeIn .3s ease 3.65s forwards"><tspan fill="#818cf8">always </tspan><tspan fill="#e6edf3">@(*) begin</tspan></text>
  <text class="cl" x="534" y="240" style="animation:fadeIn .3s ease 3.85s forwards"><tspan fill="#22d3ee">endmodule</tspan><tspan fill="#8b949e"> // bharath</tspan></text>
  <text class="cl" x="534" y="258" style="animation:fadeIn .3s ease 4.0s forwards"><tspan fill="#8b949e">// ECE grad &amp; builder</tspan></text>
</g>

<!-- NEON SIGN: Amber/cyan, "DESIGN IT / BUILD IT" (vs Megha's pink, "KEEP CODING / KEEP GROWING") -->
<g class="neon-on">
  <rect x="1010" y="42" width="242" height="128" rx="14" fill="none" stroke="#f59e0b" stroke-width="1.5" opacity=".5" filter="url(#glow)"/>
  <text class="np" x="1131" y="90" text-anchor="middle" font-size="32" font-weight="bold" fill="#22d3ee" filter="url(#glowBig)" style="animation-delay:.2s">&#9651;</text>
  <text class="np" x="1131" y="120" text-anchor="middle" font-size="19" font-weight="bold" fill="#f59e0b" filter="url(#glow)" letter-spacing="3">DESIGN IT</text>
  <text class="np" x="1131" y="148" text-anchor="middle" font-size="19" font-weight="bold" fill="#22d3ee" filter="url(#glow)" letter-spacing="2.5" style="animation-delay:1.3s">BUILD IT</text>
</g>

<!-- PIXEL GEAR: Different from Megha's pixel heart -->
<g class="fl2" style="animation-delay:.7s">
  <g transform="translate(600,300)" opacity="0">
    <animate attributeName="opacity" from="0" to=".9" dur=".6s" begin="4.4s" fill="freeze"/>
    <g fill="#f59e0b">
      <rect x="8" y="0" width="8" height="5"/>
      <rect x="20" y="0" width="8" height="5"/>
      <rect x="0" y="8" width="36" height="20"/>
      <rect x="8" y="28" width="8" height="5"/>
      <rect x="20" y="28" width="8" height="5"/>
      <rect x="12" y="11" width="12" height="14" fill="#090e1b"/>
    </g>
  </g>
</g>

<!-- HEARTBEAT: Amber (vs Megha's pink) -->
<g class="hb" style="animation-delay:1.4s">
  <path d="M1234 320 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#f59e0b" opacity=".85" filter="url(#glow)"/>
</g>

<!-- ============ FOOTER ============ -->
<line x1="48" y1="676" x2="1232" y2="676" stroke="#1e2a3a" stroke-width="1" opacity=".7" stroke-dasharray="1184" stroke-dashoffset="1184">
  <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.2s" fill="freeze"/>
</line>
<!-- SOCIAL LINKS: Bharath's accounts, cyan/amber icons -->
<g class="soc" style="animation:fadeIn .5s ease 7.4s forwards">
  <g transform="translate(48,692) scale(.8)">
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#c9d1d9"/>
  </g>
  <text x="74" y="707" font-size="12.5" fill="#c9d1d9">BharathGDevadiga</text>
  <g transform="translate(226,693) scale(.8)">
    <rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#22d3ee" stroke-width="2"/>
    <path d="M2.5 5.5 12 13l9.5-7.5" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="252" y="707" font-size="12.5" fill="#c9d1d9">bharathgdevadiga@gmail.com</text>
  <!-- LinkedIn icon (vs Megha's Instagram) -->
  <g transform="translate(470,692) scale(.8)">
    <rect width="24" height="24" rx="4" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="7" cy="8" r="1.5" fill="#f59e0b"/>
    <line x1="7" y1="11" x2="7" y2="18" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    <path d="M11 13a3 3 0 016 0v5" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    <line x1="11" y1="11" x2="11" y2="18" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
  </g>
  <text x="496" y="707" font-size="12.5" fill="#c9d1d9">bharath-g-devadiga</text>
</g>
<!-- FOOTER TAGLINE: Different from Megha's -->
<text class="soc" x="1232" y="707" text-anchor="end" font-size="13" style="animation:fadeIn .5s ease 7.6s forwards">
  <tspan fill="#8b949e">"</tspan><tspan fill="#22d3ee">Hardware is my canvas, Logic is my superpower.</tspan><tspan fill="#8b949e">" </tspan><tspan fill="#f59e0b">&#9889;</tspan>
</text>
<text class="soc" x="700" y="707" font-size="11.5" style="animation:fadeIn .5s ease 7.5s forwards">
  <tspan fill="#4ade80">&#9679;</tspan><tspan fill="#8b949e"> open to collaborate</tspan>
</text>

<!-- FULL-BANNER SCANNER: Vertical line moving LEFT-TO-RIGHT (vs Megha's horizontal line top-to-bottom) -->
<g clip-path="url(#bannerBox)" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="-60,0;1340,0" dur="3.5s" begin="3s" repeatCount="indefinite"/>
    <rect x="-34" y="0" width="34" height="740" fill="url(#scanTrailH)"/>
    <rect x="0" y="0" width="2.6" height="740" fill="url(#fullScanV)" opacity=".6" filter="url(#glow)"/>
  </g>
</g>
</svg>"""

NEW_BANNER = NEW_BANNER.replace("__IMG__", img)

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(NEW_BANNER)

print("New banner written successfully!")
