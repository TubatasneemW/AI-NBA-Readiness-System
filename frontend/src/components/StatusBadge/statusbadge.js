/**
 * ACCREDIX — StatusBadge Component
 * Utility to generate HTML status badges and chips
 */

const StatusBadgeComponent = {
  /**
   * Returns a styled status badge HTML string
   * @param {'PASS'|'WARNING'|'CRITICAL'|'VERIFIED'|'NEEDS_REVIEW'|'MISSING'} status
   * @param {string} [customLabel] - Optional override for display text
   */
  render(status, customLabel) {
    const map = {
      PASS:         { cls: 'status-pass',     label: 'PASS ✓' },
      WARNING:      { cls: 'status-warning',  label: 'WARNING ⚠' },
      CRITICAL:     { cls: 'status-critical', label: 'CRITICAL 🔴' },
      VERIFIED:     { cls: 'status-pass',     label: 'VERIFIED ✓' },
      NEEDS_REVIEW: { cls: 'status-warning',  label: 'NEEDS REVIEW' },
      MISSING:      { cls: 'status-critical', label: 'MISSING ✕' },
      EXPIRED:      { cls: 'status-warning',  label: 'EXPIRED' },
      IN_PROGRESS:  { cls: 'status-warning',  label: 'IN PROGRESS' },
      PENDING:      { cls: 'status-warning',  label: 'PENDING' },
      COMPLETED:    { cls: 'status-pass',     label: 'COMPLETED ✓' }
    };
    const entry = map[status] || { cls: 'status-warning', label: status };
    const label = customLabel || entry.label;
    return `<span class="badge-status ${entry.cls}">${label}</span>`;
  },

  /**
   * Returns a risk level badge for students
   */
  riskBadge(level) {
    const map = {
      HIGH_ATTENTION:    { cls: 'status-critical', label: 'HIGH ATTENTION 🔴' },
      NEEDS_MONITORING:  { cls: 'status-warning',  label: 'MONITORING 🟡' },
      ON_TRACK:          { cls: 'status-pass',     label: 'ON TRACK 🟢' }
    };
    const entry = map[level] || map['ON_TRACK'];
    return `<span class="badge-status ${entry.cls}">${entry.label}</span>`;
  }
};
