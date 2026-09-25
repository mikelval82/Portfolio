document.documentElement.classList.add('js');

const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.site-nav');
function closeMenu() {
  navigation.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.textContent = 'Menu +';
}
toggle?.addEventListener('click', () => {
  const isOpen = navigation.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', String(isOpen));
  toggle.textContent = isOpen ? 'Close −' : 'Menu +';
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation?.classList.contains('is-open')) {
    closeMenu();
    toggle.focus();
  }
});
matchMedia('(min-width: 761px)').addEventListener('change', () => {
  if (navigation && toggle) closeMenu();
});

const form = document.querySelector('#contact-form');
form?.addEventListener('submit', async event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const submit = form.querySelector('[type="submit"]');
  const status = document.querySelector('#form-status');
  submit.disabled = true;
  submit.textContent = 'Sending…';
  status.textContent = '';
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 15000);
  try {
    const response = await fetch(form.action, {
      method: 'POST', body: new FormData(form),
      headers: { Accept: 'application/json' }, signal: controller.signal
    });
    if (!response.ok) throw new Error('Message not accepted');
    status.textContent = 'Thank you. Your message has been sent.';
    form.reset();
  } catch {
    status.textContent = 'Your message could not be sent. Please try again or email mikel1982mail@gmail.com.';
  } finally {
    clearTimeout(timeout);
    submit.disabled = false;
    submit.textContent = 'Send message →';
  }
});
