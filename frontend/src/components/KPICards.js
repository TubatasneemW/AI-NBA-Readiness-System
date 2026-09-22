/**
 * KPICards Component - Criterion 3 High-Level Metrics
 */

export function renderKPICards(attainment, outcomes, assessments, students) {
  const totalCOs = outcomes.length;
  const metCOs = outcomes.filter(o => o.actualAttainment >= o.target).length;
  const avgAttainment = (outcomes.reduce((acc, o) => acc + o.actualAttainment, 0) / totalCOs).toFixed(1);

  return `
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-title">
          <span>Overall C3 Readiness</span>
          <span class="badge badge-success">COMPLIANT</span>
        </div>
        <div class="kpi-value-row">
          <span class="kpi-value" style="color: #2563eb;">${attainment.overallReadiness}%</span>
        </div>
        <div class="kpi-subtext">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span class="text-success">Good Accreditation Standing</span>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-title">
          <span>CO Attainment Met</span>
          <span class="badge badge-info">Target: 70.0%</span>
        </div>
        <div class="kpi-value-row">
          <span class="kpi-value">${metCOs} / ${totalCOs} COs</span>
        </div>
        <div class="kpi-subtext">
          <span>Avg Attainment: <strong>${avgAttainment}%</strong></span>
        </div>
      </div>

      <div class="kpi-card">
        <div class="kpi-title">
          <span>Assessments Tracked</span>
          <span class="badge badge-success">Completed</span>
        </div>
        <div class="kpi-value-row">
          <span class="kpi-value">${assessments.length} / ${assessments.length}</span>
        </div>
        <div class="kpi-subtext">
          <span>CIE-I, CIE-II, Assign, Lab</span>
        </div>
      </div>

      <div class="kpi-card" style="border-left: 4px solid #ef4444;">
        <div class="kpi-title">
          <span>CO Attainment Gap</span>
          <span class="badge badge-warning">1 Action Req</span>
        </div>
        <div class="kpi-value-row">
          <span class="kpi-value text-warning">CO2 (61.0%)</span>
        </div>
        <div class="kpi-subtext text-warning">
          <span>Gap: -9.0% below target</span>
        </div>
      </div>
    </div>
  `;
}
