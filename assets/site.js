(() => {
  const toggle = document.querySelector('.menu-toggle');
  const panel = document.querySelector('.nav-panel');
  if (!toggle || !panel) return;

  const close = () => {
    panel.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const willOpen = !panel.classList.contains('is-open');
    panel.classList.toggle('is-open', willOpen);
    toggle.setAttribute('aria-expanded', String(willOpen));
  });

  panel.querySelectorAll('a').forEach((link) => link.addEventListener('click', close));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') close();
  });

  document.querySelectorAll('[data-language-choice]').forEach((link) => {
    link.addEventListener('click', () => {
      try {
        localStorage.setItem('terrahit-language', link.dataset.languageChoice);
      } catch (error) {}
    });
  });

  const form = document.querySelector('.contact-form[data-success-url]');
  if (!form) return;

  const submit = form.querySelector('[type="submit"]');
  const status = form.querySelector('.form-status');
  const submitLabel = submit.textContent;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    submit.disabled = true;
    submit.textContent = form.dataset.sendingLabel;
    status.hidden = true;

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
      });
      if (!response.ok) throw new Error('Submission failed');
      window.location.assign(form.dataset.successUrl);
    } catch (error) {
      status.textContent = form.dataset.errorMessage;
      status.hidden = false;
      submit.disabled = false;
      submit.textContent = submitLabel;
    }
  });
})();
