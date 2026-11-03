#!/usr/bin/env python3
"""
Generates all LK Informatik HTML pages (13 Theorie + 11 Praktikum).
- No rating box
- Includes lk-viz.css + lk-viz.js
- Injects interactive visualizations per topic
"""
import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

TOPICS = [
    (1,  "Binär- & Hexadezimalzahlen",  "--c1",  "Thema1_Binaer_und_Hexadezimalzahlen",               "Zahlensysteme · Grundlagen"),
    (2,  "Binäre Arithmetik",            "--c2",  "Thema2_Binaere_Arithmetik_V2",                       "Rechnen · ALU"),
    (3,  "Einer- & Zweierkomplement",    "--c3",  "Thema3_Einer_und_Zweierkomplement",                  "Negative Zahlen · Vorzeichen"),
    (4,  "Fest- & Gleitkommazahlen",     "--c4",  "Thema4_Fest_und_Gleitkommazahlen",                   "IEEE 754 · Kommazahlen"),
    (5,  "Nachricht & Information",      "--c5",  "Thema5_Nachricht_Information_Nachrichtentraeger",     "Shannon · Entropie · Codierung"),
    (6,  "Datenkompression",             "--c6",  "Thema6_Datenkompression",                             "Huffman · LZW · RLE · Delta"),
    (7,  "Hashing",                      "--c7",  "Thema7_Hashing",                                     "Hashtabellen · SHA · Kollisionen"),
    (8,  "Hamming-Codes",                "--c8",  "Thema8_Hamming_Codes",                               "Fehlerkorrektur · Parität"),
    (9,  "Java-Grundlagen",              "--c9",  "Thema9_Java_Grundlagen",                             "Syntax · Typen · Methoden"),
    (10, "Softwareentwicklung",          "--c10", "Thema10_Softwareentwicklung_Wasserfallmodell",        "Wasserfallmodell · Agil · Scrum"),
    (11, "Objektorientierung",           "--c11", "Thema11_Objektorientierung",                          "OOP · Klassen · Vererbung"),
    (12, "Struktogramme",                "--c12", "Thema12_Struktogramme_und_Ablaufplaene",              "Nassi-Shneiderman · Flussdiagramm"),
    (13, "Sortieralgorithmen",           "--c13", "Thema13_Sortieralgorithmen",                          "Quicksort · Mergesort · O-Notation"),
]

# Praktikum track – stored separately so sidebar can add a section label
PRAKTIKUM = [
    (1,  "Hallo Welt",                  "--c1",  "Praktikum1_Hallo_Welt",                              "println · Klasse · main"),
    (2,  "Variablen",                   "--c2",  "Praktikum2_Variablen",                                "int · double · String · boolean"),
    (3,  "Konsoleneingabe",             "--c3",  "Praktikum3_Konsoleneingabe",                          "Scanner · nextLine · nextInt"),
    (4,  "Bedingungen",                 "--c4",  "Praktikum4_Bedingungen",                              "if · else if · else"),
    (5,  "switch",                      "--c5",  "Praktikum5_Switch",                                   "switch · case · break · default"),
    (6,  "Arrays",                      "--c6",  "Praktikum6_Arrays",                                   "Arrays · for · for-each"),
    (7,  "while",                       "--c7",  "Praktikum7_While",                                    "while · do-while · break"),
    (8,  "Methoden Grundlagen",         "--c8",  "Praktikum8_Methoden_Grundlagen",                      "void · return · Parameter"),
    (9,  "Methoden Fortgeschritten",    "--c9",  "Praktikum9_Methoden_Fortgeschritten",                 "Overloading · final · Scope"),
    (10, "Klassen Grundlagen",          "--c10", "Praktikum10_Klassen_Grundlagen",                      "class · Konstruktor · new · this"),
    (11, "OOP Getränkeautomat",         "--c11", "Praktikum11_OOP_Getraenkeautomat",                    "private · Getter · Setter · toString"),
]

# Klausurvorbereitung track
KLAUSUR = [
    ('k1', "Arrays & 2D-Arrays",        "--c9",  "Klausurvorbereitung_Arrays",  "Kino-Wochenprogramm · Szenario"),
]

ALL_TOPICS = TOPICS + [(f'p{p[0]}', p[1], p[2], p[3], p[4]) for p in PRAKTIKUM]

# ─────────────────────────────────────────────────────────────────────────────
# Visualization HTML snippets – one dict entry per topic number
# Each snippet uses IDs that match lk-viz.js
# ─────────────────────────────────────────────────────────────────────────────
VIZUALIZATIONS = {

1: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Bit-Schalter -->
<div class="viz-box">
  <div class="viz-title">Bit-Schalter – 8-Bit-Zahl erkunden</div>
  <p class="viz-note">Klicke auf die Bits, um sie ein- oder auszuschalten. Dezimal- und Hex-Wert aktualisieren sich automatisch.</p>
  <div id="viz-t1-bits" class="bit-row">
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-sep">·</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
  </div>
  <div class="viz-row" style="margin-top:14px">
    <span class="viz-label">Dezimal:</span><span class="viz-result" id="viz-t1-dec">0</span>
    <span class="viz-label" style="margin-left:20px">Hex:</span><span class="viz-result" id="viz-t1-hex">0x00</span>
  </div>
</div>

<!-- VIZ 2: Divisions-Animation -->
<div class="viz-box">
  <div class="viz-title">Resteverfahren – Dezimal → Binär</div>
  <div class="viz-row">
    <span class="viz-label">Zahl (0–255):</span>
    <input id="viz-t1-div-inp" class="viz-input" type="number" min="0" max="255" value="42" style="width:80px">
    <button id="viz-t1-div-btn" class="viz-btn">Umrechnen ▶</button>
  </div>
  <div id="viz-t1-div-steps" class="step-list" style="margin-top:12px"></div>
  <div class="viz-result" id="viz-t1-div-result" style="margin-top:10px"></div>
</div>

<!-- VIZ 3: Binärzähler -->
<div class="viz-box">
  <div class="viz-title">Binärzähler (4 Bit)</div>
  <p class="viz-note">Beobachte wie Überträge durch die Stellen rollen.</p>
  <div id="viz-t1-counter" class="bit-row">
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
  </div>
  <div class="viz-row" style="margin-top:10px">
    <span class="viz-label">Dezimal:</span><span class="viz-result" id="viz-t1-cnt-dec">0</span>
  </div>
  <div class="viz-row" style="margin-top:10px;gap:8px">
    <button id="viz-t1-cnt-start" class="viz-btn">▶ Start</button>
    <button id="viz-t1-cnt-stop"  class="viz-btn viz-btn-ghost">⏸ Stop</button>
    <button id="viz-t1-cnt-reset" class="viz-btn viz-btn-ghost">↺ Reset</button>
  </div>
</div>

<!-- VIZ 4: Farb-Mixer -->
<div class="viz-box">
  <div class="viz-title">RGB-Farbmixer – Hex-Farben verstehen</div>
  <p class="viz-note">Verschiebe die Regler. Jeder Kanal ist ein Byte (0–255).</p>
  <div id="viz-t1-color">
    <div class="viz-row"><span class="viz-label" style="color:#ff6b9d">Rot:</span>
      <input id="viz-t1-r" class="viz-range" type="range" min="0" max="255" value="255" style="flex:1">
      <span id="viz-t1-bin-r" style="font-family:var(--font-code);font-size:11px;color:var(--text-muted);min-width:80px">11111111</span>
    </div>
    <div class="viz-row"><span class="viz-label" style="color:#4de8b2">Grün:</span>
      <input id="viz-t1-g" class="viz-range" type="range" min="0" max="255" value="0" style="flex:1">
      <span id="viz-t1-bin-g" style="font-family:var(--font-code);font-size:11px;color:var(--text-muted);min-width:80px">00000000</span>
    </div>
    <div class="viz-row"><span class="viz-label" style="color:#38bdf8">Blau:</span>
      <input id="viz-t1-b" class="viz-range" type="range" min="0" max="255" value="0" style="flex:1">
      <span id="viz-t1-bin-b" style="font-family:var(--font-code);font-size:11px;color:var(--text-muted);min-width:80px">00000000</span>
    </div>
    <div id="viz-t1-preview" class="color-preview"></div>
    <div class="viz-row" style="margin-top:8px">
      <span class="viz-label">Hex-Code:</span><span class="viz-result" id="viz-t1-hexout">#FF0000</span>
    </div>
  </div>
</div>
""",

2: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Binäre Addition -->
<div class="viz-box">
  <div class="viz-title">Binäre Addition mit Überträgen</div>
  <div class="viz-row">
    <span class="viz-label">A (binär):</span>
    <input id="viz-t2-a" class="viz-input" type="text" value="01010101" maxlength="8" style="width:120px">
    <span class="viz-label">B (binär):</span>
    <input id="viz-t2-b" class="viz-input" type="text" value="00110011" maxlength="8" style="width:120px">
    <button id="viz-t2-add-btn" class="viz-btn">Addieren ▶</button>
  </div>
  <div id="viz-t2-arena" style="margin-top:14px"></div>
</div>

<!-- VIZ 2: Bit-Verschiebung -->
<div class="viz-box">
  <div class="viz-title">Bit-Verschiebung (Shift)</div>
  <p class="viz-note">Links-Shift = ×2, Rechts-Shift = ÷2</p>
  <div class="viz-row">
    <span class="viz-label">Startwert:</span>
    <input id="viz-t2-shift-inp" class="viz-input" type="number" min="0" max="255" value="12" style="width:80px">
  </div>
  <div id="viz-t2-shift" class="bit-row" style="margin:12px 0">
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-sep">·</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
  </div>
  <div class="viz-row">
    <span class="viz-label">Dezimal:</span><span class="viz-result" id="viz-t2-shift-dec">0</span>
    <span class="viz-label" style="margin-left:16px">Letzte Op:</span><span class="viz-result" id="viz-t2-shift-op">–</span>
  </div>
  <div class="viz-row" style="margin-top:10px;gap:8px">
    <button id="viz-t2-left"  class="viz-btn">◀ Links-Shift (×2)</button>
    <button id="viz-t2-right" class="viz-btn viz-btn-ghost">Rechts-Shift (÷2) ▶</button>
  </div>
</div>

<!-- VIZ 3: Overflow -->
<div class="viz-box">
  <div class="viz-title">Overflow – 4-Bit-Register</div>
  <p class="viz-note">Klicke wiederholt auf "+1". Bei 1111+1 springt das Register auf 0000.</p>
  <div id="viz-t2-overflow-bits" class="bit-row" style="margin:12px 0">
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
  </div>
  <div class="viz-row">
    <span class="viz-label">Dezimal:</span><span class="viz-result" id="viz-t2-overflow-dec">0</span>
  </div>
  <div id="viz-t2-overflow-msg" style="margin-top:8px;font-size:13px;font-family:var(--font-code)"></div>
  <div class="viz-row" style="margin-top:10px;gap:8px">
    <button id="viz-t2-overflow-btn"   class="viz-btn">+1</button>
    <button id="viz-t2-overflow-reset" class="viz-btn viz-btn-ghost">↺ Reset</button>
  </div>
</div>
""",

3: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Bit-Inverter -->
<div class="viz-box">
  <div class="viz-title">Einer- &amp; Zweierkomplement live</div>
  <p class="viz-note">Klicke auf die Bits oben. Einer- und Zweierkomplement werden sofort berechnet.</p>
  <div class="viz-label" style="margin-bottom:6px">Eingabe (positiver Wert):</div>
  <div id="viz-t3-inv" class="bit-row">
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-cell">0</div><div class="bit-cell">0</div>
    <div class="bit-sep">·</div>
    <div class="bit-cell">0</div><div class="bit-cell">1</div>
    <div class="bit-cell">0</div><div class="bit-cell">1</div>
  </div>
  <div class="viz-row" style="margin-top:8px">
    <span class="viz-label">Dezimal:</span><span class="viz-result" id="viz-t3-inv-dec">5</span>
  </div>
  <div id="viz-t3-ek" class="bit-row" style="margin-top:14px">
    <div class="bit-cell" style="border-color:#ff6b9d">0</div><div class="bit-cell" style="border-color:#ff6b9d">0</div>
    <div class="bit-cell" style="border-color:#ff6b9d">0</div><div class="bit-cell" style="border-color:#ff6b9d">0</div>
    <div class="bit-sep">·</div>
    <div class="bit-cell" style="border-color:#ff6b9d">0</div><div class="bit-cell" style="border-color:#ff6b9d">0</div>
    <div class="bit-cell" style="border-color:#ff6b9d">0</div><div class="bit-cell" style="border-color:#ff6b9d">0</div>
  </div>
  <div class="viz-note" id="viz-t3-ek-dec">Einerkomplement = …</div>
  <div id="viz-t3-zk" class="bit-row" style="margin-top:10px">
    <div class="bit-cell" style="border-color:#ffa047">0</div><div class="bit-cell" style="border-color:#ffa047">0</div>
    <div class="bit-cell" style="border-color:#ffa047">0</div><div class="bit-cell" style="border-color:#ffa047">0</div>
    <div class="bit-sep">·</div>
    <div class="bit-cell" style="border-color:#ffa047">0</div><div class="bit-cell" style="border-color:#ffa047">0</div>
    <div class="bit-cell" style="border-color:#ffa047">0</div><div class="bit-cell" style="border-color:#ffa047">0</div>
  </div>
  <div class="viz-note" id="viz-t3-zk-dec">Zweierkomplement = …</div>
</div>

<!-- VIZ 2: Zahlenkreis -->
<div class="viz-box">
  <div class="viz-title">4-Bit-Zweierkomplement Zahlenkreis</div>
  <p class="viz-note">Klicke auf einen Kreis, um den Binärwert und Dezimalwert zu sehen.</p>
  <div style="display:flex;justify-content:center">
    <canvas id="viz-t3-circle" width="280" height="280" style="cursor:pointer;border-radius:8px;background:var(--bg-code)"></canvas>
  </div>
</div>
""",

4: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: IEEE 754 Zerlegung -->
<div class="viz-box">
  <div class="viz-title">IEEE 754 – Dezimalzahl zerlegen</div>
  <p class="viz-note"><span style="color:#ff6b9d">■ Vorzeichen</span> &nbsp;<span style="color:#ffa047">■ Exponent (8 Bit)</span> &nbsp;<span style="color:#4de8b2">■ Mantisse (23 Bit)</span></p>
  <div class="viz-row">
    <span class="viz-label">Zahl:</span>
    <input id="viz-t4-ieee-inp" class="viz-input" type="number" value="13.5" step="any" style="width:120px">
  </div>
  <div id="viz-t4-ieee-bits" class="bit-row" style="margin:14px 0;flex-wrap:wrap;gap:2px">
    <!-- 32 bits injected by JS -->
  </div>
  <div style="font-family:var(--font-code);font-size:12px;display:flex;flex-direction:column;gap:6px;margin-top:8px">
    <div><span class="viz-label">Vorzeichen:</span> <span id="viz-t4-ieee-sign" class="viz-result"></span></div>
    <div><span class="viz-label">Exponent:  </span> <span id="viz-t4-ieee-exp"  class="viz-result"></span></div>
    <div><span class="viz-label">Mantisse:  </span> <span id="viz-t4-ieee-man"  class="viz-result"></span></div>
    <div><span class="viz-label">Darstellung:</span><span id="viz-t4-ieee-info" class="viz-result"></span></div>
  </div>
</div>

<!-- VIZ 2: Bias-Rechner -->
<div class="viz-box">
  <div class="viz-title">Exponent-Bias (127) erkunden</div>
  <p class="viz-note">Verschiebe den Schieberegler für den gespeicherten Exponenten (0–255).</p>
  <div class="viz-row">
    <span class="viz-label">Gespeichert:</span>
    <input id="viz-t4-bias-sl" class="viz-range" type="range" min="0" max="255" value="130" style="flex:1">
  </div>
  <div style="font-family:var(--font-code);font-size:13px;display:flex;flex-direction:column;gap:6px;margin-top:10px">
    <div><span class="viz-label">Gespeicherter Wert:</span> <span id="viz-t4-bias-stored" class="viz-result"></span></div>
    <div><span class="viz-label">Echter Exponent:  </span> <span id="viz-t4-bias-real"   class="viz-result"></span></div>
    <div><span class="viz-label">Bedeutet:         </span> <span id="viz-t4-bias-pow"    class="viz-result"></span></div>
  </div>
</div>
""",

5: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Informationsgehalt -->
<div class="viz-box">
  <div class="viz-title">Informationsgehalt I(x) = −log₂(P)</div>
  <p class="viz-note">Je unwahrscheinlicher ein Ereignis, desto mehr Information trägt es.</p>
  <div class="viz-row">
    <span class="viz-label">P(x):</span>
    <input id="viz-t5-prob-sl" class="viz-range" type="range" min="0.01" max="1" step="0.01" value="0.5" style="flex:1">
    <span id="viz-t5-prob-val" class="viz-result" style="min-width:50px">0.500</span>
  </div>
  <div class="viz-row" style="margin-top:8px">
    <span class="viz-label">I(x):</span><span class="viz-result" id="viz-t5-info-val">1.000 Bit</span>
  </div>
</div>

<!-- VIZ 2: Entropie -->
<div class="viz-box">
  <div class="viz-title">Shannon-Entropie – Zwei Zeichen A und B</div>
  <p class="viz-note">Maximum bei P(A) = P(B) = 0.5 → H = 1 Bit</p>
  <div class="viz-row">
    <span class="viz-label">P(A):</span>
    <input id="viz-t5-ent-a" class="viz-range" type="range" min="0.01" max="0.99" step="0.01" value="0.5" style="flex:1">
  </div>
  <div class="viz-row" style="margin-top:6px">
    <span class="viz-label">P(A) = </span><span id="viz-t5-pa" class="viz-result">0.50</span>
    <span class="viz-label" style="margin-left:16px">P(B) = </span><span id="viz-t5-pb" class="viz-result">0.50</span>
    <span class="viz-label" style="margin-left:16px">H = </span><span id="viz-t5-h" class="viz-result">1.0000 Bit</span>
  </div>
  <div style="display:flex;align-items:flex-end;gap:16px;margin-top:14px;height:110px">
    <div style="display:flex;flex-direction:column;align-items:center;gap:4px;flex:1">
      <div id="viz-t5-bar-a" style="width:100%;background:#7c6aff;border-radius:4px 4px 0 0;transition:height .3s;height:50px"></div>
      <span style="font-size:11px;color:var(--text-muted)">P(A)</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:4px;flex:1">
      <div id="viz-t5-bar-b" style="width:100%;background:#ff6b9d;border-radius:4px 4px 0 0;transition:height .3s;height:50px"></div>
      <span style="font-size:11px;color:var(--text-muted)">P(B)</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:4px;flex:2">
      <div id="viz-t5-bar-h" style="width:100%;background:var(--active);border-radius:4px 4px 0 0;transition:height .3s;height:100px"></div>
      <span style="font-size:11px;color:var(--text-muted)">H (Entropie)</span>
    </div>
  </div>
</div>

<!-- VIZ 3: ASCII -->
<div class="viz-box">
  <div class="viz-title">ASCII-Codierung interaktiv</div>
  <div class="viz-row">
    <span class="viz-label">Zeichen:</span>
    <input id="viz-t5-ascii-inp" class="viz-input" type="text" maxlength="1" value="A" style="width:60px;text-align:center;font-size:22px">
  </div>
  <div style="font-family:var(--font-code);font-size:13px;display:flex;flex-direction:column;gap:6px;margin-top:10px">
    <div><span class="viz-label">Zeichen:  </span><span id="viz-t5-ascii-char" class="viz-result">"A"</span></div>
    <div><span class="viz-label">Binär:    </span><span id="viz-t5-ascii-bin"  class="viz-result">1000001₂</span></div>
    <div><span class="viz-label">Dezimal:  </span><span id="viz-t5-ascii-dec"  class="viz-result">65₁₀ (0x41)</span></div>
  </div>
</div>
""",

6: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: RLE -->
<div class="viz-box">
  <div class="viz-title">Lauflängencodierung (RLE) – live</div>
  <div class="viz-row">
    <input id="viz-t6-rle-inp" class="viz-input" type="text" value="AAAABBBBBCCAAA" style="width:220px">
    <button id="viz-t6-rle-btn" class="viz-btn">Codieren ▶</button>
  </div>
  <div id="viz-t6-rle-out"   style="font-family:var(--font-code);font-size:16px;margin-top:14px;letter-spacing:2px"></div>
  <div id="viz-t6-rle-ratio" class="viz-note" style="margin-top:8px"></div>
</div>

<!-- VIZ 2: Huffman -->
<div class="viz-box">
  <div class="viz-title">Huffman-Codierung – Häufigkeiten & Codes</div>
  <div class="viz-row">
    <span class="viz-label">Text:</span>
    <input id="viz-t6-huff-inp" class="viz-input" type="text" value="AABBBCDDDD" style="width:200px">
    <button id="viz-t6-huff-btn" class="viz-btn">Huffman ▶</button>
  </div>
  <div id="viz-t6-huff-codes" style="margin-top:14px"></div>
</div>
""",

7: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Hashtabelle -->
<div class="viz-box">
  <div class="viz-title">Hashtabellen-Simulator  h(k) = k mod m</div>
  <div class="viz-row">
    <span class="viz-label">Schlüssel:</span>
    <input id="viz-t7-key" class="viz-input" type="number" value="23" style="width:80px">
    <span class="viz-label">m:</span>
    <input id="viz-t7-m" class="viz-input" type="number" value="7" min="3" max="13" style="width:60px">
    <button id="viz-t7-hash-btn"   class="viz-btn">Einfügen ▶</button>
    <button id="viz-t7-hash-reset" class="viz-btn viz-btn-ghost">↺</button>
  </div>
  <div id="viz-t7-table" style="margin-top:14px"></div>
</div>

<!-- VIZ 2: Lawineneffekt -->
<div class="viz-box">
  <div class="viz-title">Lawineneffekt – kleine Änderung, großer Unterschied</div>
  <div class="viz-row">
    <input id="viz-t7-av-inp1" class="viz-input" type="text" value="Hallo" style="width:140px">
    <input id="viz-t7-av-inp2" class="viz-input" type="text" value="hallo" style="width:140px">
    <button id="viz-t7-av-btn" class="viz-btn">Hashen ▶</button>
  </div>
  <div style="font-family:var(--font-code);font-size:13px;margin-top:14px;display:flex;flex-direction:column;gap:6px">
    <div>Hash 1: <span id="viz-t7-av-out1" class="viz-result"></span></div>
    <div>Hash 2: <span id="viz-t7-av-out2" class="viz-result"></span></div>
    <div id="viz-t7-av-diff" class="viz-note"></div>
  </div>
</div>
""",

8: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Hamming codieren -->
<div class="viz-box">
  <div class="viz-title">Hamming-Code erzeugen (4 Datenbits → 7 Bit)</div>
  <p class="viz-note"><span style="color:#e06cff">■ Prüfbits (p₁,p₂,p₄)</span> &nbsp;<span style="color:#38bdf8">■ Datenbits</span></p>
  <div class="viz-row">
    <span class="viz-label">4 Datenbits:</span>
    <input id="viz-t8-data-inp" class="viz-input" type="text" value="1011" maxlength="4" style="width:90px">
    <button id="viz-t8-enc-btn" class="viz-btn">Codieren ▶</button>
  </div>
  <div id="viz-t8-enc-bits" class="bit-row" style="margin:14px 0">
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div>
  </div>
  <div class="viz-row"><span class="viz-label">7-Bit-Code:</span><span class="viz-result" id="viz-t8-enc-out">–</span></div>
</div>

<!-- VIZ 2: Fehler erkennen -->
<div class="viz-box">
  <div class="viz-title">Fehler erkennen &amp; korrigieren</div>
  <p class="viz-note">Gib einen empfangenen 7-Bit-Code ein (kann fehlerhaft sein).</p>
  <div class="viz-row">
    <span class="viz-label">Empfangen:</span>
    <input id="viz-t8-err-inp" class="viz-input" type="text" value="0110111" maxlength="7" style="width:110px">
    <button id="viz-t8-err-btn" class="viz-btn">Prüfen ▶</button>
  </div>
  <div id="viz-t8-err-bits" class="bit-row" style="margin:12px 0">
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div><div class="bit-cell">?</div>
    <div class="bit-cell">?</div>
  </div>
  <div id="viz-t8-err-out" style="font-family:var(--font-code);font-size:13px;margin-top:6px"></div>
</div>

<!-- VIZ 3: Hamming-Abstand -->
<div class="viz-box">
  <div class="viz-title">Hamming-Abstand zweier Bitketten</div>
  <div class="viz-row">
    <input id="viz-t8-dist-a" class="viz-input" type="text" value="11010" style="width:110px">
    <input id="viz-t8-dist-b" class="viz-input" type="text" value="10110" style="width:110px">
    <button id="viz-t8-dist-btn" class="viz-btn">Berechnen ▶</button>
  </div>
  <div id="viz-t8-dist-out" style="font-family:var(--font-code);font-size:14px;margin-top:12px"></div>
</div>
""",

9: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Datentypen -->
<div class="viz-box">
  <div class="viz-title">Java-Datentypen – Wertebereich &amp; Speicher</div>
  <div class="viz-row">
    <span class="viz-label">Typ:</span>
    <select id="viz-t9-type-sel" class="viz-input" style="width:auto">
      <option value="byte">byte</option>
      <option value="short">short</option>
      <option value="int" selected>int</option>
      <option value="long">long</option>
      <option value="float">float</option>
      <option value="double">double</option>
    </select>
  </div>
  <div style="font-family:var(--font-code);font-size:13px;display:flex;flex-direction:column;gap:6px;margin-top:12px">
    <div><span class="viz-label">Größe:    </span><span id="viz-t9-bits"  class="viz-result"></span></div>
    <div><span class="viz-label">Minimum:  </span><span id="viz-t9-min"   class="viz-result"></span></div>
    <div><span class="viz-label">Maximum:  </span><span id="viz-t9-max"   class="viz-result"></span></div>
    <div><span class="viz-label">Intern:   </span><span id="viz-t9-note"  class="viz-result"></span></div>
  </div>
  <div style="margin-top:12px">
    <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px">Speichergröße relativ zu 64 Bit:</div>
    <div style="height:8px;background:var(--border);border-radius:4px;overflow:hidden">
      <div id="viz-t9-type-bar" style="height:100%;background:var(--active);border-radius:4px;transition:width .4s;width:50%"></div>
    </div>
  </div>
</div>

<!-- VIZ 2: Schleifen-Trace -->
<div class="viz-box">
  <div class="viz-title">Schleifen-Trace – Summe 1 bis n</div>
  <div class="viz-row">
    <span class="viz-label">n:</span>
    <input id="viz-t9-loop-n" class="viz-input" type="number" min="1" max="20" value="5" style="width:70px">
    <button id="viz-t9-loop-btn" class="viz-btn">Ausführen ▶</button>
  </div>
  <div style="margin-top:14px;overflow-x:auto">
    <table class="viz-table">
      <thead><tr><th>i</th><th>summe (vorher)</th><th>summe (nachher)</th></tr></thead>
      <tbody id="viz-t9-loop-tbody"></tbody>
    </table>
  </div>
</div>
""",

10: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Wasserfall-Phasen -->
<div class="viz-box">
  <div class="viz-title">Wasserfallmodell – Phasen interaktiv</div>
  <p class="viz-note">Klicke auf eine Phase für Details.</p>
  <div style="display:flex;flex-direction:column;gap:4px;margin-bottom:14px">
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #00d4ff">1. Anforderungsanalyse</div>
    <div style="text-align:center;font-size:18px;color:var(--text-muted)">↓</div>
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #7c6aff">2. Entwurf</div>
    <div style="text-align:center;font-size:18px;color:var(--text-muted)">↓</div>
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #ffa047">3. Implementierung</div>
    <div style="text-align:center;font-size:18px;color:var(--text-muted)">↓</div>
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #ff4f6a">4. Test</div>
    <div style="text-align:center;font-size:18px;color:var(--text-muted)">↓</div>
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #4de8b2">5. Einführung</div>
    <div style="text-align:center;font-size:18px;color:var(--text-muted)">↓</div>
    <div class="wf-phase" style="padding:10px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .15s;border-left:3px solid #f472b6">6. Wartung</div>
  </div>
  <div id="viz-t10-detail" style="padding:14px;background:var(--bg-code);border-radius:8px;font-size:13px;color:var(--text-secondary);min-height:60px">
    ← Klicke auf eine Phase
  </div>
</div>
""",

11: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Klasse → Objekt -->
<div class="viz-box">
  <div class="viz-title">Klasse instanziieren – new Schueler(...)</div>
  <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start">
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:8px">KLASSE (Bauplan)</div>
      <div class="uml-box" style="min-width:170px">
        <div class="uml-class-name">Schueler</div>
        <div class="uml-section">
          <span class="uml-private">- name: String</span><br>
          <span class="uml-private">- alter: int</span><br>
          <span class="uml-private">- note: double</span>
        </div>
        <div class="uml-section">
          <span class="uml-public">+ getName()</span><br>
          <span class="uml-public">+ begruesse()</span>
        </div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px;align-self:center">
      <input id="viz-t11-name"  class="viz-input" type="text"   placeholder="Name"  value="Hannah" style="width:120px">
      <input id="viz-t11-alter" class="viz-input" type="number" placeholder="Alter" value="17"     style="width:120px">
      <input id="viz-t11-note"  class="viz-input" type="number" placeholder="Note"  value="1.7" step="0.1" style="width:120px">
      <button id="viz-t11-new-btn" class="viz-btn">new ▶</button>
    </div>
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:8px">OBJEKT (Instanz)</div>
      <div id="viz-t11-obj" class="uml-box" style="min-width:200px;opacity:.4">
        <div class="uml-class-name">Schueler@????</div>
        <div class="uml-section"><span class="uml-private">– noch nicht erstellt –</span></div>
      </div>
    </div>
  </div>
</div>

<!-- VIZ 2: Polymorphismus -->
<div class="viz-box">
  <div class="viz-title">Polymorphismus – lautGeben() auf verschiedenen Objekten</div>
  <p class="viz-note">Klicke auf "Nächstes Tier" – obwohl alle vom Typ Tier sind, wird die richtige Methode aufgerufen.</p>
  <div id="viz-t11-poly-arena" style="display:flex;gap:16px;flex-wrap:wrap;margin:14px 0;align-items:flex-end">
    <div class="poly-item" style="text-align:center;position:relative">
      <div class="poly-bubble" style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);background:var(--bg-panel);border:1px solid #ffa047;border-radius:6px;padding:2px 8px;font-family:var(--font-code);font-size:11px;color:#ffa047;white-space:nowrap;opacity:0;transition:all .3s">Wau!</div>
      <div style="font-size:32px">🐕</div><div style="font-size:11px;color:var(--text-muted)">Hund</div>
    </div>
    <div class="poly-item" style="text-align:center;position:relative">
      <div class="poly-bubble" style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);background:var(--bg-panel);border:1px solid #a78bfa;border-radius:6px;padding:2px 8px;font-family:var(--font-code);font-size:11px;color:#a78bfa;white-space:nowrap;opacity:0;transition:all .3s">Miau!</div>
      <div style="font-size:32px">🐈</div><div style="font-size:11px;color:var(--text-muted)">Katze</div>
    </div>
    <div class="poly-item" style="text-align:center;position:relative">
      <div class="poly-bubble" style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);background:var(--bg-panel);border:1px solid #38bdf8;border-radius:6px;padding:2px 8px;font-family:var(--font-code);font-size:11px;color:#38bdf8;white-space:nowrap;opacity:0;transition:all .3s">Piep!</div>
      <div style="font-size:32px">🐦</div><div style="font-size:11px;color:var(--text-muted)">Vogel</div>
    </div>
    <div class="poly-item" style="text-align:center;position:relative">
      <div class="poly-bubble" style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);background:var(--bg-panel);border:1px solid #ffa047;border-radius:6px;padding:2px 8px;font-family:var(--font-code);font-size:11px;color:#ffa047;white-space:nowrap;opacity:0;transition:all .3s">Wau!</div>
      <div style="font-size:32px">🐕</div><div style="font-size:11px;color:var(--text-muted)">Hund</div>
    </div>
    <div class="poly-item" style="text-align:center;position:relative">
      <div class="poly-bubble" style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);background:var(--bg-panel);border:1px solid #a78bfa;border-radius:6px;padding:2px 8px;font-family:var(--font-code);font-size:11px;color:#a78bfa;white-space:nowrap;opacity:0;transition:all .3s">Miau!</div>
      <div style="font-size:32px">🐈</div><div style="font-size:11px;color:var(--text-muted)">Katze</div>
    </div>
  </div>
  <button id="viz-t11-poly-btn" class="viz-btn">Nächstes Tier ▶</button>
</div>
""",

12: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Struktogramm-Trace -->
<div class="viz-box">
  <div class="viz-title">Struktogramm-Trace – Summe 1 bis n</div>
  <p class="viz-note">Wähle n, klicke "Aufbauen" – dann Schritt für Schritt vor und zurück navigieren.</p>
  <div class="viz-row">
    <span class="viz-label">n:</span>
    <input id="viz-t12-trace-n" class="viz-input" type="number" min="1" max="10" value="4" style="width:70px">
    <button id="viz-t12-build-btn" class="viz-btn">Aufbauen</button>
  </div>
  <div style="margin-top:16px;font-family:var(--font-code);font-size:13px">
    <div class="struk-row" style="border:1px solid var(--border);border-radius:4px;padding:8px 12px;margin:2px 0;transition:background .2s,border-color .2s">
      Lies n &nbsp;·&nbsp; summe = 0 &nbsp;·&nbsp; i = 1
    </div>
    <div class="struk-row" style="border:1px solid var(--border);border-radius:4px;padding:8px 12px 8px 24px;margin:2px 0;border-left:4px solid var(--active);transition:background .2s,border-color .2s">
      SOLANGE i ≤ n: &nbsp; summe = summe + i &nbsp;·&nbsp; i = i + 1
    </div>
    <div class="struk-row" style="border:1px solid var(--border);border-radius:4px;padding:8px 12px;margin:2px 0;transition:background .2s,border-color .2s">
      Ausgabe: summe
    </div>
  </div>
  <div class="viz-row" style="margin-top:10px">
    <span class="viz-label">Variablen:</span>
    <span id="viz-t12-vars" class="viz-result" style="font-size:12px;font-weight:500"></span>
  </div>
  <div class="viz-nav">
    <button id="viz-t12-prev-btn" class="viz-btn viz-btn-ghost" disabled>◀ Zurück</button>
    <span   id="viz-t12-counter"  class="viz-step-counter">–</span>
    <button id="viz-t12-next-btn" class="viz-btn">Weiter ▶</button>
    <button id="viz-t12-reset-btn" class="viz-btn viz-btn-ghost">↺ Reset</button>
  </div>
</div>
<style>
  .struk-active { background: color-mix(in srgb, var(--active) 12%, var(--bg-card)) !important; border-color: var(--active) !important; color: var(--text-primary); }
</style>
""",

13: """
<h2>Interaktive Visualisierungen</h2>

<!-- VIZ 1: Sortier-Rennen -->
<div class="viz-box">
  <div class="viz-title">Sortier-Rennen – 4 Algorithmen gleichzeitig</div>
  <p class="viz-note">
    <span style="color:#ffa047">■</span> Vergleich &nbsp;
    <span style="color:#ff4f6a">■</span> Tausch &nbsp;
    <span style="color:#4de8b2">■</span> Fertig
  </p>
  <div class="viz-nav" style="margin-bottom:16px">
    <button id="viz-t13-build-btn" class="viz-btn">▶ Simulation starten</button>
    <button id="viz-t13-prev-btn"  class="viz-btn viz-btn-ghost" disabled>◀ Zurück</button>
    <span   id="viz-t13-counter"   class="viz-step-counter">– (Simulation starten)</span>
    <button id="viz-t13-next-btn"  class="viz-btn">Weiter ▶</button>
    <button id="viz-t13-auto-btn"  class="viz-btn viz-btn-ghost">⏩ Auto</button>
    <button id="viz-t13-new-btn"   class="viz-btn viz-btn-ghost">↺ Neues Array</button>
  </div>
  <div class="viz-speed-row">
    <span>Geschwindigkeit:</span>
    <input id="viz-t13-speed" class="viz-range" type="range" min="1" max="100" value="60" style="width:120px">
    <span>schnell</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px">
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:6px;font-weight:600">Insertion Sort</div>
      <div id="viz-t13-arena-ins"   class="sort-arena"></div>
      <div id="viz-t13-stats-ins"   class="sort-stats">Vergleiche: <span>0</span>&nbsp;&nbsp;Tausche: <span>0</span></div>
    </div>
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:6px;font-weight:600">Selection Sort</div>
      <div id="viz-t13-arena-sel"   class="sort-arena"></div>
      <div id="viz-t13-stats-sel"   class="sort-stats">Vergleiche: <span>0</span>&nbsp;&nbsp;Tausche: <span>0</span></div>
    </div>
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:6px;font-weight:600">Quicksort</div>
      <div id="viz-t13-arena-quick" class="sort-arena"></div>
      <div id="viz-t13-stats-quick" class="sort-stats">Vergleiche: <span>0</span>&nbsp;&nbsp;Tausche: <span>0</span></div>
    </div>
    <div>
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:6px;font-weight:600">Mergesort</div>
      <div id="viz-t13-arena-merge" class="sort-arena"></div>
      <div id="viz-t13-stats-merge" class="sort-stats">Vergleiche: <span>0</span>&nbsp;&nbsp;Tausche: <span>0</span></div>
    </div>
  </div>
</div>

<!-- VIZ 2: O-Notation -->
<div class="viz-box">
  <div class="viz-title">O-Notation – Laufzeitwachstum</div>
  <div class="viz-row">
    <span class="viz-label">n = <span id="viz-t13-n-val">50</span>:</span>
    <input id="viz-t13-n-sl" class="viz-range" type="range" min="5" max="150" value="50" style="flex:1">
  </div>
  <canvas id="viz-t13-canvas" class="viz-canvas" style="margin-top:12px;height:220px"></canvas>
</div>
""",
}

# ─────────────────────────────────────────────────────────────────────────────
# Klausurvorbereitung visualizations – keyed by string 'k1', 'k2', …
# ─────────────────────────────────────────────────────────────────────────────
VIZUALIZATIONS_KLAUSUR = {

'k1': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">Kino-Wochenprogramm – 2D-Array als Heatmap</div>
  <p class="viz-note">Klicke auf eine Zeile (= einen Film), um die Wochensumme und den besten Tag hervorzuheben.</p>
  <div id="viz-k1-grid" style="overflow-x:auto;margin-bottom:16px;"></div>
  <div id="viz-k1-info" style="background:var(--bg-code);border-radius:8px;padding:14px;font-family:var(--font-code);font-size:13px;min-height:52px;color:var(--text-secondary);">← Klicke auf einen Film</div>
  <div style="margin-top:12px;">
    <button class="viz-btn" onclick="resetKlausur1()">↺ Auswahl zurücksetzen</button>
  </div>
</div>
""",

}

# ─────────────────────────────────────────────────────────────────────────────
# Praktikum visualizations – keyed by string 'p1' .. 'p11'
# ─────────────────────────────────────────────────────────────────────────────
VIZUALIZATIONS_PRAKTIKUM = {

'p2': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">Datentypen – Wertebereich &amp; Speicher</div>
  <p class="viz-note">Klicke auf einen Datentyp, um Speichergröße, Wertebereich und ein Beispiel zu sehen.</p>
  <div id="viz-p2-types" style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px;"></div>
  <div id="viz-p2-detail" style="background:var(--bg-code);border-radius:10px;padding:16px;min-height:80px;font-family:var(--font-mono);font-size:13px;color:var(--text-primary);"></div>
</div>
""",

'p4': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">if / else – Ablaufverfolgung</div>
  <p class="viz-note">Stelle den eingeworfenen Betrag ein und verfolge welcher Zweig ausgeführt wird.</p>
  <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:16px;">
    <label style="font-size:13px;color:var(--text-secondary);">Betrag (EUR):</label>
    <input id="viz-p4-betrag" type="range" min="0" max="3" step="0.10" value="1.00"
           style="width:180px;" oninput="updateP4Viz()">
    <span id="viz-p4-betrag-val" style="font-family:var(--font-mono);font-size:14px;font-weight:700;color:var(--active);min-width:50px;">1.00</span>
    <span style="font-size:12px;color:var(--text-secondary);">Preis: 1.50 EUR</span>
  </div>
  <div id="viz-p4-branches" style="display:flex;gap:12px;flex-wrap:wrap;"></div>
</div>
""",

'p5': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">switch – Welcher case wird aktiv?</div>
  <p class="viz-note">Wähle eine Nummer und sieh, welcher case im switch aufleuchtet.</p>
  <div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">
    <button class="viz-btn" onclick="setP5(1)">1 – Cola</button>
    <button class="viz-btn" onclick="setP5(2)">2 – Apfelschorle</button>
    <button class="viz-btn" onclick="setP5(3)">3 – Wasser</button>
    <button class="viz-btn" onclick="setP5(4)">4 – Eistee</button>
    <button class="viz-btn" onclick="setP5(5)">5 – Limo</button>
    <button class="viz-btn" onclick="setP5(9)">9 – (default)</button>
  </div>
  <div id="viz-p5-cases" style="font-family:var(--font-mono);font-size:13px;line-height:2;"></div>
</div>
""",

'p6': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">Array – Zellen und Index</div>
  <p class="viz-note">Klicke "Schritt" um die for-Schleife durchzugehen. Der aktuelle Index wird hervorgehoben.</p>
  <div id="viz-p6-cells" style="display:flex;gap:6px;margin-bottom:16px;flex-wrap:wrap;"></div>
  <div id="viz-p6-info" style="font-family:var(--font-mono);font-size:13px;color:var(--text-secondary);margin-bottom:12px;min-height:20px;"></div>
  <div style="display:flex;gap:10px;">
    <button class="viz-btn" onclick="stepP6()">Schritt →</button>
    <button class="viz-btn" onclick="resetP6()">Reset</button>
  </div>
</div>
""",

'p7': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">while-Schleife – Durchläufe verfolgen</div>
  <p class="viz-note">Münzen werden simuliert eingeworfen. Verfolge wie der Betrag wächst.</p>
  <div id="viz-p7-log" style="font-family:var(--font-mono);font-size:12px;line-height:1.9;max-height:200px;overflow-y:auto;background:var(--bg-code);border-radius:8px;padding:12px;margin-bottom:12px;"></div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;">
    <button class="viz-btn" onclick="addCoinP7(0.50)">+ 0,50 €</button>
    <button class="viz-btn" onclick="addCoinP7(1.00)">+ 1,00 €</button>
    <button class="viz-btn" onclick="addCoinP7(2.00)">+ 2,00 €</button>
    <button class="viz-btn" onclick="stopP7()">Fertig (0)</button>
    <button class="viz-btn" onclick="resetP7()">Reset</button>
  </div>
  <div id="viz-p7-total" style="margin-top:12px;font-size:15px;font-weight:700;color:var(--active);"></div>
</div>
""",

'p8': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">Methoden – Call Stack</div>
  <p class="viz-note">Sieh wie Methoden aufgerufen werden und der Stack wächst und schrumpft.</p>
  <div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">
    <button class="viz-btn" onclick="callP8('zeigeMenu')">zeigeMenu()</button>
    <button class="viz-btn" onclick="callP8('addiereMuenze')">addiereMuenze(1.00, 0.50)</button>
    <button class="viz-btn" onclick="callP8('gibNachricht')">gibNachricht(1.50, 1.50)</button>
    <button class="viz-btn" onclick="resetP8()">Reset</button>
  </div>
  <div id="viz-p8-stack" style="font-family:var(--font-mono);font-size:13px;"></div>
</div>
""",

'p10': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">Klasse → Objekte instanziieren</div>
  <p class="viz-note">Klicke auf "new Getraenk(...)" um ein neues Objekt zu erzeugen und im Speicher zu sehen.</p>
  <div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">
    <button class="viz-btn" onclick="newGetraenk('Cola', 1.50, 5)">new Getraenk("Cola", 1.50, 5)</button>
    <button class="viz-btn" onclick="newGetraenk('Wasser', 1.00, 3)">new Getraenk("Wasser", 1.00, 3)</button>
    <button class="viz-btn" onclick="newGetraenk('Limo', 1.30, 2)">new Getraenk("Limo", 1.30, 2)</button>
    <button class="viz-btn" onclick="resetP10()">Reset</button>
  </div>
  <div style="display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start;">
    <div>
      <div style="font-size:11px;color:var(--text-secondary);margin-bottom:6px;">BAUPLAN (Klasse)</div>
      <div id="viz-p10-blueprint" style="background:var(--bg-code);border-radius:8px;padding:12px;font-family:var(--font-mono);font-size:12px;min-width:200px;border:2px solid var(--active);"></div>
    </div>
    <div style="font-size:20px;color:var(--text-secondary);padding-top:30px;">→</div>
    <div>
      <div style="font-size:11px;color:var(--text-secondary);margin-bottom:6px;">OBJEKTE (Instanzen)</div>
      <div id="viz-p10-objects" style="display:flex;flex-direction:column;gap:10px;"></div>
    </div>
  </div>
</div>
""",

'p11': """
<h2>Interaktive Visualisierung</h2>
<div class="viz-box">
  <div class="viz-title">UML-Klassendiagramm – Getränkeautomat</div>
  <p class="viz-note">Klicke auf eine Klasse um ihre Attribute und Methoden zu sehen.</p>
  <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px;">
    <button class="viz-btn" onclick="showP11Class('Getraenk')">Getraenk</button>
    <button class="viz-btn" onclick="showP11Class('Geldfach')">Geldfach</button>
    <button class="viz-btn" onclick="showP11Class('Automat')">Automat</button>
  </div>
  <div id="viz-p11-detail" style="background:var(--bg-code);border-radius:10px;padding:16px;font-family:var(--font-mono);font-size:13px;min-height:120px;"></div>
</div>
""",
}

# ─────────────────────────────────────────────────────────────────────────────
# Also inject 32 bit-cells for IEEE viz on page load
# ─────────────────────────────────────────────────────────────────────────────
IEEE_BIT_INIT = """
<script>
(function(){
  const el = document.getElementById('viz-t4-ieee-bits');
  if (!el) return;
  for (let i=0;i<32;i++){
    const c = document.createElement('div');
    c.className = 'bit-cell';
    c.textContent = '0';
    c.style.width='22px'; c.style.height='22px'; c.style.fontSize='11px'; c.style.borderRadius='4px';
    el.appendChild(c);
  }
})();
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
def sidebar_html(active_num):
    # Theory items
    theory_items = []
    for num, title, color, slug, _ in TOPICS:
        active_cls = " active" if num == active_num else ""
        theory_items.append(f'''
    <li class="nav-item{active_cls}" data-c="{num}">
      <a href="{slug}.html">
        <span class="nav-num">{num:02d}</span>
        {htmlmod.escape(title)}
      </a>
    </li>''')
    # Praktikum items
    praxis_items = []
    for num, title, color, slug, _ in PRAKTIKUM:
        active_cls = " active" if f'p{num}' == active_num else ""
        praxis_items.append(f'''
    <li class="nav-item{active_cls}" data-c="{num}">
      <a href="{slug}.html">
        <span class="nav-num">{num:02d}</span>
        {htmlmod.escape(title)}
      </a>
    </li>''')
    # Klausurvorbereitung items
    klausur_items = []
    for key, title, color, slug, _ in KLAUSUR:
        active_cls = " active" if key == active_num else ""
        klausur_items.append(f'''
    <li class="nav-item{active_cls}" data-c="9">
      <a href="{slug}.html">
        <span class="nav-num">K</span>
        {htmlmod.escape(title)}
      </a>
    </li>''')
    theory_nav  = "\n".join(theory_items)
    praxis_nav  = "\n".join(praxis_items)
    klausur_nav = "\n".join(klausur_items)
    return f'''<aside class="sidebar">
  <div class="sidebar-header">
    <a href="index.html" class="sidebar-home-link">
      <div class="sidebar-logo">LK Informatik</div>
      <div class="sidebar-title">Hannah&#39;s Skript</div>
    </a>
    <div class="sidebar-subtitle">Gymnasium J2 &middot; 13 Themen + Praktikum</div>
    <div class="theme-toggle" id="themeToggle" role="button" tabindex="0" aria-label="Theme wechseln">
      <span class="toggle-icons">🌙</span>
      <div class="toggle-track"><div class="toggle-thumb"></div></div>
      <span class="toggle-label">Dark Mode</span>
    </div>
  </div>
  <div class="nav-section-label">Themenübersicht</div>
  <ul class="nav-list">{theory_nav}
  </ul>
  <div class="nav-section-label">Praktikum</div>
  <ul class="nav-list">{praxis_nav}
  </ul>
  <div class="nav-section-label">Klausurvorbereitung</div>
  <ul class="nav-list">{klausur_nav}
  </ul>
</aside>'''

# ─────────────────────────────────────────────────────────────────────────────
def md_to_html(md_text):
    lines = md_text.split('\n')
    out = []
    i = 0
    in_pre = False
    pre_lines = []

    def flush_pre():
        nonlocal pre_lines
        code = htmlmod.escape('\n'.join(pre_lines))
        pre_lines = []
        return f'<div class="code-wrap"><button class="copy-btn" onclick="copyCode(this)">Kopieren</button><pre>{code}</pre></div>'

    def inline(s):
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'`([^`]+)`', lambda m: f'<code>{htmlmod.escape(m.group(1))}</code>', s)
        return s

    while i < len(lines):
        line = lines[i]
        # Progress box: :::progress-box ... :::
        if line.strip() == ':::progress-box':
            box_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != ':::':
                box_lines.append(lines[i])
                i += 1
            i += 1  # skip closing :::
            inner = '<br>'.join(inline(l) for l in box_lines if l.strip())
            out.append(f'<div class="progress-box">{inner}</div>')
            continue
        if line.strip().startswith('```'):
            if in_pre:
                out.append(flush_pre())
                in_pre = False
            else:
                in_pre = True
            i += 1
            continue
        if in_pre:
            pre_lines.append(line)
            i += 1
            continue
        if re.match(r'^-{3,}$', line.strip()):
            out.append('<hr>')
            i += 1
            continue
        if line.startswith('#### '):
            out.append(f'<h4>{inline(line[5:])}</h4>')
            i += 1
            continue
        if line.startswith('### '):
            out.append(f'<h3>{inline(line[4:])}</h3>')
            i += 1
            continue
        if line.startswith('## '):
            out.append(f'<h2>{inline(line[3:])}</h2>')
            i += 1
            continue
        if line.startswith('# '):
            i += 1
            continue
        if '|' in line and i + 1 < len(lines) and re.match(r'[\s|:-]+', lines[i+1]):
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            # Split on '|', strip each cell, but drop only the empty strings
            # produced by the leading and trailing '|' delimiters — not inner empty cells.
            raw_header = table_lines[0].split('|')
            header_row = [c.strip() for c in raw_header[1:-1]]  # keep empty inner cells
            body_rows  = []
            for tl in table_lines[2:]:
                raw = tl.split('|')
                cols = [c.strip() for c in raw[1:-1]]
                if any(c for c in cols):  # skip blank separator lines
                    body_rows.append(cols)
            ths = ''.join(f'<th>{inline(h)}</th>' for h in header_row)
            trs = ''
            for row in body_rows:
                cells = ''.join(f'<td>{inline(c)}</td>' for c in row)
                trs += f'<tr>{cells}</tr>'
            out.append(f'<div class="table-wrap"><table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>')
            continue
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                items.append(f'<li>{inline(lines[i][2:])}</li>')
                i += 1
            out.append('<ul>' + ''.join(items) + '</ul>')
            continue
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                txt = re.sub(r'^\d+\. ', '', lines[i])
                items.append(f'<li>{inline(txt)}</li>')
                i += 1
            out.append('<ol>' + ''.join(items) + '</ol>')
            continue
        if not line.strip():
            i += 1
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() \
              and not lines[i].startswith('#') \
              and not lines[i].startswith('```') \
              and not re.match(r'^-{3,}$', lines[i].strip()) \
              and '|' not in lines[i] \
              and not re.match(r'^[-*] ', lines[i]) \
              and not re.match(r'^\d+\. ', lines[i]):
            para.append(lines[i])
            i += 1
        out.append(f'<p>{inline(" ".join(para))}</p>')

    if in_pre:
        out.append(flush_pre())
    return '\n'.join(out)

# ─────────────────────────────────────────────────────────────────────────────
def build_page(num, title, color_var, slug, subtitle, body_html, viz_html):
    active_css = f':root {{ --active: var({color_var}); }}'
    is_praktikum = isinstance(num, str) and num.startswith('p')
    is_klausur   = isinstance(num, str) and num.startswith('k')

    if is_praktikum:
        p_idx = int(num[1:])
        prev_slug = PRAKTIKUM[p_idx-2][3] if p_idx > 1 else None
        next_slug = PRAKTIKUM[p_idx][3]   if p_idx < len(PRAKTIKUM) else None
        prev_title = PRAKTIKUM[p_idx-2][1] if p_idx > 1 else None
        next_title = PRAKTIKUM[p_idx][1]   if p_idx < len(PRAKTIKUM) else None
        badge_text = f'Praktikum {p_idx:02d}'
        of_text    = f'Schritt {p_idx} von {len(PRAKTIKUM)}'
        title_tag  = f'Praktikum {p_idx:02d} – {htmlmod.escape(title)} | LK Informatik'
    elif is_klausur:
        k_idx = int(num[1:])
        prev_slug  = None
        next_slug  = None
        prev_title = None
        next_title = None
        badge_text = f'Klausurvorbereitung'
        of_text    = f'Übung {k_idx}'
        title_tag  = f'Klausurvorbereitung – {htmlmod.escape(title)} | LK Informatik'
    else:
        prev_slug  = TOPICS[num-2][3] if num > 1  else None
        next_slug  = TOPICS[num][3]   if num < 13 else None
        prev_title = TOPICS[num-2][1] if num > 1  else None
        next_title = TOPICS[num][1]   if num < 13 else None
        badge_text = f'Thema {num:02d}'
        of_text    = f'Thema {num} von 13'
        title_tag  = f'Thema {num:02d} – {htmlmod.escape(title)} | LK Informatik'

    nav_links = '<div class="page-nav">'
    if prev_slug:
        nav_links += f'<a href="{prev_slug}.html" class="nav-btn nav-prev">← {htmlmod.escape(prev_title)}</a>'
    else:
        nav_links += '<span></span>'
    if next_slug:
        nav_links += f'<a href="{next_slug}.html" class="nav-btn nav-next">{htmlmod.escape(next_title)} →</a>'
    nav_links += '</div>'

    meta_parts = subtitle.split(' · ')
    meta_html  = ' <span class="meta-dot"></span> '.join(f'<span>{htmlmod.escape(p)}</span>' for p in meta_parts)
    sidebar    = sidebar_html(num)

    extra_init = IEEE_BIT_INIT if num == 4 else ''

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_tag}</title>
<link rel="stylesheet" href="lk-style.css">
<link rel="stylesheet" href="lk-viz.css">
<style>
{active_css}
.page-nav {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 52px;
  padding-top: 28px;
  border-top: 1px solid var(--border);
  gap: 16px;
}}
.nav-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-secondary);
  text-decoration: none;
  padding: 9px 16px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg-panel);
  transition: border-color .15s, color .15s, background .15s;
}}
.nav-btn:hover {{
  color: var(--active);
  border-color: var(--active);
  background: color-mix(in srgb, var(--active) 6%, var(--bg-panel));
}}
.wf-phase {{ font-size:14px; color:var(--text-secondary); font-family:var(--font-ui); }}
.wf-phase.active {{ background: color-mix(in srgb, var(--active) 10%, var(--bg-card)) !important; color: var(--active) !important; }}
</style>
</head>
<body>
<div id="progress"></div>
{sidebar}
<main class="main">
  <div class="topbar">
    <span class="topbar-badge">{badge_text}</span>
    <span class="topbar-title">{htmlmod.escape(title)}</span>
    <span class="topbar-spacer"></span>
    <span class="topbar-lk">LK Informatik</span>
  </div>
  <div class="content">
    <h1>{htmlmod.escape(title)}</h1>
    <div class="meta">
      <span>{of_text}</span>
      <span class="meta-dot"></span>
      {meta_html}
    </div>
{body_html}
{viz_html}
{nav_links}
  </div>
</main>
{extra_init}
<script src="lk-script.js"></script>
<script src="lk-viz.js"></script>
</body>
</html>'''

# ─────────────────────────────────────────────────────────────────────────────
def main():
    built = 0
    total = len(TOPICS) + len(PRAKTIKUM) + len(KLAUSUR)

    # Build theory pages
    for num, title, color_var, slug, subtitle in TOPICS:
        md_path   = os.path.join(BASE, f'{slug}.md')
        html_path = os.path.join(BASE, f'{slug}.html')
        if not os.path.exists(md_path):
            print(f'  SKIP  {slug}.md  (not found)')
            continue
        with open(md_path, encoding='utf-8') as f:
            md_text = f.read()
        md_body   = re.split(r'##\s+Gesamteinsch[äa]tzung', md_text)[0]
        body_html = md_to_html(md_body)
        viz_html  = VIZUALIZATIONS.get(num, '')
        page = build_page(num, title, color_var, slug, subtitle, body_html, viz_html)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page)
        print(f'  OK    {slug}.html')
        built += 1

    # Build Praktikum pages
    for num, title, color_var, slug, subtitle in PRAKTIKUM:
        pkey      = f'p{num}'
        md_path   = os.path.join(BASE, f'{slug}.md')
        html_path = os.path.join(BASE, f'{slug}.html')
        if not os.path.exists(md_path):
            print(f'  SKIP  {slug}.md  (not found)')
            continue
        with open(md_path, encoding='utf-8') as f:
            md_text = f.read()
        body_html = md_to_html(md_text)
        viz_html  = VIZUALIZATIONS_PRAKTIKUM.get(pkey, '')
        page = build_page(pkey, title, color_var, slug, subtitle, body_html, viz_html)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page)
        print(f'  OK    {slug}.html')
        built += 1

    # Build Klausurvorbereitung pages
    for key, title, color_var, slug, subtitle in KLAUSUR:
        md_path   = os.path.join(BASE, f'{slug}.md')
        html_path = os.path.join(BASE, f'{slug}.html')
        if not os.path.exists(md_path):
            print(f'  SKIP  {slug}.md  (not found)')
            continue
        with open(md_path, encoding='utf-8') as f:
            md_text = f.read()
        body_html = md_to_html(md_text)
        viz_html  = VIZUALIZATIONS_KLAUSUR.get(key, '')
        page = build_page(key, title, color_var, slug, subtitle, body_html, viz_html)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page)
        print(f'  OK    {slug}.html')
        built += 1

    print(f'\n✓ {built}/{total} Seiten erstellt.')

if __name__ == '__main__':
    main()
