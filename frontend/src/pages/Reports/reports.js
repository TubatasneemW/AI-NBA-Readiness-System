/* ====================================================
   ACCREDIX — Reports Page Module (Vanilla JS)
   ==================================================== */

const ReportsPage = {
  name: 'reports',
  title: 'SAR Document Generator & Export Engine',
  init: function(appState) {
    console.log('[Accredix] Reports page loaded');
  },
  availableReports: [
    { title: 'ACCREDIX — System High-Level Architecture Diagram PDF', file: 'ACCREDIX_System_High_Level_Architecture_Diagram.pdf' },
    { title: 'ACCREDIX — System Architecture & Technical Guide PDF', file: 'ACCREDIX_System_Architecture_Doc.pdf' },
    { title: 'Self Assessment Report (SAR) - Full Draft', file: 'NBA_SAR_Full_Draft_CSE.pdf' },
    { title: 'Criterion 3: CO-PO Attainment Summary', file: 'C3_CO_PO_Attainment_Report.pdf' },
    { title: 'Criterion 4: Student Success & Support Matrix', file: 'C4_Student_Performance_Matrix.pdf' },
    { title: 'Criterion 5: Faculty Qualification & Cadre Audit', file: 'C5_Faculty_Audit_Report.pdf' },
    { title: 'Criterion 6: Research & Publication Ledger', file: 'C6_Faculty_Contributions_Ledger.pdf' }
  ]
};

window.ReportsPage = ReportsPage;
