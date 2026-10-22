/* lk-viz.js – Interactive visualizations for all 13 topics */

/* ══════════════════════════════════════════════════════════
   THEMA 1 – Binär & Hex
══════════════════════════════════════════════════════════ */

function initT1BitSchalter() {
  const el = document.getElementById('viz-t1-bits');
  if (!el) return;
  const bits = el.querySelectorAll('.bit-cell');
  const dec  = document.getElementById('viz-t1-dec');
  const hex  = document.getElementById('viz-t1-hex');
  function update() {
    let val = 0;
    bits.forEach((b, i) => { if (b.classList.contains('on')) val += (1 << (7 - i)); });
    dec.textContent = val;
    hex.textContent = '0x' + val.toString(16).toUpperCase().padStart(2,'0');
  }
  bits.forEach(b => b.addEventListener('click', () => { b.classList.toggle('on'); update(); }));
  update();
}

function initT1Division() {
  const btn = document.getElementById('viz-t1-div-btn');
  if (!btn) return;
  const inp   = document.getElementById('viz-t1-div-inp');
  const steps = document.getElementById('viz-t1-div-steps');
  const res   = document.getElementById('viz-t1-div-result');
  btn.addEventListener('click', () => {
    let n = parseInt(inp.value) || 0;
    if (n < 0 || n > 255) { res.textContent = 'Bitte 0–255 eingeben'; return; }
    steps.innerHTML = '';
    res.textContent = '';
    const rows = [];
    let tmp = n;
    if (tmp === 0) { rows.push({q:0,r:0}); }
    while (tmp > 0) { rows.push({q: Math.floor(tmp/2), r: tmp%2}); tmp = Math.floor(tmp/2); }
    const binary = n === 0 ? '0' : rows.map(r=>r.r).reverse().join('');
    rows.forEach((row, i) => {
      const orig = i === 0 ? n : rows[i-1].q;
      const div  = document.createElement('div');
      div.className = 'step-row';
      div.innerHTML = `<span class="step-val">${orig}</span><span class="step-arrow"> ÷ 2 = </span><span class="step-val">${row.q}</span><span class="step-arrow"> Rest </span><span class="step-rest">${row.r}</span>`;
      steps.appendChild(div);
      setTimeout(() => div.classList.add('visible'), i * 200);
    });
    setTimeout(() => {
      const div = document.createElement('div');
      div.className = 'step-row highlight';
      div.innerHTML = `<span class="step-arrow">↑ von unten lesen: </span><span class="step-rest">${binary}₂</span>`;
      steps.appendChild(div);
      setTimeout(() => div.classList.add('visible'), 100);
      res.textContent = n + '₁₀ = ' + binary + '₂';
    }, rows.length * 200 + 100);
  });
}

function initT1BinaryCounter() {
  const el = document.getElementById('viz-t1-counter');
  if (!el) return;
  const bits  = el.querySelectorAll('.bit-cell');
  const decEl = document.getElementById('viz-t1-cnt-dec');
  let val = 0, timer = null;
  function show(v) {
    bits.forEach((b, i) => {
      const on = !!(v & (1 << (3 - i)));
      b.classList.toggle('on', on);
    });
    if (decEl) decEl.textContent = v;
  }
  document.getElementById('viz-t1-cnt-start').addEventListener('click', () => {
    if (timer) return;
    timer = setInterval(() => { val = (val + 1) % 16; show(val); }, 500);
  });
  document.getElementById('viz-t1-cnt-stop').addEventListener('click', () => {
    clearInterval(timer); timer = null;
  });
  document.getElementById('viz-t1-cnt-reset').addEventListener('click', () => {
    clearInterval(timer); timer = null; val = 0; show(0);
  });
  show(0);
}

function initT1ColorMixer() {
  const el = document.getElementById('viz-t1-color');
  if (!el) return;
  const sliders = ['r','g','b'].map(c => document.getElementById('viz-t1-'+c));
  const preview = document.getElementById('viz-t1-preview');
  const hexOut  = document.getElementById('viz-t1-hexout');
  const binOuts = ['r','g','b'].map(c => document.getElementById('viz-t1-bin-'+c));
  function update() {
    const vals = sliders.map(s => parseInt(s.value));
    const hex  = '#' + vals.map(v => v.toString(16).padStart(2,'0').toUpperCase()).join('');
    if (preview) preview.style.background = hex;
    if (hexOut)  hexOut.textContent = hex;
    binOuts.forEach((b, i) => { if (b) b.textContent = vals[i].toString(2).padStart(8,'0'); });
  }
  sliders.forEach(s => s && s.addEventListener('input', update));
  update();
}

/* ══════════════════════════════════════════════════════════
   THEMA 2 – Binäre Arithmetik
══════════════════════════════════════════════════════════ */

function initT2Addition() {
  const btn = document.getElementById('viz-t2-add-btn');
  if (!btn) return;
  const aInp  = document.getElementById('viz-t2-a');
  const bInp  = document.getElementById('viz-t2-b');
  const arena = document.getElementById('viz-t2-arena');
  btn.addEventListener('click', () => {
    const a = parseInt(aInp.value, 2);
    const b = parseInt(bInp.value, 2);
    if (isNaN(a) || isNaN(b)) { arena.innerHTML = '<p style="color:#ff4f6a">Nur 0 und 1 eingeben!</p>'; return; }
    const sum = a + b;
    const aB  = a.toString(2).padStart(8,'0');
    const bB  = b.toString(2).padStart(8,'0');
    const sB  = sum.toString(2).padStart(9,'0');
    // show carries
    let carry = 0;
    const carries = [];
    for (let i = 7; i >= 0; i--) {
      const s = parseInt(aB[i]) + parseInt(bB[i]) + carry;
      carry = s >= 2 ? 1 : 0;
      carries.unshift(carry);
    }
    const carryStr = carries.map(c => c ? '<span class="sh-hi">'+c+'</span>' : '<span class="step-val">0</span>').join('');
    arena.innerHTML = `
      <div style="font-family:var(--font-code);font-size:14px;line-height:2">
        <div style="color:var(--text-muted);font-size:11px">Überträge: &nbsp;${carryStr}</div>
        <div>&nbsp;&nbsp;<span class="sh-num">${aB}</span> &nbsp;(${a})</div>
        <div>+ <span class="sh-num">${bB}</span> &nbsp;(${b})</div>
        <div style="border-top:1px solid var(--border);padding-top:4px">= <span class="sh-hi">${sB}</span> &nbsp;(${sum})</div>
        ${sum > 255 ? '<div style="color:#ff4f6a;margin-top:8px">⚠ Overflow! Ergebnis passt nicht in 8 Bit.</div>' : ''}
      </div>`;
  });
}

function initT2Bitshift() {
  const el = document.getElementById('viz-t2-shift');
  if (!el) return;
  const inp   = document.getElementById('viz-t2-shift-inp');
  const bits  = el.querySelectorAll('.bit-cell');
  const decEl = document.getElementById('viz-t2-shift-dec');
  const op    = document.getElementById('viz-t2-shift-op');
  function show(val) {
    const clamped = Math.max(0, Math.min(255, val));
    bits.forEach((b,i) => b.classList.toggle('on', !!(clamped & (1<<(7-i)))));
    if (decEl) decEl.textContent = clamped;
    return clamped;
  }
  let cur = 0;
  inp && inp.addEventListener('input', () => { cur = show(parseInt(inp.value)||0); });
  document.getElementById('viz-t2-left') && document.getElementById('viz-t2-left').addEventListener('click', () => {
    cur = show((cur << 1) & 0xFF);
    if (op) op.textContent = '× 2';
  });
  document.getElementById('viz-t2-right') && document.getElementById('viz-t2-right').addEventListener('click', () => {
    cur = show(cur >> 1);
    if (op) op.textContent = '÷ 2';
  });
  show(cur);
}

function initT2Overflow() {
  const btn = document.getElementById('viz-t2-overflow-btn');
  if (!btn) return;
  const bits  = document.getElementById('viz-t2-overflow-bits');
  const msg   = document.getElementById('viz-t2-overflow-msg');
  const decEl = document.getElementById('viz-t2-overflow-dec');
  let val = 0;
  function show(v) {
    const clamped = v & 0xF;
    if (bits) bits.querySelectorAll('.bit-cell').forEach((b,i) => b.classList.toggle('on', !!(clamped & (1<<(3-i)))));
    if (decEl) decEl.textContent = clamped;
    if (msg) {
      if (v > 15) { msg.textContent = '⚠ Overflow! Bit 5 passt nicht in 4 Bit → springt auf ' + clamped; msg.style.color='#ff4f6a'; }
      else        { msg.textContent = ''; }
    }
  }
  btn.addEventListener('click', () => { val++; show(val); });
  document.getElementById('viz-t2-overflow-reset') && document.getElementById('viz-t2-overflow-reset').addEventListener('click', () => { val=0; show(0); if(msg) msg.textContent=''; });
  show(0);
}

/* ══════════════════════════════════════════════════════════
   THEMA 3 – Zweier­komplement
══════════════════════════════════════════════════════════ */

function initT3Inverter() {
  const el = document.getElementById('viz-t3-inv');
  if (!el) return;
  const bits   = el.querySelectorAll('.bit-cell');
  const decEl  = document.getElementById('viz-t3-inv-dec');
  const ek     = document.getElementById('viz-t3-ek');
  const zk     = document.getElementById('viz-t3-zk');
  const ek_dec = document.getElementById('viz-t3-ek-dec');
  const zk_dec = document.getElementById('viz-t3-zk-dec');
  function getVal() { let v=0; bits.forEach((b,i)=>{ if(b.classList.contains('on')) v+=(1<<(7-i)); }); return v; }
  function update() {
    const v = getVal();
    if (decEl) decEl.textContent = v;
    const ekV = (~v) & 0xFF;
    const zkV = (ekV + 1) & 0xFF;
    if (ek) ek.querySelectorAll('.bit-cell').forEach((b,i) => b.classList.toggle('on', !!(ekV & (1<<(7-i)))));
    if (zk) zk.querySelectorAll('.bit-cell').forEach((b,i) => b.classList.toggle('on', !!(zkV & (1<<(7-i)))));
    if (ek_dec) ek_dec.textContent = 'Einerkomplement = ' + ekV.toString(2).padStart(8,'0') + ' (' + (ekV >= 128 ? ekV - 256 : ekV) + ')';
    if (zk_dec) zk_dec.textContent = 'Zweierkomplement = ' + zkV.toString(2).padStart(8,'0') + ' (' + (zkV >= 128 ? zkV - 256 : zkV) + ')';
  }
  bits.forEach(b => b.addEventListener('click', () => { b.classList.toggle('on'); update(); }));
  update();
}

function initT3Zahlenkreis() {
  const canvas = document.getElementById('viz-t3-circle');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height, R = 90, cx = W/2, cy = H/2;
  let selected = 0;
  function draw() {
    ctx.clearRect(0,0,W,H);
    for (let i = 0; i < 16; i++) {
      const angle = (i / 16) * 2 * Math.PI - Math.PI / 2;
      const x = cx + R * Math.cos(angle);
      const y = cy + R * Math.sin(angle);
      const twos = i < 8 ? i : i - 16;
      const isSelected = i === selected;
      ctx.beginPath();
      ctx.arc(x, y, isSelected ? 16 : 12, 0, 2*Math.PI);
      ctx.fillStyle = isSelected ? 'var(--active, #00d4ff)' : (i === 0 ? '#4de8b2' : (i < 8 ? '#7c6aff' : '#ff6b9d'));
      ctx.globalAlpha = isSelected ? 1 : 0.7;
      ctx.fill();
      ctx.globalAlpha = 1;
      ctx.fillStyle = '#fff';
      ctx.font = isSelected ? 'bold 11px monospace' : '10px monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(twos, x, y);
    }
    // label
    const twos = selected < 8 ? selected : selected - 16;
    const bin  = (selected & 0xF).toString(2).padStart(4,'0');
    ctx.fillStyle = 'var(--active, #00d4ff)';
    ctx.font = 'bold 13px monospace';
    ctx.textAlign = 'center';
    ctx.fillText(bin + '₂ = ' + twos, cx, cy);
  }
  canvas.addEventListener('click', e => {
    const rect = canvas.getBoundingClientRect();
    const mx = (e.clientX - rect.left) * (W / rect.width);
    const my = (e.clientY - rect.top)  * (H / rect.height);
    let best = -1, bestD = 999;
    for (let i = 0; i < 16; i++) {
      const angle = (i/16)*2*Math.PI - Math.PI/2;
      const x = cx + R*Math.cos(angle), y = cy + R*Math.sin(angle);
      const d = Math.hypot(mx-x, my-y);
      if (d < bestD) { bestD = d; best = i; }
    }
    if (bestD < 20) { selected = best; draw(); }
  });
  draw();
}

/* ══════════════════════════════════════════════════════════
   THEMA 4 – IEEE 754
══════════════════════════════════════════════════════════ */

function initT4IEEE() {
  const inp = document.getElementById('viz-t4-ieee-inp');
  if (!inp) return;
  const bitsEl = document.getElementById('viz-t4-ieee-bits');
  const signEl = document.getElementById('viz-t4-ieee-sign');
  const expEl  = document.getElementById('viz-t4-ieee-exp');
  const manEl  = document.getElementById('viz-t4-ieee-man');
  const infoEl = document.getElementById('viz-t4-ieee-info');

  function toIEEE754(f) {
    const buf = new ArrayBuffer(4);
    new DataView(buf).setFloat32(0, f, false);
    const bytes = new Uint8Array(buf);
    return Array.from(bytes).map(b => b.toString(2).padStart(8,'0')).join('');
  }

  function update() {
    const val = parseFloat(inp.value);
    if (isNaN(val)) return;
    const b = toIEEE754(val);
    const sign = b[0];
    const exp  = b.slice(1,9);
    const man  = b.slice(9);
    const expVal = parseInt(exp, 2) - 127;

    if (bitsEl) {
      bitsEl.querySelectorAll('.bit-cell').forEach((cell, i) => {
        cell.textContent = b[i];
        cell.classList.toggle('on', b[i] === '1');
        if (i === 0)       cell.style.borderColor = '#ff6b9d';
        else if (i < 9)    cell.style.borderColor = '#ffa047';
        else               cell.style.borderColor = '#4de8b2';
      });
    }
    if (signEl)  signEl.textContent  = sign === '0' ? '0  (positiv)' : '1  (negativ)';
    if (expEl)   expEl.textContent   = exp + '  → ' + parseInt(exp,2) + ' − 127 = ' + expVal;
    if (manEl)   manEl.textContent   = '1.' + man.replace(/0+$/, '') + '  (Hidden Bit)';
    if (infoEl)  infoEl.textContent  = val + ' = ' + (sign==='0'?'+':'-') + '1.' + man.replace(/0+$/,'') + ' × 2^' + expVal;
  }

  inp.addEventListener('input', update);
  update();
}

function initT4Bias() {
  const sl = document.getElementById('viz-t4-bias-sl');
  if (!sl) return;
  const stored = document.getElementById('viz-t4-bias-stored');
  const real   = document.getElementById('viz-t4-bias-real');
  const pow2   = document.getElementById('viz-t4-bias-pow');
  sl.addEventListener('input', () => {
    const v = parseInt(sl.value);
    if (stored) stored.textContent = v + '  (' + v.toString(2).padStart(8,'0') + '₂)';
    if (real)   real.textContent   = (v - 127) + '';
    if (pow2)   pow2.textContent   = '2^' + (v-127) + ' = ' + (v===127 ? '1' : (v>127 ? Math.pow(2,v-127).toExponential(2) : (1/Math.pow(2,127-v)).toExponential(2)));
  });
  sl.dispatchEvent(new Event('input'));
}

/* ══════════════════════════════════════════════════════════
   THEMA 5 – Information & Entropie
══════════════════════════════════════════════════════════ */

function initT5InfoCalc() {
  const sl = document.getElementById('viz-t5-prob-sl');
  if (!sl) return;
  const probEl = document.getElementById('viz-t5-prob-val');
  const infoEl = document.getElementById('viz-t5-info-val');
  sl.addEventListener('input', () => {
    const p = parseFloat(sl.value);
    if (probEl) probEl.textContent = p.toFixed(3);
    const I = p > 0 ? -Math.log2(p) : Infinity;
    if (infoEl) infoEl.textContent = I === Infinity ? '∞' : I.toFixed(3) + ' Bit';
  });
  sl.dispatchEvent(new Event('input'));
}

function initT5Entropy() {
  const slA = document.getElementById('viz-t5-ent-a');
  if (!slA) return;
  const pAEl = document.getElementById('viz-t5-pa');
  const pBEl = document.getElementById('viz-t5-pb');
  const hEl  = document.getElementById('viz-t5-h');
  const barA = document.getElementById('viz-t5-bar-a');
  const barB = document.getElementById('viz-t5-bar-b');
  const barH = document.getElementById('viz-t5-bar-h');

  slA.addEventListener('input', () => {
    const pA = parseFloat(slA.value);
    const pB = 1 - pA;
    if (pAEl) pAEl.textContent = pA.toFixed(2);
    if (pBEl) pBEl.textContent = pB.toFixed(2);
    const H = -(pA > 0 ? pA * Math.log2(pA) : 0) - (pB > 0 ? pB * Math.log2(pB) : 0);
    if (hEl)  hEl.textContent  = H.toFixed(4) + ' Bit';
    if (barA) barA.style.height = (pA * 100) + 'px';
    if (barB) barB.style.height = (pB * 100) + 'px';
    if (barH) barH.style.height = (H * 100)  + 'px';
  });
  slA.dispatchEvent(new Event('input'));
}

function initT5ASCII() {
  const inp = document.getElementById('viz-t5-ascii-inp');
  if (!inp) return;
  const binEl  = document.getElementById('viz-t5-ascii-bin');
  const decEl  = document.getElementById('viz-t5-ascii-dec');
  const charEl = document.getElementById('viz-t5-ascii-char');
  inp.addEventListener('input', () => {
    const ch = inp.value.slice(-1);
    if (!ch) return;
    const code = ch.charCodeAt(0);
    if (binEl)  binEl.textContent  = code.toString(2).padStart(7,'0') + '₂';
    if (decEl)  decEl.textContent  = code + '₁₀ (0x' + code.toString(16).toUpperCase() + ')';
    if (charEl) charEl.textContent = '"' + ch + '"';
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 6 – Datenkompression
══════════════════════════════════════════════════════════ */

function initT6RLE() {
  const btn = document.getElementById('viz-t6-rle-btn');
  if (!btn) return;
  const inp    = document.getElementById('viz-t6-rle-inp');
  const outEl  = document.getElementById('viz-t6-rle-out');
  const ratioEl= document.getElementById('viz-t6-rle-ratio');
  btn.addEventListener('click', () => {
    const s = (inp.value || '').toUpperCase();
    if (!s) return;
    let result = [], i = 0;
    while (i < s.length) {
      let ch = s[i], cnt = 1;
      while (i + cnt < s.length && s[i+cnt] === ch) cnt++;
      result.push({ ch, cnt });
      i += cnt;
    }
    const compressed = result.map(r => r.cnt > 1 ? '('+r.cnt+','+r.ch+')' : r.ch).join('');
    if (outEl) {
      outEl.innerHTML = result.map(r => {
        const color = r.cnt > 1 ? 'var(--active)' : 'var(--text-secondary)';
        const rep   = r.cnt > 1 ? `<span style="color:${color}"><b>(${r.cnt},${r.ch})</b></span>` : `<span style="color:${color}">${r.ch}</span>`;
        return rep;
      }).join(' ');
    }
    const ratio = ((1 - compressed.length / s.length) * 100).toFixed(1);
    if (ratioEl) ratioEl.textContent = `Original: ${s.length} Zeichen → Komprimiert: ${compressed.length} Zeichen (${ratio > 0 ? '-' : '+'}${Math.abs(ratio)}%)`;
  });
}

function initT6Huffman() {
  const btn = document.getElementById('viz-t6-huff-btn');
  if (!btn) return;
  const inp   = document.getElementById('viz-t6-huff-inp');
  const treeEl= document.getElementById('viz-t6-huff-tree');
  const codesEl = document.getElementById('viz-t6-huff-codes');

  btn.addEventListener('click', () => {
    const text = inp.value || 'AABBBCDDDD';
    const freq = {};
    for (const ch of text) freq[ch] = (freq[ch]||0) + 1;

    // Build tree
    let nodes = Object.entries(freq).map(([ch,f]) => ({ ch, f, left:null, right:null }));
    nodes.sort((a,b) => a.f - b.f);

    while (nodes.length > 1) {
      nodes.sort((a,b) => a.f - b.f);
      const left = nodes.shift(), right = nodes.shift();
      nodes.push({ ch: left.ch+right.ch, f: left.f+right.f, left, right });
    }

    // Get codes
    const codes = {};
    function traverse(node, code) {
      if (!node.left && !node.right) { codes[node.ch] = code || '0'; return; }
      if (node.left)  traverse(node.left,  code+'0');
      if (node.right) traverse(node.right, code+'1');
    }
    if (nodes[0]) traverse(nodes[0], '');

    const avgBefore = Math.ceil(Math.log2(Object.keys(freq).length));
    const totalBefore = text.length * avgBefore;
    const totalAfter  = Object.entries(freq).reduce((s,[ch,f]) => s + f * codes[ch].length, 0);

    if (codesEl) {
      codesEl.innerHTML = '<table class="viz-table"><thead><tr><th>Zeichen</th><th>Häufigkeit</th><th>Code</th><th>Bits</th></tr></thead><tbody>' +
        Object.entries(codes).sort((a,b)=>a[1].length-b[1].length).map(([ch,code]) =>
          `<tr><td>${ch}</td><td>${freq[ch]}</td><td><span class="sh-hi">${code}</span></td><td>${code.length}</td></tr>`
        ).join('') +
        `</tbody></table><div class="viz-note" style="margin-top:10px">Feste Kodierung: ${totalBefore} Bit → Huffman: ${totalAfter} Bit → Ersparnis: ${totalBefore - totalAfter} Bit</div>`;
    }
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 7 – Hashing
══════════════════════════════════════════════════════════ */

function initT7Hashtable() {
  const btn = document.getElementById('viz-t7-hash-btn');
  if (!btn) return;
  const keyInp = document.getElementById('viz-t7-key');
  const mInp   = document.getElementById('viz-t7-m');
  const tableEl= document.getElementById('viz-t7-table');
  const table  = {};

  function render() {
    const m = parseInt(mInp.value) || 7;
    let html = '<table class="viz-table"><thead><tr><th>Index</th><th>Einträge</th></tr></thead><tbody>';
    for (let i = 0; i < m; i++) {
      const entries = table[i] || [];
      const active  = entries.length > 0;
      html += `<tr class="${active ? 'active-row' : ''}"><td>${i}</td><td>${entries.length ? entries.join(' → ') : '–'}</td></tr>`;
    }
    html += '</tbody></table>';
    if (tableEl) tableEl.innerHTML = html;
  }

  btn.addEventListener('click', () => {
    const key = parseInt(keyInp.value);
    const m   = parseInt(mInp.value) || 7;
    if (isNaN(key)) return;
    const idx = ((key % m) + m) % m;
    if (!table[idx]) table[idx] = [];
    if (!table[idx].includes(key)) table[idx].push(key);
    render();
  });

  document.getElementById('viz-t7-hash-reset') && document.getElementById('viz-t7-hash-reset').addEventListener('click', () => {
    Object.keys(table).forEach(k => delete table[k]);
    render();
  });
  render();
}

function initT7Avalanche() {
  const btn = document.getElementById('viz-t7-av-btn');
  if (!btn) return;
  const inp1 = document.getElementById('viz-t7-av-inp1');
  const inp2 = document.getElementById('viz-t7-av-inp2');
  const out1 = document.getElementById('viz-t7-av-out1');
  const out2 = document.getElementById('viz-t7-av-out2');
  const diffEl = document.getElementById('viz-t7-av-diff');

  // Simple but visible hash (djb2-like, hex output)
  function simpleHash(str) {
    let h = 5381;
    for (let i = 0; i < str.length; i++) h = ((h << 5) + h + str.charCodeAt(i)) & 0xFFFFFFFF;
    return (h >>> 0).toString(16).toUpperCase().padStart(8, '0');
  }

  btn.addEventListener('click', () => {
    const s1 = inp1.value || 'Hallo';
    const s2 = inp2.value || 'hallo';
    const h1 = simpleHash(s1);
    const h2 = simpleHash(s2);
    let diffs = 0;
    const marked1 = h1.split('').map((c,i) => { if(c!==h2[i]){diffs++;return `<span style="color:#ff4f6a;font-weight:700">${c}</span>`;} return c; }).join('');
    const marked2 = h2.split('').map((c,i) => { if(c!==h1[i]) return `<span style="color:#ff4f6a;font-weight:700">${c}</span>`; return c; }).join('');
    if (out1) out1.innerHTML = marked1;
    if (out2) out2.innerHTML = marked2;
    if (diffEl) diffEl.textContent = diffs + ' von ' + h1.length + ' Zeichen unterschiedlich';
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 8 – Hamming-Codes
══════════════════════════════════════════════════════════ */

function initT8Hamming() {
  const btn = document.getElementById('viz-t8-enc-btn');
  if (!btn) return;
  const inp   = document.getElementById('viz-t8-data-inp');
  const outEl = document.getElementById('viz-t8-enc-out');
  const bitsEl= document.getElementById('viz-t8-enc-bits');

  btn.addEventListener('click', () => {
    const data = (inp.value || '1011').replace(/[^01]/g,'').slice(0,4).padStart(4,'0');
    const d    = data.split('').map(Number);
    // positions 1,2,3,4,5,6,7 → d at 3,5,6,7
    let code   = [0,0,0,0,0,0,0]; // index 0=unused
    code[3-1] = d[0]; code[5-1] = d[1]; code[6-1] = d[2]; code[7-1] = d[3];
    // p1 covers 1,3,5,7
    code[1-1] = (code[3-1] ^ code[5-1] ^ code[7-1]) & 1;
    // p2 covers 2,3,6,7
    code[2-1] = (code[3-1] ^ code[6-1] ^ code[7-1]) & 1;
    // p4 covers 4,5,6,7
    code[4-1] = (code[5-1] ^ code[6-1] ^ code[7-1]) & 1;

    if (outEl) outEl.textContent = code.join('');
    if (bitsEl) {
      bitsEl.querySelectorAll('.bit-cell').forEach((b,i) => {
        b.textContent = code[i];
        b.classList.toggle('on', code[i] === 1);
        b.classList.remove('parity','data-bit');
        if ([0,1,3].includes(i)) b.classList.add('parity');
        else                      b.classList.add('data-bit');
      });
    }
  });
}

function initT8Error() {
  const btn = document.getElementById('viz-t8-err-btn');
  if (!btn) return;
  const inp   = document.getElementById('viz-t8-err-inp');
  const outEl = document.getElementById('viz-t8-err-out');
  const bitsEl= document.getElementById('viz-t8-err-bits');

  btn.addEventListener('click', () => {
    const code = (inp.value || '0110011').replace(/[^01]/g,'').slice(0,7).padEnd(7,'0').split('').map(Number);
    const p1 = code[0] ^ code[2] ^ code[4] ^ code[6];
    const p2 = code[1] ^ code[2] ^ code[5] ^ code[6];
    const p4 = code[3] ^ code[4] ^ code[5] ^ code[6];
    const errPos = p1*1 + p2*2 + p4*4;

    if (bitsEl) {
      bitsEl.querySelectorAll('.bit-cell').forEach((b,i) => {
        b.textContent = code[i];
        b.classList.toggle('on', code[i]===1);
        b.classList.remove('error-bit','parity','data-bit');
        if (errPos > 0 && i === errPos-1) b.classList.add('error-bit');
        else if ([0,1,3].includes(i)) b.classList.add('parity');
        else b.classList.add('data-bit');
      });
    }
    if (outEl) {
      if (errPos === 0) { outEl.textContent = '✓ Kein Fehler gefunden.'; outEl.style.color='#4de8b2'; }
      else {
        const fixed = [...code]; fixed[errPos-1] ^= 1;
        outEl.textContent = `⚠ Fehler an Position ${errPos}! Korrigiert: ${fixed.join('')}`;
        outEl.style.color = '#ff4f6a';
      }
    }
  });
}

function initT8HammingDist() {
  const btn = document.getElementById('viz-t8-dist-btn');
  if (!btn) return;
  const a = document.getElementById('viz-t8-dist-a');
  const b = document.getElementById('viz-t8-dist-b');
  const outEl = document.getElementById('viz-t8-dist-out');
  btn.addEventListener('click', () => {
    const s1 = (a.value||'11010').replace(/[^01]/g,'');
    const s2 = (b.value||'10110').replace(/[^01]/g,'');
    const len = Math.max(s1.length,s2.length);
    const p1  = s1.padStart(len,'0');
    const p2  = s2.padStart(len,'0');
    let dist = 0;
    let html = '';
    for (let i=0; i<len; i++) {
      const diff = p1[i] !== p2[i];
      if (diff) dist++;
      html += `<span style="color:${diff?'#ff4f6a':'var(--text-secondary)'};font-weight:${diff?700:400}">${p1[i]}</span>`;
    }
    if (outEl) outEl.innerHTML = `${html} &nbsp;↔&nbsp; ${p2} &nbsp;→ Hamming-Abstand = <span style="color:var(--active);font-weight:700">${dist}</span>`;
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 9 – Java
══════════════════════════════════════════════════════════ */

function initT9Datatypes() {
  const sel = document.getElementById('viz-t9-type-sel');
  if (!sel) return;
  const info = {
    byte:   { bits:8,  min:-128,           max:127,            note:'Zweierkomplement' },
    short:  { bits:16, min:-32768,          max:32767,          note:'Zweierkomplement' },
    int:    { bits:32, min:-2147483648,      max:2147483647,     note:'Zweierkomplement' },
    long:   { bits:64, min:'-9.2 × 10¹⁸',  max:'9.2 × 10¹⁸',  note:'Zweierkomplement' },
    float:  { bits:32, min:'~1.4 × 10⁻⁴⁵', max:'~3.4 × 10³⁸', note:'IEEE 754 Single' },
    double: { bits:64, min:'~5 × 10⁻³²⁴',  max:'~1.8 × 10³⁰⁸',note:'IEEE 754 Double' },
  };
  const bitsEl = document.getElementById('viz-t9-bits');
  const minEl  = document.getElementById('viz-t9-min');
  const maxEl  = document.getElementById('viz-t9-max');
  const noteEl = document.getElementById('viz-t9-note');
  const barEl  = document.getElementById('viz-t9-type-bar');

  sel.addEventListener('change', () => {
    const t = info[sel.value];
    if (!t) return;
    if (bitsEl) bitsEl.textContent = t.bits + ' Bit';
    if (minEl)  minEl.textContent  = t.min;
    if (maxEl)  maxEl.textContent  = t.max;
    if (noteEl) noteEl.textContent = t.note;
    if (barEl)  barEl.style.width  = (t.bits / 64 * 100) + '%';
  });
  sel.dispatchEvent(new Event('change'));
}

function initT9LoopTrace() {
  const btn = document.getElementById('viz-t9-loop-btn');
  if (!btn) return;
  const nInp  = document.getElementById('viz-t9-loop-n');
  const tbody = document.getElementById('viz-t9-loop-tbody');

  btn.addEventListener('click', () => {
    const n = Math.min(parseInt(nInp.value)||5, 20);
    if (!tbody) return;
    tbody.innerHTML = '';
    let summe = 0;
    for (let i = 1; i <= n; i++) {
      summe += i;
      const tr = document.createElement('tr');
      tr.className = i === n ? 'active-row' : '';
      tr.innerHTML = `<td>${i}</td><td>${i-1 === 0 ? 0 : Array.from({length:i-1},(_,k)=>k+1).reduce((a,b)=>a+b,0)}</td><td>${summe}</td>`;
      tbody.appendChild(tr);
      setTimeout(() => tr.style.opacity='1', i * 80);
      tr.style.opacity = '0';
      tr.style.transition = 'opacity .3s';
    }
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 10 – Softwareentwicklung
══════════════════════════════════════════════════════════ */

function initT10Waterfall() {
  const phases = document.querySelectorAll('.wf-phase');
  if (!phases.length) return;
  const detail = document.getElementById('viz-t10-detail');
  const info = {
    0: { title:'Anforderungsanalyse', result:'Pflichtenheft / Anforderungsspezifikation', artefakt:'Lastenheft, Pflichtenheft' },
    1: { title:'Entwurf (Design)',    result:'Systemarchitektur, Klassendiagramme', artefakt:'UML-Diagramme, ER-Modell' },
    2: { title:'Implementierung',     result:'Quellcode', artefakt:'Java-Klassen, Module' },
    3: { title:'Test',                result:'Testprotokolle, Fehlerlisten', artefakt:'Unit-Tests, Testberichte' },
    4: { title:'Einführung',          result:'Laufendes System beim Kunden', artefakt:'Installationspaket, Handbuch' },
    5: { title:'Wartung',             result:'Bugfixes, Updates', artefakt:'Patches, Release Notes' },
  };
  phases.forEach((ph, i) => {
    ph.addEventListener('click', () => {
      phases.forEach(p => p.classList.remove('active'));
      ph.classList.add('active');
      if (detail && info[i]) {
        detail.innerHTML = `<strong>${info[i].title}</strong><br>
          <span class="viz-label">Ergebnis:</span> ${info[i].result}<br>
          <span class="viz-label">Artefakte:</span> ${info[i].artefakt}`;
      }
    });
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 11 – OOP
══════════════════════════════════════════════════════════ */

function initT11Instantiate() {
  const btn = document.getElementById('viz-t11-new-btn');
  if (!btn) return;
  const nameInp  = document.getElementById('viz-t11-name');
  const alterInp = document.getElementById('viz-t11-alter');
  const noteInp  = document.getElementById('viz-t11-note');
  const objEl    = document.getElementById('viz-t11-obj');

  btn.addEventListener('click', () => {
    const name  = nameInp.value  || 'Hannah';
    const alter = alterInp.value || '17';
    const note  = noteInp.value  || '1.7';
    if (!objEl) return;
    objEl.style.opacity = '0';
    objEl.style.transform = 'scale(.9)';
    objEl.style.transition = 'opacity .3s, transform .3s';
    objEl.innerHTML = `
      <div class="uml-class-name">Schueler@${Math.floor(Math.random()*9000+1000)}</div>
      <div class="uml-section">
        <span class="uml-private">- name</span> = "${name}"<br>
        <span class="uml-private">- alter</span> = ${alter}<br>
        <span class="uml-private">- note</span>  = ${note}
      </div>
      <div class="uml-section">
        <span class="uml-public">+ getName()</span> → "${name}"<br>
        <span class="uml-public">+ begruesse()</span> → "Hallo, ${name}!"
      </div>`;
    requestAnimationFrame(() => {
      objEl.style.opacity = '1';
      objEl.style.transform = 'scale(1)';
    });
  });
}

function initT11Polymorphism() {
  const btn = document.getElementById('viz-t11-poly-btn');
  if (!btn) return;
  const arena = document.getElementById('viz-t11-poly-arena');
  const animals = [
    { name:'Hund',  sound:'Wau!',  color:'#ffa047' },
    { name:'Katze', sound:'Miau!', color:'#a78bfa' },
    { name:'Vogel', sound:'Piep!', color:'#38bdf8' },
    { name:'Hund',  sound:'Wau!',  color:'#ffa047' },
    { name:'Katze', sound:'Miau!', color:'#a78bfa' },
  ];
  let idx = 0;
  btn.addEventListener('click', () => {
    if (!arena) return;
    const items = arena.querySelectorAll('.poly-item');
    items.forEach(it => it.classList.remove('active'));
    if (idx < items.length) {
      const item = items[idx];
      item.classList.add('active');
      const bubble = item.querySelector('.poly-bubble');
      if (bubble) { bubble.style.opacity='1'; bubble.style.transform='translateY(-4px)'; }
      idx++;
    } else {
      items.forEach(it => { it.classList.remove('active'); const b=it.querySelector('.poly-bubble'); if(b){b.style.opacity='0';b.style.transform='';} });
      idx = 0;
    }
  });
}

/* ══════════════════════════════════════════════════════════
   THEMA 12 – Struktogramme
══════════════════════════════════════════════════════════ */

function initT12Trace() {
  const btn = document.getElementById('viz-t12-trace-btn');
  if (!btn) return;
  const nInp  = document.getElementById('viz-t12-trace-n');
  const rows  = document.querySelectorAll('.struk-row');
  const varEl = document.getElementById('viz-t12-vars');
  let steps = [], stepIdx = 0;

  btn.addEventListener('click', () => {
    const n = Math.min(parseInt(nInp.value)||5, 10);
    steps = [];
    steps.push({ row:0, vars:'n = '+n+', summe = 0, i = 1' });
    let summe = 0;
    for (let i=1; i<=n; i++) {
      summe += i;
      steps.push({ row:1, vars:`i = ${i}, summe = ${summe}` });
    }
    steps.push({ row:2, vars:`Ausgabe: summe = ${summe}` });
    stepIdx = 0;
    nextStep();
  });

  function nextStep() {
    if (!steps.length) return;
    rows.forEach(r => r.classList.remove('struk-active'));
    const s = steps[stepIdx % steps.length];
    if (rows[s.row]) rows[s.row].classList.add('struk-active');
    if (varEl) varEl.textContent = s.vars;
    stepIdx++;
    if (stepIdx < steps.length) setTimeout(nextStep, 600);
  }
}

/* ══════════════════════════════════════════════════════════
   THEMA 13 – Sortieralgorithmen
══════════════════════════════════════════════════════════ */

function initT13SortRace() {
  const btn = document.getElementById('viz-t13-sort-btn');
  if (!btn) return;
  const arenas = {
    insertion: document.getElementById('viz-t13-arena-ins'),
    selection: document.getElementById('viz-t13-arena-sel'),
    quick:     document.getElementById('viz-t13-arena-quick'),
    merge:     document.getElementById('viz-t13-arena-merge'),
  };
  const statsEls = {
    insertion: document.getElementById('viz-t13-stats-ins'),
    selection: document.getElementById('viz-t13-stats-sel'),
    quick:     document.getElementById('viz-t13-stats-quick'),
    merge:     document.getElementById('viz-t13-stats-merge'),
  };

  function makeArray() {
    return Array.from({length:16}, () => Math.floor(Math.random()*95)+5);
  }

  function renderBars(arena, arr, comparing=[], swapping=[], sorted=[]) {
    if (!arena) return;
    const max = Math.max(...arr);
    arena.innerHTML = arr.map((v,i) => {
      let cls = 'sort-bar';
      if (sorted.includes(i))   cls += ' sorted';
      else if (swapping.includes(i))  cls += ' swapping';
      else if (comparing.includes(i)) cls += ' comparing';
      return `<div class="${cls}" style="height:${(v/max*130)}px"></div>`;
    }).join('');
  }

  async function animateSort(name, arr) {
    const arena = arenas[name];
    const statsEl = statsEls[name];
    let comparisons = 0, swaps = 0;
    const a = [...arr];

    function setStats() { if (statsEl) statsEl.innerHTML = `Vergleiche: <span>${comparisons}</span> Tausche: <span>${swaps}</span>`; }
    function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

    if (name === 'insertion') {
      for (let i=1; i<a.length; i++) {
        let j = i;
        while (j>0) {
          comparisons++;
          renderBars(arena, a, [j,j-1]);
          setStats();
          await delay(60);
          if (a[j]<a[j-1]) { [a[j],a[j-1]] = [a[j-1],a[j]]; swaps++; j--; }
          else break;
        }
      }
    } else if (name === 'selection') {
      for (let i=0; i<a.length-1; i++) {
        let minIdx = i;
        for (let j=i+1; j<a.length; j++) {
          comparisons++;
          renderBars(arena, a, [j, minIdx]);
          setStats();
          await delay(50);
          if (a[j]<a[minIdx]) minIdx = j;
        }
        if (minIdx !== i) { [a[i],a[minIdx]] = [a[minIdx],a[i]]; swaps++; }
        renderBars(arena, a, [], [], Array.from({length:i+1},(_,k)=>k));
      }
    } else if (name === 'quick') {
      async function qsort(lo, hi) {
        if (lo >= hi) return;
        const pivot = a[hi];
        let pi = lo;
        for (let j=lo; j<hi; j++) {
          comparisons++;
          renderBars(arena, a, [j, hi]);
          setStats();
          await delay(40);
          if (a[j]<=pivot) { [a[j],a[pi]]=[a[pi],a[j]]; swaps++; pi++; }
        }
        [a[pi],a[hi]] = [a[hi],a[pi]]; swaps++;
        await qsort(lo, pi-1);
        await qsort(pi+1, hi);
      }
      await qsort(0, a.length-1);
    } else if (name === 'merge') {
      async function msort(lo, hi) {
        if (lo >= hi) return;
        const mid = Math.floor((lo+hi)/2);
        await msort(lo, mid);
        await msort(mid+1, hi);
        const left  = a.slice(lo, mid+1);
        const right = a.slice(mid+1, hi+1);
        let i=0, j=0, k=lo;
        while (i<left.length && j<right.length) {
          comparisons++;
          renderBars(arena, a, [k]);
          setStats();
          await delay(35);
          if (left[i]<=right[j]) a[k++]=left[i++];
          else { a[k++]=right[j++]; swaps++; }
        }
        while (i<left.length) a[k++]=left[i++];
        while (j<right.length) a[k++]=right[j++];
      }
      await msort(0, a.length-1);
    }

    renderBars(arena, a, [], [], a.map((_,i)=>i));
    setStats();
  }

  btn.addEventListener('click', () => {
    const arr = makeArray();
    Object.keys(arenas).forEach(name => animateSort(name, arr));
  });
  // Initial display
  const arr = makeArray();
  Object.keys(arenas).forEach(name => renderBars(arenas[name], arr));
}

function initT13ONotation() {
  const canvas = document.getElementById('viz-t13-canvas');
  if (!canvas) return;
  const sl = document.getElementById('viz-t13-n-sl');
  const ctx = canvas.getContext('2d');

  function draw() {
    const n = parseInt(sl ? sl.value : 100);
    const W = canvas.width, H = canvas.height;
    ctx.clearRect(0,0,W,H);

    // Background
    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--sh-code-bg').trim() || '#0a0c14';
    ctx.fillRect(0,0,W,H);

    const pad = 40;
    const funcs = [
      { label:'O(n²)',     fn: x => x*x,            color:'#ff4f6a' },
      { label:'O(n log n)',fn: x => x*Math.log2(x+1),color:'#ffa047' },
      { label:'O(n)',      fn: x => x,               color:'#4de8b2' },
      { label:'O(log n)',  fn: x => Math.log2(x+1),  color:'#38bdf8' },
    ];

    const maxY = n * n;
    const scaleX = (W - pad*2) / n;
    const scaleY = (H - pad*2) / maxY;

    // Grid
    ctx.strokeStyle = '#252840';
    ctx.lineWidth = 1;
    for (let i=0; i<=5; i++) {
      const y = pad + (H-pad*2) * i/5;
      ctx.beginPath(); ctx.moveTo(pad,y); ctx.lineTo(W-pad,y); ctx.stroke();
    }

    // Axes
    ctx.strokeStyle = '#565a80';
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(pad,pad); ctx.lineTo(pad,H-pad); ctx.lineTo(W-pad,H-pad); ctx.stroke();

    // Axis labels
    ctx.fillStyle = '#565a80';
    ctx.font = '11px monospace';
    ctx.fillText('n = '+n, W-pad-30, H-pad+14);
    ctx.fillText('0', pad-14, H-pad+4);

    // Functions
    funcs.forEach(f => {
      ctx.beginPath();
      ctx.strokeStyle = f.color;
      ctx.lineWidth = 2;
      let first = true;
      for (let x=0; x<=n; x++) {
        const py = H - pad - Math.min(f.fn(x),maxY) * scaleY;
        const px = pad + x * scaleX;
        if (first) { ctx.moveTo(px,py); first=false; } else ctx.lineTo(px,py);
      }
      ctx.stroke();
      // label at right end
      const endY = H - pad - Math.min(f.fn(n),maxY) * scaleY;
      ctx.fillStyle = f.color;
      ctx.font = 'bold 11px monospace';
      ctx.fillText(f.label, W - pad - 60, Math.max(pad+8, endY));
    });

    if (sl) {
      const nLabel = document.getElementById('viz-t13-n-val');
      if (nLabel) nLabel.textContent = n;
    }
  }

  if (sl) sl.addEventListener('input', draw);
  // Resize canvas to match CSS width
  canvas.width  = canvas.offsetWidth  || 700;
  canvas.height = canvas.offsetHeight || 200;
  draw();
}

/* ══════════════════════════════════════════════════════════
   BOOT – call all inits
══════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
  // T1
  initT1BitSchalter();
  initT1Division();
  initT1BinaryCounter();
  initT1ColorMixer();
  // T2
  initT2Addition();
  initT2Bitshift();
  initT2Overflow();
  // T3
  initT3Inverter();
  initT3Zahlenkreis();
  // T4
  initT4IEEE();
  initT4Bias();
  // T5
  initT5InfoCalc();
  initT5Entropy();
  initT5ASCII();
  // T6
  initT6RLE();
  initT6Huffman();
  // T7
  initT7Hashtable();
  initT7Avalanche();
  // T8
  initT8Hamming();
  initT8Error();
  initT8HammingDist();
  // T9
  initT9Datatypes();
  initT9LoopTrace();
  // T10
  initT10Waterfall();
  // T11
  initT11Instantiate();
  initT11Polymorphism();
  // T12
  initT12Trace();
  // T13
  initT13SortRace();
  initT13ONotation();
});
