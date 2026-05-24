// Versioned cache — bump CACHE to force a refresh of cached assets.
const CACHE = 'qr-v1';
const ASSETS = ['./', './manifest.json', './icon.svg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  // Share-target navigations land at /?text=…&url=… — serve cached / and let
  // the page JS read the params. This also keeps the shared payload off
  // GitHub's request logs (the SW intercepts before any network hit).
  if (req.mode === 'navigate') {
    e.respondWith(
      caches.match('./', { ignoreSearch: true })
        .then(r => r || fetch('./'))
    );
    return;
  }

  e.respondWith(
    caches.match(req).then(r => r || fetch(req))
  );
});
