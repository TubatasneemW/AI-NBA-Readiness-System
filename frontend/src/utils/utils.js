/**
 * ACCREDIX — utils.js
 * Shared utility functions across all page modules
 */

const Utils = {
  /**
   * Format a percentage with sign for trend deltas
   */
  formatDelta(value) {
    return value >= 0 ? `↑ ${value}%` : `↓ ${Math.abs(value)}%`;
  },

  /**
   * Get status level from a score vs target
   */
  getStatus(score, target = 70) {
    if (score >= target) return 'PASS';
    if (score >= target - 10) return 'WARNING';
    return 'CRITICAL';
  },

  /**
   * Escape HTML for safe rendering of user-input text
   */
  escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  },

  /**
   * Animate a numeric counter from 0 to target
   */
  animateCounter(elementId, target, suffix = '', duration = 1200) {
    const el = document.getElementById(elementId);
    if (!el) return;
    const start = Date.now();
    const tick = () => {
      const elapsed = Date.now() - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    };
    tick();
  },

  /**
   * Show a temporary toast notification
   */
  showToast(message, type = 'success') {
    const existing = document.getElementById('accredix-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'accredix-toast';
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `<span>${message}</span>`;
    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add('toast-visible'), 50);
    setTimeout(() => {
      toast.classList.remove('toast-visible');
      setTimeout(() => toast.remove(), 400);
    }, 3500);
  }
};
