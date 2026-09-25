// Cache hors ligne de l'application (PWA)
const CACHE = 'normes-nm-en-v1';
const FILES = ['./', './index.html', './data/normes.js', './data/guide.js', './manifest.webmanifest', './icon.svg'];
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES))));
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))));
self.addEventListener('fetch', e => e.respondWith(caches.match(e.request).then(r => r || fetch(e.request))));
