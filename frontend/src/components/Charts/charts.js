/**
 * ACCREDIX — Charts Component
 * Renders SVG-based bar and line charts using vanilla JS
 */

const ChartsComponent = {

  /**
   * Render a simple horizontal bar chart (CO Attainment bars)
   * @param {string} containerId
   * @param {Array<{label, value, target, color}>} data
   */
  renderBarChart(containerId, data) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = data.map(item => {
      const isWeak = item.value < item.target;
      const barColor = isWeak ? 'var(--crimson)' : 'var(--emerald)';
      const statusChip = isWeak
        ? `<span class="badge-status status-critical">GAP: -${(item.target - item.value).toFixed(1)}%</span>`
        : `<span class="badge-status status-pass">PASS ✓</span>`;

      return `
        <div class="co-bar-item">
          <div class="co-bar-header">
            <strong>${item.label}</strong>
            <div>${statusChip} <strong class="co-score">${item.value}%</strong></div>
          </div>
          <div class="bar-track">
            <div class="bar-fill" style="width: ${item.value}%; background: ${barColor};"></div>
            <div class="bar-target-line" style="left: ${item.target}%;" title="Target ${item.target}%"></div>
          </div>
        </div>
      `;
    }).join('');
  },

  /**
   * Render an SVG line trend chart
   * @param {string} containerId
   * @param {Array<{year, value}>} data
   * @param {string} color
   */
  renderLineTrend(containerId, data, color = 'var(--cyan)') {
    const container = document.getElementById(containerId);
    if (!container) return;

    const W = 400, H = 160, pad = 40;
    const maxVal = 100, minVal = 75;
    const scaleX = (i) => pad + (i / (data.length - 1)) * (W - pad * 2);
    const scaleY = (v) => H - pad - ((v - minVal) / (maxVal - minVal)) * (H - pad * 2);

    const points = data.map((d, i) => `${scaleX(i)},${scaleY(d.value)}`).join(' ');
    const circles = data.map((d, i) => `
      <circle cx="${scaleX(i)}" cy="${scaleY(d.value)}" r="${i === data.length - 1 ? 6 : 4}" 
        fill="${color}" stroke="${i === data.length - 1 ? '#fff' : 'none'}" stroke-width="2"
        title="${d.year}: ${d.value}%"/>
      <text x="${scaleX(i)}" y="${H - 8}" fill="var(--text-dim)" font-size="10" text-anchor="middle">${d.year}</text>
    `).join('');

    container.innerHTML = `
      <svg viewBox="0 0 ${W} ${H}" style="width:100%; height:${H}px;">
        <!-- Grid -->
        <line x1="${pad}" y1="${scaleY(100)}" x2="${W - pad}" y2="${scaleY(100)}" stroke="var(--border-color)" stroke-dasharray="3"/>
        <line x1="${pad}" y1="${scaleY(90)}"  x2="${W - pad}" y2="${scaleY(90)}"  stroke="var(--border-color)" stroke-dasharray="3"/>
        <line x1="${pad}" y1="${scaleY(80)}"  x2="${W - pad}" y2="${scaleY(80)}"  stroke="var(--border-color)"/>
        <!-- Y Labels -->
        <text x="10" y="${scaleY(100) + 4}" fill="var(--text-dim)" font-size="10">100%</text>
        <text x="15" y="${scaleY(90) + 4}"  fill="var(--text-dim)" font-size="10">90%</text>
        <text x="15" y="${scaleY(80) + 4}"  fill="var(--text-dim)" font-size="10">80%</text>
        <!-- Line -->
        <polyline points="${points}" fill="none" stroke="${color}" stroke-width="3"/>
        ${circles}
      </svg>
    `;
  },

  /**
   * Render a simple workload horizontal bar list
   * @param {string} containerId
   * @param {Array<{name, hours, maxHours}>} data
   */
  renderWorkloadBars(containerId, data) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = data.map(f => `
      <div style="margin-bottom:12px;">
        <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:4px;">
          <span>${f.name}</span>
          <strong>${f.hours} hrs/wk ${f.hours > 20 ? '⚠' : ''}</strong>
        </div>
        <div style="height:8px; background:var(--bg-panel); border-radius:4px; overflow:hidden;">
          <div style="height:100%; width:${(f.hours / 24) * 100}%; background:${f.hours > 20 ? 'var(--amber)' : 'var(--emerald)'};"></div>
        </div>
      </div>
    `).join('');
  }
};
