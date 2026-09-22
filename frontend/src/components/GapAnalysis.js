/**
 * GapAnalysis Component - Criterion 3 CO2 Gap & Remedial Action Tracker
 */

export function renderGapAnalysis(attainmentSummary) {
  const { weakCO } = attainmentSummary;

  return `
    <div class="gap-alert-card">
      <div class="gap-alert-header">
        <div class="gap-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <span>CRITICAL GAP IDENTIFIED — ${weakCO.id} Attainment Deficit</span>
        </div>
        <span class="badge badge-warning">Target: ${weakCO.target}% | Actual: ${weakCO.attainment}%</span>
      </div>

      <p class="gap-description">
        <strong>Root Cause Analysis:</strong> ${weakCO.reason}
      </p>

      <div class="action-item-box">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #991b1b; text-transform: uppercase;">Recommended Corrective Action (Criterion 3.4)</span>
          <p style="font-size: 13px; font-weight: 600; color: #7f1d1d; margin-top: 2px;">
            ${weakCO.recommendedAction}
          </p>
          <div style="font-size: 12px; color: #991b1b; margin-top: 4px; display: flex; gap: 16px;">
            <span>Assigned Faculty: <strong>${weakCO.assignedFaculty}</strong></span>
            <span>Target Completion: <strong>Oct 15, 2026</strong></span>
          </div>
        </div>

        <button class="btn btn-outline-danger btn-sm" id="toggle-action-status">
          <span>Status: ${weakCO.status === 'IN_PROGRESS' ? 'In Progress ⏳' : 'Completed ✓'}</span>
        </button>
      </div>
    </div>
  `;
}
