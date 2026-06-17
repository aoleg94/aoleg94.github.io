// Tombstone service worker. The QR app's SW moved to /qr/sw.js (scope /qr/).
// This retires the old root-scoped SW on devices that installed it before the
// move: on its next update check the browser fetches this file, and it
// unregisters itself and reloads open clients so they hit the live network.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    await self.registration.unregister();
    const clients = await self.clients.matchAll();
    clients.forEach(c => c.navigate(c.url));
  })());
});
