// ==UserScript==
// @name         Claude Usage Bar
// @namespace    eocuwll
// @version      1.0.0
// @description  Affiche en permanence sous la barre de chat de claude.ai le % d'utilisation (fenêtre 5 h et hebdomadaire).
// @match        https://claude.ai/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==

// NOTE : s'appuie sur l'endpoint interne non documenté utilisé par la page
// Paramètres > Utilisation de claude.ai. Il peut changer sans préavis.

(function () {
  'use strict';

  const REFRESH_MS = 60 * 1000;

  const bar = document.createElement('div');
  bar.id = 'claude-usage-bar';
  Object.assign(bar.style, {
    position: 'fixed',
    bottom: '2px',
    left: '50%',
    transform: 'translateX(-50%)',
    zIndex: '9999',
    font: '12px/1.4 system-ui, sans-serif',
    padding: '2px 10px',
    borderRadius: '10px',
    background: 'rgba(40,40,40,0.85)',
    color: '#f2f2f2',
    pointerEvents: 'none',
    whiteSpace: 'nowrap',
  });
  bar.textContent = 'Usage : chargement…';
  document.body.appendChild(bar);

  function color(p) {
    if (p >= 90) return '#ff6b6b';
    if (p >= 70) return '#ffb84d';
    return '#7bd88f';
  }

  function fmtReset(iso, withDay) {
    if (!iso) return '';
    const d = new Date(iso);
    if (isNaN(d)) return '';
    const opts = withDay
      ? { weekday: 'short', hour: '2-digit', minute: '2-digit' }
      : { hour: '2-digit', minute: '2-digit' };
    return ' (reset ' + d.toLocaleString('fr-FR', opts) + ')';
  }

  function part(label, w, withDay) {
    if (!w || w.utilization == null) return '';
    const p = Math.round(w.utilization);
    return `<span style="color:${color(p)}">${label} : ${p}%</span>${fmtReset(w.resets_at, withDay)}`;
  }

  let orgId = null;
  async function getOrgId() {
    if (orgId) return orgId;
    const m = document.cookie.match(/(?:^|;\s*)lastActiveOrg=([^;]+)/);
    if (m) return (orgId = decodeURIComponent(m[1]));
    const r = await fetch('/api/organizations', { credentials: 'include' });
    const orgs = await r.json();
    return (orgId = orgs && orgs[0] && orgs[0].uuid);
  }

  async function refresh() {
    try {
      const id = await getOrgId();
      if (!id) throw new Error('organisation introuvable');
      const r = await fetch(`/api/organizations/${id}/usage`, { credentials: 'include' });
      if (!r.ok) throw new Error('HTTP ' + r.status);
      const d = await r.json();
      const parts = [part('5 h', d.five_hour, false), part('Semaine', d.seven_day, true)].filter(Boolean);
      bar.innerHTML = parts.length ? parts.join(' &nbsp;|&nbsp; ') : 'Usage : non disponible';
    } catch (e) {
      bar.textContent = 'Usage : erreur (' + e.message + ')';
    }
  }

  refresh();
  setInterval(refresh, REFRESH_MS);
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden) refresh();
  });
})();
