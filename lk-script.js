/* lk-script.js — shared JS for all LK Informatik pages */

/* ── Theme Toggle ──────────────────────────────────────── */
(function () {
  const STORAGE_KEY = 'lk-theme';
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved === 'light') document.body.classList.add('light');
})();

function initThemeToggle() {
  const btn = document.getElementById('themeToggle');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light');
    localStorage.setItem('lk-theme', isLight ? 'light' : 'dark');
    const lbl = btn.querySelector('.toggle-label');
    if (lbl) lbl.textContent = isLight ? 'Light Mode' : 'Dark Mode';
  });
  // set initial label
  const lbl = btn.querySelector('.toggle-label');
  if (lbl) lbl.textContent = document.body.classList.contains('light') ? 'Light Mode' : 'Dark Mode';
}

/* ── Copy Buttons ──────────────────────────────────────── */
function copyCode(btn) {
  const pre = btn.closest('.code-wrap').querySelector('pre');
  navigator.clipboard.writeText(pre.innerText).then(() => {
    const orig = btn.textContent;
    btn.classList.add('copied');
    btn.textContent = 'Kopiert ✓';
    setTimeout(() => {
      btn.classList.remove('copied');
      btn.textContent = orig;
    }, 1800);
  });
}

/* ── Task Toggles ──────────────────────────────────────── */
function toggleTask(header) {
  const body   = header.nextElementSibling;
  const toggle = header.querySelector('.task-toggle');
  const isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  toggle.classList.toggle('open', !isOpen);
}

/* ── Reading Progress Bar ──────────────────────────────── */
function initProgress() {
  const bar = document.getElementById('progress');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const doc = document.documentElement;
    const pct = doc.scrollTop / (doc.scrollHeight - doc.clientHeight);
    bar.style.transform = `scaleX(${pct || 0})`;
  }, { passive: true });
}

/* ── Rating Bars (IntersectionObserver) ───────────────── */
function initRatingBars() {
  const fills = document.querySelectorAll('.rating-fill');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.width = e.target.dataset.val + '%';
        obs.unobserve(e.target);
      }
    });
  }, { threshold: .3 });
  fills.forEach(f => obs.observe(f));
}

/* ── Boot ──────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initProgress();
  initRatingBars();
});
