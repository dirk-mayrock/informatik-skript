#!/usr/bin/env python3
"""
Generates all 13 LK Informatik HTML pages from their .md source files.
Run from the hannah_script directory.
"""

import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Thema metadata ────────────────────────────────────────────────────────────
TOPICS = [
    (1,  "Binär- & Hexadezimalzahlen",    "--c1",  "Thema1_Binaer_und_Hexadezimalzahlen",                "Zahlensysteme · Grundlagen"),
    (2,  "Binäre Arithmetik",             "--c2",  "Thema2_Binaere_Arithmetik_V2",                        "Rechnen · ALU"),
    (3,  "Einer- & Zweierkomplement",     "--c3",  "Thema3_Einer_und_Zweierkomplement",                   "Negative Zahlen · Vorzeichen"),
    (4,  "Fest- & Gleitkommazahlen",      "--c4",  "Thema4_Fest_und_Gleitkommazahlen",                    "IEEE 754 · Kommazahlen"),
    (5,  "Nachricht & Information",       "--c5",  "Thema5_Nachricht_Information_Nachrichtentraeger",      "Shannon · Entropie · Codierung"),
    (6,  "Datenkompression",              "--c6",  "Thema6_Datenkompression",                              "Huffman · LZW · RLE · Delta"),
    (7,  "Hashing",                       "--c7",  "Thema7_Hashing",                                      "Hashtabellen · SHA · Kollisionen"),
    (8,  "Hamming-Codes",                 "--c8",  "Thema8_Hamming_Codes",                                "Fehlerkorrektur · Parität"),
    (9,  "Java-Grundlagen",               "--c9",  "Thema9_Java_Grundlagen",                              "Syntax · Typen · Methoden"),
    (10, "Softwareentwicklung",           "--c10", "Thema10_Softwareentwicklung_Wasserfallmodell",         "Wasserfallmodell · Agil · Scrum"),
    (11, "Objektorientierung",            "--c11", "Thema11_Objektorientierung",                           "OOP · Klassen · Vererbung"),
    (12, "Struktogramme",                 "--c12", "Thema12_Struktogramme_und_Ablaufplaene",               "Nassi-Shneiderman · Flussdiagramm"),
    (13, "Sortieralgorithmen",            "--c13", "Thema13_Sortieralgorithmen",                           "Quicksort · Mergesort · O-Notation"),
]

# ── Sidebar HTML (shared) ─────────────────────────────────────────────────────
def sidebar_html(active_num):
    items = []
    for num, title, color, slug, _ in TOPICS:
        active_cls = " active" if num == active_num else ""
        items.append(f'''
    <li class="nav-item{active_cls}" data-c="{num}">
      <a href="{slug}.html">
        <span class="nav-num">{num:02d}</span>
        {htmlmod.escape(title)}
      </a>
    </li>''')
    nav = "\n".join(items)
    return f'''<aside class="sidebar">
  <div class="sidebar-header">
    <div class="sidebar-logo">LK Informatik</div>
    <div class="sidebar-title">Hannah's Skript</div>
    <div class="sidebar-subtitle">Gymnasium J2 &middot; 13 Themen</div>
    <div class="theme-toggle" id="themeToggle" role="button" tabindex="0" aria-label="Theme wechseln">
      <span class="toggle-icons">🌙</span>
      <div class="toggle-track"><div class="toggle-thumb"></div></div>
      <span class="toggle-label">Dark Mode</span>
    </div>
  </div>
  <div class="nav-section-label">Themenübersicht</div>
  <ul class="nav-list">{nav}
  </ul>
</aside>'''

# ── Markdown → HTML converter (lightweight) ──────────────────────────────────
def md_to_html(md_text):
    """Convert the .md files to HTML content blocks."""
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
        # Bold
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        # Inline code
        s = re.sub(r'`([^`]+)`', lambda m: f'<code>{htmlmod.escape(m.group(1))}</code>', s)
        return s

    while i < len(lines):
        line = lines[i]

        # Fenced code block start
        if line.strip().startswith('```'):
            if in_pre:
                # end
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

        # HR
        if re.match(r'^-{3,}$', line.strip()):
            out.append('<hr>')
            i += 1
            continue

        # H4
        if line.startswith('#### '):
            out.append(f'<h4>{inline(line[5:])}</h4>')
            i += 1
            continue

        # H3
        if line.startswith('### '):
            out.append(f'<h3>{inline(line[4:])}</h3>')
            i += 1
            continue

        # H2
        if line.startswith('## '):
            out.append(f'<h2>{inline(line[3:])}</h2>')
            i += 1
            continue

        # H1 — skip the document title (used in topbar/h1 separately)
        if line.startswith('# '):
            i += 1
            continue

        # Table
        if '|' in line and i + 1 < len(lines) and re.match(r'[\s|:-]+', lines[i+1]):
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            # parse
            header_row = [c.strip() for c in table_lines[0].split('|') if c.strip()]
            body_rows  = []
            for tl in table_lines[2:]:
                cols = [c.strip() for c in tl.split('|') if c.strip()]
                if cols:
                    body_rows.append(cols)
            ths = ''.join(f'<th>{inline(h)}</th>' for h in header_row)
            trs = ''
            for row in body_rows:
                cells = ''.join(f'<td>{inline(c)}</td>' for c in row)
                trs += f'<tr>{cells}</tr>'
            out.append(f'<div class="table-wrap"><table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>')
            continue

        # Unordered list
        if re.match(r'^[-*] ', line):
            items = []
            while i < len(lines) and re.match(r'^[-*] ', lines[i]):
                items.append(f'<li>{inline(lines[i][2:])}</li>')
                i += 1
            out.append('<ul>' + ''.join(items) + '</ul>')
            continue

        # Ordered list
        if re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                txt = re.sub(r'^\d+\. ', '', lines[i])
                items.append(f'<li>{inline(txt)}</li>')
                i += 1
            out.append('<ol>' + ''.join(items) + '</ol>')
            continue

        # Blank line
        if not line.strip():
            i += 1
            continue

        # Paragraph
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith('#') \
              and not lines[i].startswith('```') and not re.match(r'^-{3,}$', lines[i].strip()) \
              and '|' not in lines[i] and not re.match(r'^[-*] ', lines[i]) \
              and not re.match(r'^\d+\. ', lines[i]):
            para.append(lines[i])
            i += 1
        out.append(f'<p>{inline(" ".join(para))}</p>')

    if in_pre:
        out.append(flush_pre())

    return '\n'.join(out)


# ── Extract Gesamteinschätzung from MD ────────────────────────────────────────
def extract_rating(md_text):
    """Returns list of (label, score_int) or defaults."""
    defaults = [("Didaktik",9),("Fachliche Korrektheit",9),("LK-Niveau",9),("Verständlichkeit",9)]
    pattern = re.compile(r'\*\*(.*?)\*\*[:\s]+(\d+)\s*/\s*10')
    matches = pattern.findall(md_text)
    if len(matches) >= 4:
        return [(m[0], int(m[1])) for m in matches[-4:]]
    return defaults


# ── Full page template ────────────────────────────────────────────────────────
def build_page(num, title, color_var, slug, subtitle, body_html, ratings):
    active_css = f':root {{ --active: var({color_var}); }}'
    rating_items = ''
    for label, score in ratings:
        pct = score * 10
        rating_items += f'''
        <div class="rating-item">
          <div class="rating-label">
            <span>{htmlmod.escape(label)}</span>
            <span class="rating-score">{score} / 10</span>
          </div>
          <div class="rating-bar"><div class="rating-fill" data-val="{pct}"></div></div>
        </div>'''

    sidebar = sidebar_html(num)
    # prev / next links
    prev_slug = TOPICS[num-2][3] if num > 1 else None
    next_slug = TOPICS[num][3]   if num < 13 else None
    nav_links = '<div class="page-nav">'
    if prev_slug:
        prev_title = TOPICS[num-2][1]
        nav_links += f'<a href="{prev_slug}.html" class="nav-btn nav-prev">← {htmlmod.escape(prev_title)}</a>'
    else:
        nav_links += '<span></span>'
    if next_slug:
        next_title = TOPICS[num][1]
        nav_links += f'<a href="{next_slug}.html" class="nav-btn nav-next">{htmlmod.escape(next_title)} →</a>'
    nav_links += '</div>'

    meta_parts = subtitle.split(' · ')
    meta_html = ' <span class="meta-dot"></span> '.join(f'<span>{htmlmod.escape(p)}</span>' for p in meta_parts)

    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thema {num:02d} – {htmlmod.escape(title)} | LK Informatik</title>
<link rel="stylesheet" href="lk-style.css">
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
</style>
</head>
<body>
<div id="progress"></div>
{sidebar}
<main class="main">
  <div class="topbar">
    <span class="topbar-badge">Thema {num:02d}</span>
    <span class="topbar-title">{htmlmod.escape(title)}</span>
    <span class="topbar-spacer"></span>
    <span class="topbar-lk">LK Informatik</span>
  </div>
  <div class="content">
    <h1>{htmlmod.escape(title)}</h1>
    <div class="meta">
      <span>Thema {num} von 13</span>
      <span class="meta-dot"></span>
      {meta_html}
    </div>
{body_html}
    <div class="rating-card">
      <div class="rating-title">Gesamteinschätzung</div>
      <div class="rating-grid">{rating_items}
      </div>
    </div>
{nav_links}
  </div>
</main>
<script src="lk-script.js"></script>
</body>
</html>'''


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    built = 0
    for num, title, color_var, slug, subtitle in TOPICS:
        md_path   = os.path.join(BASE, f'{slug}.md')
        html_path = os.path.join(BASE, f'{slug}.html')

        if not os.path.exists(md_path):
            print(f'  SKIP  {slug}.md  (not found)')
            continue

        with open(md_path, encoding='utf-8') as f:
            md_text = f.read()

        # Strip the Gesamteinschätzung block from body (rendered separately)
        md_body = re.split(r'##\s+Gesamteinsch[äa]tzung', md_text)[0]
        ratings = extract_rating(md_text)

        body_html = md_to_html(md_body)
        page = build_page(num, title, color_var, slug, subtitle, body_html, ratings)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(page)

        print(f'  OK    {slug}.html')
        built += 1

    print(f'\n✓ {built}/{len(TOPICS)} Seiten erstellt.')

if __name__ == '__main__':
    main()
