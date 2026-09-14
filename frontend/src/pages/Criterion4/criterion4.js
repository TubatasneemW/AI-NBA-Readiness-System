/* ====================================================
   ACCREDIX — Criterion 4 Page Module (Vanilla JS)
   ==================================================== */

const Criterion4Page = {
  name: 'criterion-4',
  title: 'Criterion 4 — Student Performance & Early Intervention Intelligence',
  init: function(appState) {
    console.log('[Accredix] Criterion 4 page loaded');
  },
  getAtRiskStudents: function(appState) {
    return appState.students.filter(s => s.riskLevel === 'High' || s.riskLevel === 'Medium');
  }
};

window.Criterion4Page = Criterion4Page;
