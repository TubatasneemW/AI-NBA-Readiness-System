/* ====================================================
   ACCREDIX — DashboardCard Component (Vanilla JS)
   ==================================================== */

const DashboardCardComponent = {
  render: function({ title, value, badge, subtext, icon, trend }) {
    return `
      <div class="kpi-card glass-panel">
        <div class="kpi-header">
          <span class="kpi-title">${title}</span>
          ${icon ? `<span class="kpi-icon">${icon}</span>` : ''}
        </div>
        <div class="kpi-body">
          <div class="kpi-value-row">
            <span class="kpi-value">${value}</span>
            ${badge ? `<span class="kpi-badge ${badge.type || 'emerald'}">${badge.text}</span>` : ''}
          </div>
          ${subtext ? `<p class="kpi-subtext">${subtext}</p>` : ''}
          ${trend ? `
            <div class="kpi-trend">
              <span class="trend-icon ${trend.direction}">${trend.direction === 'up' ? '↑' : '↓'}</span>
              <span>${trend.label}</span>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }
};

window.DashboardCardComponent = DashboardCardComponent;
