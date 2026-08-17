import re
import os

with open("bharath-banner.svg", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'href="(data:image/[^"]+)"', content)
if not m:
    # Check if one_piece_banner.jpg or avatar exists
    import base64
    if os.path.exists("one_piece_small.jpg"):
        with open("one_piece_small.jpg", "rb") as img_f:
            img_b64 = "data:image/jpeg;base64," + base64.b64encode(img_f.read()).decode('utf-8')
    elif os.path.exists("avatar.jpg"):
        with open("avatar.jpg", "rb") as img_f:
            img_b64 = "data:image/jpeg;base64," + base64.b64encode(img_f.read()).decode('utf-8')
    else:
        img_b64 = ""
else:
    img_b64 = m.group(1)

print(f"Loaded image b64 (length: {len(img_b64)})")

# =========================================================================
# 1. DARK BANNER GENERATION
# =========================================================================
DARK_BANNER = """<?xml version="1.0" encoding="UTF-8"?>
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
@keyframes neonPulse{0%,100%{opacity:.6}50%{opacity:1}}
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

<!-- BACKGROUND -->
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#090e1b"/>
  <stop offset="55%" stop-color="#0c1222"/>
  <stop offset="100%" stop-color="#070b16"/>
</linearGradient>

<!-- NAME GRADIENT -->
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#0ea5e9;#22d3ee" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="50%"><animate attributeName="stop-color" values="#f59e0b;#22d3ee;#38bdf8;#f59e0b" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#4ade80;#f59e0b;#22d3ee;#4ade80" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>

<!-- BORDER -->
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".4"/>
  <stop offset="50%" stop-color="#f59e0b" stop-opacity=".2"/>
  <stop offset="100%" stop-color="#06b6d4" stop-opacity=".4"/>
</linearGradient>

<!-- IMAGE GLOW -->
<radialGradient id="imgGlow"><stop offset="0%" stop-color="#06b6d4" stop-opacity=".22"/><stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/></radialGradient>

<!-- ORB GRADIENTS -->
<radialGradient id="orbC"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".10"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="orbA"><stop offset="0%" stop-color="#f59e0b" stop-opacity=".10"/><stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/></radialGradient>
<radialGradient id="orbG"><stop offset="0%" stop-color="#4ade80" stop-opacity=".08"/><stop offset="100%" stop-color="#4ade80" stop-opacity="0"/></radialGradient>

<!-- FILTERS -->
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowC"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>

<!-- DOTS -->
<pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse">
  <circle cx="18" cy="18" r=".7" fill="rgba(34,211,238,.08)"/>
</pattern>

<!-- TEXT CLIP PATHS -->
<clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="520" dur="1s" begin=".3s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="200" dur=".5s" begin="1.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="420" dur=".7s" begin="3.4s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="420" dur=".6s" begin="4.2s" fill="freeze"/></rect></clipPath>

<!-- CYCLING ROLE CLIPS -->
<clipPath id="r1"><rect x="48" y="210" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.01;.07;.2;.24;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="210" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.26;.32;.45;.49;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="210" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.51;.57;.7;.74;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="210" width="0" height="36"><animate attributeName="width" values="0;0;380;380;0;0" keyTimes="0;.76;.82;.95;.99;1" dur="24s" repeatCount="indefinite" begin="2.9s"/></rect></clipPath>

<!-- IMAGE REVEAL -->
<clipPath id="imgReveal"><rect x="740" y="152" width="0" height="522">
  <animate attributeName="width" from="0" to="540" dur="1.8s" begin=".5s" fill="freeze"/>
</rect></clipPath>
<clipPath id="imgBox"><rect x="740" y="152" width="540" height="522"/></clipPath>

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

<circle cx="150" cy="300" r="280" fill="url(#orbC)"><animate attributeName="r" values="280;310;280" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1050" cy="430" r="260" fill="url(#orbA)"><animate attributeName="r" values="260;290;260" dur="7.5s" repeatCount="indefinite"/></circle>
<circle cx="620" cy="90" r="180" fill="url(#orbG)"><animate attributeName="r" values="180;200;180" dur="5s" repeatCount="indefinite"/></circle>

<rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- Circuit corner decorations -->
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

<!-- RISING PARTICLES -->
<circle class="rp" cx="120" cy="640" r="1.4" fill="#22d3ee" style="animation-duration:5s"/>
<circle class="rp" cx="380" cy="710" r="1.1" fill="#f59e0b" style="animation-duration:6.2s;animation-delay:1s"/>
<circle class="rp" cx="600" cy="670" r="1.3" fill="#4ade80" style="animation-duration:4.8s;animation-delay:2s"/>
<circle class="rp" cx="1160" cy="700" r="1.2" fill="#22d3ee" style="animation-duration:5.5s;animation-delay:.6s"/>
<circle class="rp" cx="1220" cy="380" r="1" fill="#f59e0b" style="animation-duration:6.4s;animation-delay:1.6s"/>

<!-- SPARKLES -->
<g class="tw" style="animation-delay:.4s"><path d="M480 95h-5v-5h-6v5h-5v6h5v5h6v-5h5z" fill="none" stroke="#22d3ee" stroke-width="1.5"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M910 110h-5v-5h-6v5h-5v6h5v5h6v-5h5z" fill="none" stroke="#f59e0b" stroke-width="1.5"/></g>

<!-- ============ LEFT: CONTENT ============ -->
<text clip-path="url(#cPrompt)" x="48" y="69" font-size="14">
  <tspan fill="#4ade80" font-weight="bold">bharath@ece-eng</tspan><tspan fill="#8b949e">:~$ </tspan><tspan fill="#e6edf3">cat </tspan><tspan fill="#22d3ee">profile.v</tspan>
</text>
<rect x="500" y="56" width="8" height="16" fill="#4ade80" opacity="0">
  <animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" begin="1.35s"/>
</rect>

<text clip-path="url(#cHi)" x="48" y="112" font-size="23" font-weight="bold" fill="#e6edf3">Hi, I'm &#128075;</text>

<!-- NAME: Perfectly sized & spaced so NO clipping occurs -->
<text class="name-t" x="48" y="172" font-size="40" font-weight="bold" font-style="italic" fill="url(#nameg)" filter="url(#glowC)" letter-spacing="1" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".7s" begin="1.4s" fill="freeze"/>
  Bharath G Devadiga
</text>

<g class="hb" style="animation-delay:3s">
  <path d="M495 152 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#22d3ee" opacity=".9"/>
</g>

<!-- CYCLING ROLES -->
<text clip-path="url(#r1)" x="48" y="226" font-size="16" fill="#22d3ee" filter="url(#glow)">&lt; VLSI &amp; Physical Design /&gt;</text>
<text clip-path="url(#r2)" x="48" y="226" font-size="16" fill="#22d3ee" filter="url(#glow)">&lt; FPGA &amp; RTL Engineering /&gt;</text>
<text clip-path="url(#r3)" x="48" y="226" font-size="16" fill="#22d3ee" filter="url(#glow)">&lt; C++ &amp; Embedded Systems /&gt;</text>
<text clip-path="url(#r4)" x="48" y="226" font-size="16" fill="#22d3ee" filter="url(#glow)">&lt; Android App Developer /&gt;</text>
<rect x="48" y="213" width="2.5" height="16" fill="#22d3ee" opacity="0">
  <animate attributeName="opacity" values="1;0" dur=".8s" repeatCount="indefinite" begin="2.9s"/>
</rect>

<!-- QUOTE BOX -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="254" width="450" height="70" rx="8" fill="#0d1e30" stroke="#1a3a5c" stroke-width="1"/>
  <rect x="48" y="258" width="3.5" height="62" rx="1.5" fill="#22d3ee"/>
</g>
<text clip-path="url(#q1)" x="74" y="282" font-size="14.5" fill="#e6edf3">I don't just write code,</text>
<text clip-path="url(#q2)" x="74" y="308" font-size="14.5"><tspan fill="#e6edf3">I </tspan><tspan fill="#22d3ee" font-weight="bold">design</tspan><tspan fill="#e6edf3"> the silicon that runs it.</tspan></text>

<!-- TECH SECTION -->
<text class="ii" x="48" y="364" font-size="15" fill="#f59e0b" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">&#9881;&#65039; Tech Stack</text>

<!-- PILLS ROW 1 -->
<g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="378" width="82" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="89" y="395" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">Verilog</text></g>
<g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="138" y="378" width="64" height="26" rx="13" fill="rgba(74,222,128,.12)" stroke="#4ade80" stroke-width="1"/><text x="170" y="395" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">C++</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="210" y="378" width="64" height="26" rx="13" fill="rgba(245,158,11,.10)" stroke="#f59e0b" stroke-width="1"/><text x="242" y="395" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">Java</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="282" y="378" width="72" height="26" rx="13" fill="rgba(129,140,248,.12)" stroke="#818cf8" stroke-width="1"/><text x="318" y="395" text-anchor="middle" font-size="12" fill="#a5b4fc" font-weight="bold">ESP32</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="362" y="378" width="64" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="394" y="395" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">VLSI</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="434" y="378" width="72" height="26" rx="13" fill="rgba(74,222,128,.10)" stroke="#4ade80" stroke-width="1"/><text x="470" y="395" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">Vivado</text></g>

<!-- PILLS ROW 2 -->
<g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="48" y="412" width="56" height="26" rx="13" fill="rgba(74,222,128,.10)" stroke="#4ade80" stroke-width="1"/><text x="76" y="429" text-anchor="middle" font-size="12" fill="#86efac" font-weight="bold">IoT</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="112" y="412" width="135" height="26" rx="13" fill="rgba(245,158,11,.10)" stroke="#f59e0b" stroke-width="1"/><text x="179" y="429" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">Android Studio</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.6s forwards"><rect x="255" y="412" width="72" height="26" rx="13" fill="rgba(129,140,248,.10)" stroke="#818cf8" stroke-width="1"/><text x="291" y="429" text-anchor="middle" font-size="12" fill="#a5b4fc" font-weight="bold">FPGA</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.7s forwards"><rect x="335" y="412" width="76" height="26" rx="13" fill="rgba(34,211,238,.10)" stroke="#22d3ee" stroke-width="1"/><text x="373" y="429" text-anchor="middle" font-size="12" fill="#67e8f9" font-weight="bold">Linux</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.8s forwards"><rect x="419" y="412" width="86" height="26" rx="13" fill="rgba(245,158,11,.10)" stroke="#f59e0b" stroke-width="1"/><text x="462" y="429" text-anchor="middle" font-size="12" fill="#fcd34d" font-weight="bold">RTL-GDS</text></g>

<!-- ABOUT ME -->
<text class="ii" x="48" y="478" font-size="15" fill="#22d3ee" font-weight="bold" style="animation:fadeIn .4s ease 5.9s forwards">&#128161; Core Focus</text>
<text class="ii" x="48" y="504" font-size="13" style="animation:fadeIn .4s ease 6.1s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#cdd3dd">Bridging digital hardware design with intelligent software.</tspan></text>
<text class="ii" x="48" y="528" font-size="13" style="animation:fadeIn .4s ease 6.3s forwards"><tspan fill="#f59e0b">&#9889; </tspan><tspan fill="#cdd3dd">Synthesizing RTL architectures &amp; physical VLSI layouts.</tspan></text>
<text class="ii" x="48" y="552" font-size="13" style="animation:fadeIn .4s ease 6.5s forwards"><tspan fill="#22d3ee">&#128640; </tspan><tspan fill="#cdd3dd">Crafting custom hardware integrations &amp; mobile solutions.</tspan></text>

<!-- STATS CARD -->
<g class="st" style="animation:fadeIn .5s ease 6.6s forwards">
  <rect x="48" y="582" width="530" height="66" rx="12" fill="#0d1e30" stroke="#1a3a5c" stroke-width="1"/>
  <line x1="180" y1="594" x2="180" y2="636" class="sep"/>
  <line x1="312" y1="594" x2="312" y2="636" class="sep"/>
  <line x1="444" y1="594" x2="444" y2="636" class="sep"/>
  <text x="114" y="608" text-anchor="middle" font-size="11" fill="#9aa4b2">&#128230; Repos</text>
  <text x="246" y="608" text-anchor="middle" font-size="11" fill="#9aa4b2">&#128187; Commits</text>
  <text x="378" y="608" text-anchor="middle" font-size="11" fill="#9aa4b2">&#11088; Stars</text>
  <text x="500" y="608" text-anchor="middle" font-size="11" fill="#9aa4b2">&#128101; Followers</text>
</g>
<text class="st" x="114" y="636" text-anchor="middle" font-size="17" font-weight="bold" fill="#22d3ee" filter="url(#glow)" style="animation:fadeIn .4s ease 6.8s forwards">12+</text>
<text class="st" x="246" y="636" text-anchor="middle" font-size="17" font-weight="bold" fill="#f59e0b" filter="url(#glow)" style="animation:fadeIn .4s ease 6.95s forwards">500+</text>
<text class="st" x="378" y="636" text-anchor="middle" font-size="17" font-weight="bold" fill="#4ade80" filter="url(#glow)" style="animation:fadeIn .4s ease 7.1s forwards">50+</text>
<text class="st" x="500" y="636" text-anchor="middle" font-size="17" font-weight="bold" fill="#818cf8" filter="url(#glow)" style="animation:fadeIn .4s ease 7.25s forwards">25+</text>

<!-- ============ RIGHT: IMAGE ============ -->
<circle cx="1010" cy="440" r="270" fill="url(#imgGlow)"><animate attributeName="r" values="270;292;270" dur="5s" repeatCount="indefinite"/></circle>
<g class="fl">
  <g clip-path="url(#imgReveal)">
    <image x="740" y="152" width="540" height="522" preserveAspectRatio="xMidYMid slice" href="__IMG__"/>
  </g>
  <g clip-path="url(#imgBox)">
    <rect x="738" y="152" width="4" height="522" fill="url(#scanLineV)" filter="url(#glow)" opacity="0">
      <animate attributeName="opacity" values="0;.95;.95;0" keyTimes="0;.04;.9;1" dur="2s" begin=".5s" fill="freeze"/>
      <animate attributeName="x" from="738" to="1278" dur="1.8s" begin=".5s" fill="freeze"/>
    </rect>
  </g>
</g>

<!-- ============ VERILOG CODE CARD (Shifted right to x=540 so zero collision with name) ============ -->
<g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
  <rect x="540" y="38" width="310" height="236" rx="12" fill="#07111e" fill-opacity=".96" stroke="#1a3a5c" stroke-width="1.2"/>
  <rect x="540" y="38" width="310" height="28" rx="12" fill="#0f1e30"/>
  <rect x="540" y="54" width="310" height="12" fill="#0f1e30"/>
  <circle cx="558" cy="52" r="4" fill="#ff5f57"/>
  <circle cx="572" cy="52" r="4" fill="#febc2e"/>
  <circle cx="586" cy="52" r="4" fill="#28c840"/>
  <text x="700" y="56" text-anchor="middle" font-size="11" fill="#8b949e">ece_module.v</text>
</g>
<g font-size="12">
  <text class="cl" x="556" y="86" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#818cf8">module </tspan><tspan fill="#22d3ee">bharath</tspan><tspan fill="#e6edf3"> #(</tspan></text>
  <text class="cl" x="572" y="105" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#f59e0b">parameter </tspan><tspan fill="#4ade80">SKILLS</tspan><tspan fill="#e6edf3"> = 8</tspan></text>
  <text class="cl" x="556" y="124" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#e6edf3">) (</tspan></text>
  <text class="cl" x="572" y="143" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#818cf8">output </tspan><tspan fill="#22d3ee">solutions</tspan><tspan fill="#e6edf3">,</tspan></text>
  <text class="cl" x="572" y="162" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#818cf8">input  </tspan><tspan fill="#f59e0b">problems</tspan></text>
  <text class="cl" x="556" y="181" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#e6edf3">);</tspan></text>
  <text class="cl" x="572" y="200" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#8b949e">// always solving</tspan></text>
  <text class="cl" x="572" y="219" style="animation:fadeIn .3s ease 3.65s forwards"><tspan fill="#818cf8">always </tspan><tspan fill="#e6edf3">@(*) begin</tspan></text>
  <text class="cl" x="556" y="238" style="animation:fadeIn .3s ease 3.85s forwards"><tspan fill="#22d3ee">endmodule</tspan><tspan fill="#8b949e"> // ECE &amp; Logic</tspan></text>
  <text class="cl" x="556" y="256" style="animation:fadeIn .3s ease 4.0s forwards"><tspan fill="#8b949e">// RTL to Silicon Builder</tspan></text>
</g>

<!-- NEON SIGN -->
<g class="neon-on">
  <rect x="1024" y="38" width="226" height="124" rx="14" fill="none" stroke="#f59e0b" stroke-width="1.5" opacity=".55" filter="url(#glow)"/>
  <text class="np" x="1137" y="84" text-anchor="middle" font-size="30" font-weight="bold" fill="#22d3ee" filter="url(#glowBig)">&#9651;</text>
  <text class="np" x="1137" y="114" text-anchor="middle" font-size="18" font-weight="bold" fill="#f59e0b" filter="url(#glow)" letter-spacing="3">DESIGN IT</text>
  <text class="np" x="1137" y="140" text-anchor="middle" font-size="18" font-weight="bold" fill="#22d3ee" filter="url(#glow)" letter-spacing="2.5" style="animation-delay:1.3s">BUILD IT</text>
</g>

<!-- PIXEL GEAR -->
<g class="fl2" style="animation-delay:.7s">
  <g transform="translate(610,290)" opacity="0">
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

<g class="hb" style="animation-delay:1.4s">
  <path d="M1234 320 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#f59e0b" opacity=".85" filter="url(#glow)"/>
</g>

<!-- ============ FOOTER ============ -->
<line x1="48" y1="676" x2="1232" y2="676" stroke="#1e2a3a" stroke-width="1" opacity=".7" stroke-dasharray="1184" stroke-dashoffset="1184">
  <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.2s" fill="freeze"/>
</line>
<g class="soc" style="animation:fadeIn .5s ease 7.4s forwards">
  <g transform="translate(48,692) scale(.8)">
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#c9d1d9"/>
  </g>
  <text x="74" y="707" font-size="12.5" fill="#c9d1d9">BharathGDevadiga</text>
  <g transform="translate(226,693) scale(.8)">
    <rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#22d3ee" stroke-width="2"/>
    <path d="M2.5 5.5 12 13l9.5-7.5" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="252" y="707" font-size="12.5" fill="#c9d1d9">bharathgdudupi@gmail.com</text>
  <g transform="translate(478,692) scale(.8)">
    <rect width="24" height="24" rx="4" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="7" cy="8" r="1.5" fill="#f59e0b"/>
    <line x1="7" y1="11" x2="7" y2="18" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    <path d="M11 13a3 3 0 016 0v5" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    <line x1="11" y1="11" x2="11" y2="18" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
  </g>
  <text x="504" y="707" font-size="12.5" fill="#c9d1d9">bharath-g-devadiga</text>
</g>
<text class="soc" x="1232" y="707" text-anchor="end" font-size="13" style="animation:fadeIn .5s ease 7.6s forwards">
  <tspan fill="#8b949e">"</tspan><tspan fill="#22d3ee">Hardware is my canvas, Logic is my superpower.</tspan><tspan fill="#8b949e">" </tspan><tspan fill="#f59e0b">&#9889;</tspan>
</text>
<text class="soc" x="720" y="707" font-size="11.5" style="animation:fadeIn .5s ease 7.5s forwards">
  <tspan fill="#4ade80">&#9679;</tspan><tspan fill="#8b949e"> open to collaborate</tspan>
</text>

<!-- FULL-BANNER SCANNER -->
<g clip-path="url(#bannerBox)" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="-60,0;1340,0" dur="3.5s" begin="3s" repeatCount="indefinite"/>
    <rect x="-34" y="0" width="34" height="740" fill="url(#scanTrailH)"/>
    <rect x="0" y="0" width="2.6" height="740" fill="url(#fullScanV)" opacity=".6" filter="url(#glow)"/>
  </g>
</g>
</svg>"""

DARK_BANNER = DARK_BANNER.replace("__IMG__", img_b64)

with open("bharath-banner.svg", "w", encoding="utf-8") as f:
    f.write(DARK_BANNER)

# =========================================================================
# 2. LIGHT BANNER GENERATION (Clean, Crisp Slate & Blue theme)
# =========================================================================
LIGHT_BANNER = DARK_BANNER

# Replace backgrounds & containers
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#090e1b"', 'stop-color="#f8fafc"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#0c1222"', 'stop-color="#ffffff"')
LIGHT_BANNER = LIGHT_BANNER.replace('stop-color="#070b16"', 'stop-color="#f1f5f9"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="rgba(34,211,238,.08)"', 'fill="rgba(2,132,199,.08)"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#1a3a5c"', 'stroke="#cbd5e1"')
LIGHT_BANNER = LIGHT_BANNER.replace('stroke="#1e2a3a"', 'stroke="#cbd5e1"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#0d1e30"', 'fill="#ffffff"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#07111e"', 'fill="#f8fafc"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#0f1e30"', 'fill="#e2e8f0"')

# Replace text colors for high readability
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#e6edf3"', 'fill="#0f172a"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#cdd3dd"', 'fill="#334155"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#c9d1d9"', 'fill="#1e293b"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#9aa4b2"', 'fill="#64748b"')
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#8b949e"', 'fill="#64748b"')

# Replace accent colors with rich daytime versions
LIGHT_BANNER = LIGHT_BANNER.replace('#22d3ee', '#0284c7')
LIGHT_BANNER = LIGHT_BANNER.replace('#38bdf8', '#0369a1')
LIGHT_BANNER = LIGHT_BANNER.replace('#06b6d4', '#0284c7')
LIGHT_BANNER = LIGHT_BANNER.replace('#67e8f9', '#0369a1')
LIGHT_BANNER = LIGHT_BANNER.replace('#f59e0b', '#d97706')
LIGHT_BANNER = LIGHT_BANNER.replace('#fcd34d', '#b45309')
LIGHT_BANNER = LIGHT_BANNER.replace('#4ade80', '#16a34a')
LIGHT_BANNER = LIGHT_BANNER.replace('#86efac', '#15803d')
LIGHT_BANNER = LIGHT_BANNER.replace('#818cf8', '#4f46e5')
LIGHT_BANNER = LIGHT_BANNER.replace('#a5b4fc', '#4338ca')

# Update pill backgrounds
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(34,211,238,.10)', 'rgba(2,132,199,.12)')
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(74,222,128,.12)', 'rgba(22,163,74,.12)')
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(74,222,128,.10)', 'rgba(22,163,74,.12)')
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(245,158,11,.10)', 'rgba(217,119,6,.12)')
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(129,140,248,.12)', 'rgba(79,70,229,.12)')
LIGHT_BANNER = LIGHT_BANNER.replace('rgba(129,140,248,.10)', 'rgba(79,70,229,.12)')

# Replace gear inner fill
LIGHT_BANNER = LIGHT_BANNER.replace('fill="#090e1b"', 'fill="#ffffff"')

with open("bharath-banner-light.svg", "w", encoding="utf-8") as f:
    f.write(LIGHT_BANNER)

print("Both dark and light banners created successfully!")
