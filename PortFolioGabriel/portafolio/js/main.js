// Menú responsive accesible
const btn = document.getElementById('btnMenu');
const menu = document.getElementById('menu');

btn.addEventListener('click', () => {
  const open = menu.classList.toggle('show');
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
});

// Copiar email al portapapeles
const copyBtn = document.getElementById('copyBtn');
const copiedMsg = document.getElementById('copiedMsg');

if (copyBtn) {
  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText('gabymoya12@gmail.com');
      copiedMsg.hidden = false;
      setTimeout(() => (copiedMsg.hidden = true), 1200);
    } catch (e) {
      alert('No se pudo copiar el email.');
    }
  });
}
