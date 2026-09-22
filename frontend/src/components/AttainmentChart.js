/**
 * AttainmentChart Component - CO Attainment Bars & Donut Chart Visuals
 */

export function renderAttainmentCharts(outcomes, attainment) {
  const barsHtml = outcomes.map(co => {
    const isGap = co.actualAttainment < co.target;
    const fillClass = isGap ? 'warning' : 'success';
    
    return `
      <div class="attainment-bar-item">
        <div class="bar-meta">
          <span>${co.id} (${co.taxonomy})</span>
          <span class="${isGap ? 'text-warning' : 'text-success'}">${co.actualAttainment}%</span>
        </div>
        <div class="bar-track">
          <div class="target-line" title="Target: 70%"></div>
          <div class="bar-fill ${fillClass}" style="width: ${co.actualAttainment}%;">
            ${co.actualAttainment}%
          </div>
        </div>
        <div class="bar-target-info">Target: ${co.target}% ${isGap ? '⚠️ [GAP IDENTIFIED]' : '✓ Met'}</div>
      </div>
    `;
  }).join('');

  return `
    <div class="dashboard-grid">
      <!-- Card 1: CO - PO Attainment Overview -->
      <div class="card">
        <div class="card-header">
          <div>
            <h2 class="card-title">CO Attainment Overview</h2>
            <span class="card-subtitle">Actual calculated attainment vs 70% threshold</span>
          </div>
          <button class="btn btn-secondary btn-sm" id="view-attainment-details">View Details</button>
        </div>

        <div class="attainment-bar-list">
          ${barsHtml}
        </div>
      </div>

      <!-- Card 2: Donut Compliance Chart -->
      <div class="card">
        <div class="card-header">
          <div>
            <h2 class="card-title">Criterion 3 Status</h2>
            <span class="card-subtitle">Compliance breakdown</span>
          </div>
        </div>

        <div class="chart-container">
          <svg width="180" height="180" viewBox="0 0 100 100">
            <!-- Donut Base Background Track -->
            <circle cx="50" cy="50" r="38" fill="none" stroke="#f1f5f9" stroke-width="12" />
            <!-- Compliant Segment 70% (Green/Blue) -->
            <circle cx="50" cy="50" r="38" fill="none" stroke="#2563eb" stroke-width="12"
                    stroke-dasharray="167 71" stroke-dashoffset="0" transform="rotate(-90 50 50)"/>
            <!-- In Progress Segment 20% (Amber) -->
            <circle cx="50" cy="50" r="38" fill="none" stroke="#f59e0b" stroke-width="12"
                    stroke-dasharray="48 190" stroke-dashoffset="-167" transform="rotate(-90 50 50)"/>
            <!-- Non-Compliant Segment 10% (Red) -->
            <circle cx="50" cy="50" r="38" fill="none" stroke="#ef4444" stroke-width="12"
                    stroke-dasharray="24 214" stroke-dashoffset="-215" transform="rotate(-90 50 50)"/>
          </svg>
          <div class="donut-center-text">
            <div class="donut-percentage">82%</div>
            <div class="donut-label">Readiness</div>
          </div>
        </div>

        <div class="donut-legend">
          <div class="legend-item">
            <span><span class="legend-dot" style="background: #2563eb;"></span> Compliant</span>
            <strong>70%</strong>
          </div>
          <div class="legend-item">
            <span><span class="legend-dot" style="background: #f59e0b;"></span> In Progress</span>
            <strong>20%</strong>
          </div>
          <div class="legend-item">
            <span><span class="legend-dot" style="background: #ef4444;"></span> Non-Compliant</span>
            <strong>10%</strong>
          </div>
        </div>
      </div>

      <!-- Card 3: Criteria Sub-requirements -->
      <div class="card">
        <div class="card-header">
          <div>
            <h2 class="card-title">C3 Sub-requirements</h2>
            <span class="card-subtitle">NBA Audit Readiness</span>
          </div>
        </div>

        <div class="sub-progress-list">
          <div class="sub-progress-item">
            <span class="sub-title">C3.1 CO Formulation & PEO/PO Mapping</span>
            <span class="sub-score">100%</span>
          </div>
          <div class="sub-progress-item">
            <span class="sub-title">C3.2 Attainment of COs</span>
            <span class="sub-score">85%</span>
          </div>
          <div class="sub-progress-item">
            <span class="sub-title">C3.3 Attainment of POs & PSOs</span>
            <span class="sub-score">78%</span>
          </div>
          <div class="sub-progress-item">
            <span class="sub-title">C3.4 Remedial Actions & Continuous Improvement</span>
            <span class="sub-score text-warning">70%</span>
          </div>
        </div>
      </div>
    </div>
  `;
}
