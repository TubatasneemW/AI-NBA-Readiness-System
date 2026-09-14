/* ACCREDIX PLATFORM ENGINE & DYNAMIC STATE MANAGEMENT */

// GLOBAL APPLICATION STATE
const appState = {
  activeTab: 'dashboard',
  activeC3Subtab: 'attainment',
  studentRiskFilter: 'ALL',
  c6TypeFilter: 'ALL',
  evidenceStatusFilter: 'ALL',
  
  // Overall Health Data
  departmentHealth: {
    readinessScore: 87,
    scoreChange: 6.4,
    passCount: 82,
    warningCount: 14,
    criticalCount: 7
  },

  // Criterion 3 Data
  c3Data: {
    score: 82,
    courseCode: "21CS61",
    courseName: "Machine Learning",
    targetThreshold: 70.0,
    outcomes: [
      { id: "CO1", code: "CO1", description: "Explain ML fundamentals & learning models", attainmentPercent: 82.0, targetPercent: 70.0, status: "PASS" },
      { id: "CO2", code: "CO2", description: "Apply Machine Learning algorithms (SVM, Decision Trees)", attainmentPercent: 61.0, targetPercent: 70.0, status: "CRITICAL" },
      { id: "CO3", code: "CO3", description: "Evaluate & tune model hyperparameters", attainmentPercent: 78.0, targetPercent: 70.0, status: "PASS" },
      { id: "CO4", code: "CO4", description: "Build end-to-end ML project pipeline", attainmentPercent: 84.0, targetPercent: 70.0, status: "PASS" }
    ],
    questionMappings: [
      { qNo: "Q1", co: "CO1", marks: 5, blooms: "Understand", difficulty: "Easy", link: "Midterm_Q1_Proof.pdf" },
      { qNo: "Q2", co: "CO2", marks: 10, blooms: "Apply", difficulty: "Medium", link: "Midterm_Q2_Proof.pdf" },
      { qNo: "Q3", co: "CO2", marks: 10, blooms: "Apply", difficulty: "Hard", link: "Midterm_Q3_Proof.pdf" },
      { qNo: "Q4", co: "CO3", marks: 5, blooms: "Analyze", difficulty: "Medium", link: "Midterm_Q4_Proof.pdf" },
      { qNo: "Q5", co: "CO4", marks: 10, blooms: "Evaluate", difficulty: "Hard", link: "Midterm_Q5_Proof.pdf" }
    ],
    copoMatrix: [
      { co: "CO1", po1: 3, po2: 2, po3: 1, po4: 0, po5: 0, pso1: 2, pso2: 1 },
      { co: "CO2", po1: 2, po2: 3, po3: 3, po4: 1, po5: 0, pso1: 3, pso2: 2 },
      { co: "CO3", po1: 1, po2: 2, po3: 3, po4: 2, po5: 1, pso1: 2, pso2: 3 },
      { co: "CO4", po1: 2, po2: 2, po3: 3, po4: 3, po5: 2, pso1: 3, pso2: 3 }
    ]
  },

  // Criterion 4 Students Data
  students: [
    { usn: "1BM23CS001", name: "Anagha D K", cgpa: 8.4, attendance: 88, internalMarks: 82, backlogs: 0, activitiesCount: 4, riskLevel: "ON_TRACK", semester: "S6" },
    { usn: "1BM23CS002", name: "Rohan V. Sharma", cgpa: 6.2, attendance: 62, internalMarks: 54, backlogs: 2, activitiesCount: 1, riskLevel: "HIGH_ATTENTION", semester: "S6" },
    { usn: "1BM23CS003", name: "Priya Nair", cgpa: 7.1, attendance: 76, internalMarks: 64, backlogs: 1, activitiesCount: 2, riskLevel: "NEEDS_MONITORING", semester: "S6" },
    { usn: "1BM23CS004", name: "Aditya Kumar", cgpa: 9.1, attendance: 94, internalMarks: 91, backlogs: 0, activitiesCount: 6, riskLevel: "ON_TRACK", semester: "S6" },
    { usn: "1BM23CS005", name: "Sneha Reddy", cgpa: 5.8, attendance: 58, internalMarks: 48, backlogs: 3, activitiesCount: 0, riskLevel: "HIGH_ATTENTION", semester: "S6" },
    { usn: "1BM23CS006", name: "Karthik Gowda", cgpa: 7.8, attendance: 82, internalMarks: 74, backlogs: 0, activitiesCount: 3, riskLevel: "ON_TRACK", semester: "S6" }
  ],

  // Criterion 5 Faculty Data
  faculty: [
    { id: "F01", name: "Dr. K. S. Sharma", designation: "Professor", qualification: "Ph.D.", experience: 18, workload: 16, completeness: 100, status: "VERIFIED" },
    { id: "F02", name: "Dr. XYZ", designation: "Associate Professor", qualification: "Ph.D.", experience: 12, workload: 18, completeness: 92, status: "NEEDS_REVIEW", missingDoc: "Updated experience record" },
    { id: "F03", name: "Dr. ABC", designation: "Professor", qualification: "Ph.D.", experience: 20, workload: 14, completeness: 100, status: "VERIFIED" },
    { id: "F04", name: "Prof. PQR", designation: "Assistant Professor", qualification: "M.Tech", experience: 6, workload: 22, completeness: 71, status: "MISSING", missingDoc: "Ph.D. registration / Appointment order" }
  ],

  // Criterion 6 Contributions Data
  contributions: [
    { id: "C6-01", title: "Deep Learning for Medical Image Segmentation", type: "Publication", facultyName: "Dr. XYZ", publisher: "IEEE Trans. Medical Imaging", date: "2025-04-12", status: "VERIFIED", file: "IEEE_Paper_XYZ_2025.pdf" },
    { id: "C6-02", title: "Smart Edge AI IoT Gateway for Microgrids", type: "Patent", facultyName: "Dr. ABC", publisher: "Indian Patent Office", date: "2025-02-18", status: "VERIFIED", file: "Patent_Grant_ABC_2025.pdf" },
    { id: "C6-03", title: "Advanced Machine Learning & LLM Workshop", type: "FDP", facultyName: "Dr. XYZ", publisher: "IIT Bombay", date: "2025-06-10", status: "VERIFIED", file: "FDP_Cert_XYZ_IITB.pdf" },
    { id: "C6-04", title: "Cybersecurity & Neural Network Defense", type: "Research Project", facultyName: "Dr. K. S. Sharma", publisher: "DST SERB Funding", date: "2025-01-15", status: "NEEDS_REVIEW", file: "DST_Funding_Grant.pdf" }
  ],

  // Action Items
  actionItems: [
    {
      id: "ACT-101",
      criterion: "C3",
      title: "CO2 Attainment Remedial Action Plan",
      problem: "CO2 (Apply ML Algorithms) attainment is at 61.0% (Target 70%). Low midterm scores in SVM & decision tree numericals.",
      recommendedAction: "Conduct 2 additional hands-on practical sessions and a targeted remedial quiz for at-risk students.",
      ownerName: "Dr. XYZ",
      deadline: "2025-09-15",
      priority: "CRITICAL",
      status: "IN_PROGRESS",
      requiredEvidence: "Remedial attendance log, tutorial question sheet, reassessment mark list",
      coTargetRef: "CO2"
    },
    {
      id: "ACT-102",
      criterion: "C5",
      title: "Incomplete Faculty Qualification Document Upload",
      problem: "Prof. PQR faculty profile completeness is at 71%. Missing appointment order and M.Tech degree certificate proof.",
      recommendedAction: "Upload verified PDF copies of appointment order and Master's degree certificate.",
      ownerName: "Department Admin",
      deadline: "2025-09-10",
      priority: "HIGH",
      status: "PENDING",
      requiredEvidence: "Appointment_Order_PQR.pdf"
    },
    {
      id: "ACT-103",
      criterion: "C6",
      title: "Pending Publication Evidence Verification",
      problem: "3 recent journal publications entered by faculty lack verified IEEE/Scopus DOI pdf proof.",
      recommendedAction: "Submit published PDF paper copies with DOI link matching Scopus indexing.",
      ownerName: "Dr. ABC",
      deadline: "2025-09-20",
      priority: "MEDIUM",
      status: "PENDING",
      requiredEvidence: "Scopus_Indexed_Paper.pdf"
    }
  ],

  // Audit Logs
  activityLogs: [
    { text: "Dr. XYZ updated CO2 remedial action progress", time: "10 mins ago", type: "action" },
    { text: "AI parsed and verified FDP_Cert_XYZ_IITB.pdf", time: "1 hour ago", type: "ai" },
    { text: "HOD executed Virtual NBA Inspection simulation (Score 87%)", time: "3 hours ago", type: "audit" },
    { text: "Uploaded Semester VI University Result Sheet CSV", time: "Yesterday", type: "upload" }
  ]
};

// INITIALIZATION
document.addEventListener('DOMContentLoaded', () => {
  renderDashboard();
  renderC3View();
  renderC4View();
  renderC5View();
  renderC6View();
  renderEvidenceView();
  renderActionCenterView();
  renderActivityTimeline();
  setupGlobalSearch();
});

// TAB SWITCHING ROUTER
function switchTab(tabId) {
  appState.activeTab = tabId;
  
  // Update sidebar active link
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(el => {
    if (el.getAttribute('data-tab') === tabId) {
      el.classList.add('active');
    } else {
      el.classList.remove('active');
    }
  });

  // Toggle tab views
  document.querySelectorAll('.tab-view').forEach(view => {
    if (view.id === `view-${tabId}`) {
      view.classList.remove('hidden');
    } else {
      view.classList.add('hidden');
    }
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// C3 SUBTAB SWITCHING
function switchC3Subtab(subtabId) {
  appState.activeC3Subtab = subtabId;
  document.querySelectorAll('.subtab-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  event.target.classList.add('active');

  document.querySelectorAll('.subtab-content').forEach(content => {
    if (content.id === `c3-subtab-${subtabId}`) {
      content.classList.remove('hidden');
    } else {
      content.classList.add('hidden');
    }
  });
}

// DASHBOARD RENDERING — NBA DIGITAL TWIN
function renderDashboard() {
  renderKpiRow();
  renderCopoBarChart();
  renderCriteriaDonut();
  renderCriteriaProgressList();
  renderFacultyOverview();
  renderStudentOverview();
  renderInfraOverview();
  renderRecentAlerts();
  
  // Legacy gap list if element exists
  const gapListEl = document.getElementById('dashboard-gap-list');
  if (gapListEl) {
    gapListEl.innerHTML = appState.actionItems.map(item => `
      <div class="gap-item ${item.priority.toLowerCase()}">
        <div class="gap-info">
          <span class="gap-title">${item.title}</span>
          <span class="gap-meta">Criterion ${item.criterion} • Owner: ${item.ownerName} • Due: ${item.deadline}</span>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="switchTab('action-center')">Resolve Action</button>
      </div>
    `).join('');
  }
}

// 1. KPI ROW (6 CARDS)
function renderKpiRow() {
  const kpiRowEl = document.getElementById('kpi-row');
  if (!kpiRowEl) return;

  const kpis = [
    {
      title: "Overall NBA Readiness",
      score: `${appState.departmentHealth.readinessScore}%`,
      badgeText: "Good",
      badgeClass: "blue",
      fillWidth: `${appState.departmentHealth.readinessScore}%`,
      barClass: "",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>`
    },
    {
      title: "Student Success Rate",
      score: "84.2%",
      badgeText: "+3.1% YoY",
      badgeClass: "green",
      fillWidth: "84.2%",
      barClass: "green",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>`
    },
    {
      title: "Faculty Cadre & SFR",
      score: "1:15",
      badgeText: "Compliant",
      badgeClass: "green",
      fillWidth: "90%",
      barClass: "green",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`
    },
    {
      title: "Research & Publications",
      score: "38",
      badgeText: "28 Scopus",
      badgeClass: "blue",
      fillWidth: "76%",
      barClass: "",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>`
    },
    {
      title: "Infrastructure & Labs",
      score: "92%",
      badgeText: "6 AI Labs",
      badgeClass: "green",
      fillWidth: "92%",
      barClass: "green",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#06b6d4" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>`
    },
    {
      title: "CO-PO Attainment",
      score: `${appState.c3Data.score}%`,
      badgeText: appState.c3Data.score < 85 ? "1 Gap" : "Pass",
      badgeClass: appState.c3Data.score < 85 ? "yellow" : "green",
      fillWidth: `${appState.c3Data.score}%`,
      barClass: appState.c3Data.score < 85 ? "amber" : "green",
      icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>`
    }
  ];

  kpiRowEl.innerHTML = kpis.map(kpi => `
    <div class="kpi-card">
      <div class="kpi-head">
        <span class="kpi-title">${kpi.title}</span>
        <div class="kpi-icon-wrap">${kpi.icon}</div>
      </div>
      <div class="kpi-score">${kpi.score}</div>
      <div class="kpi-status-row">
        <span class="kpi-badge ${kpi.badgeClass}">${kpi.badgeText}</span>
      </div>
      <div class="kpi-bar">
        <div class="kpi-bar-fill ${kpi.barClass}" style="width: ${kpi.fillWidth};"></div>
      </div>
    </div>
  `).join('');
}

// 2. CO-PO ATTAINMENT BAR CHART (SVG)
function renderCopoBarChart() {
  const chartEl = document.getElementById('copo-bar-chart');
  if (!chartEl) return;

  const data = [
    { label: "CO1", target: 70, attainment: 82 },
    { label: "CO2", target: 70, attainment: appState.c3Data.outcomes.find(c => c.code === "CO2")?.attainmentPercent || 61 },
    { label: "CO3", target: 70, attainment: 78 },
    { label: "CO4", target: 70, attainment: 84 },
    { label: "CO5", target: 70, attainment: 76 },
    { label: "CO6", target: 70, attainment: 88 }
  ];

  chartEl.innerHTML = data.map(item => {
    const isGap = item.attainment < item.target;
    const barColor = isGap ? 'var(--crimson)' : 'var(--emerald)';

    return `
      <div class="copo-bar-group">
        <div class="copo-bars">
          <!-- Target bar -->
          <div class="copo-bar target-bar" style="height: ${item.target}%;" title="Target: ${item.target}%">
            <span class="bar-val">${item.target}%</span>
          </div>
          <!-- Attainment bar -->
          <div class="copo-bar attainment-bar ${isGap ? 'critical' : ''}" style="height: ${item.attainment}%; background: ${barColor};" title="Attainment: ${item.attainment}%">
            <span class="bar-val">${item.attainment}%</span>
          </div>
        </div>
        <div class="copo-label">${item.label}</div>
      </div>
    `;
  }).join('');
}

// 3. CRITERIA DONUT CHART (SVG)
function renderCriteriaDonut() {
  const wrapEl = document.getElementById('criteria-donut-wrap');
  if (!wrapEl) return;

  wrapEl.innerHTML = `
    <div class="donut-svg-box">
      <svg width="150" height="150" viewBox="0 0 150 150">
        <!-- Background circle -->
        <circle cx="75" cy="75" r="55" fill="none" stroke="#f1f5f9" stroke-width="18"/>
        <!-- Slices -->
        <!-- S1: Compliant 70% -> strokeDasharray offset -->
        <circle cx="75" cy="75" r="55" fill="none" stroke="#1a56db" stroke-width="18"
                stroke-dasharray="241.9 103.7" stroke-dashoffset="86" stroke-linecap="round"/>
        <!-- S2: In Progress 20% -->
        <circle cx="75" cy="75" r="55" fill="none" stroke="#f59e0b" stroke-width="18"
                stroke-dasharray="69.1 276.5" stroke-dashoffset="-155.9" stroke-linecap="round"/>
        <!-- S3: Non Compliant 10% -->
        <circle cx="75" cy="75" r="55" fill="none" stroke="#ef4444" stroke-width="18"
                stroke-dasharray="34.5 311.1" stroke-dashoffset="-225" stroke-linecap="round"/>
      </svg>
      <div class="donut-center-text">
        <span class="donut-val">78%</span>
        <span class="donut-lbl">Readiness</span>
      </div>
    </div>

    <div class="donut-legend">
      <div class="legend-row">
        <div class="legend-left">
          <div class="legend-color-dot" style="background: #1a56db;"></div>
          <span>Compliant</span>
        </div>
        <strong>70%</strong>
      </div>
      <div class="legend-row">
        <div class="legend-left">
          <div class="legend-color-dot" style="background: #f59e0b;"></div>
          <span>In Progress</span>
        </div>
        <strong>20%</strong>
      </div>
      <div class="legend-row">
        <div class="legend-left">
          <div class="legend-color-dot" style="background: #ef4444;"></div>
          <span>Non-Compliant</span>
        </div>
        <strong>10%</strong>
      </div>
    </div>
  `;
}

// 4. CRITERIA WISE PROGRESS LIST
function renderCriteriaProgressList() {
  const listEl = document.getElementById('criteria-progress-list');
  if (!listEl) return;

  const items = [
    { title: "Criterion 1 — Vision, Mission & PEOs", score: 95, status: "Compliant", color: "green" },
    { title: "Criterion 2 — Program Curriculum & Teaching", score: 88, status: "Compliant", color: "green" },
    { title: "Criterion 3 — Course & Program Outcomes", score: appState.c3Data.score, status: appState.c3Data.score >= 85 ? "Compliant" : "In Progress", color: appState.c3Data.score >= 85 ? "green" : "amber" },
    { title: "Criterion 4 — Student Performance", score: 85, status: "Compliant", color: "green" },
    { title: "Criterion 5 — Faculty Contributions", score: 76, status: "In Progress", color: "amber" },
    { title: "Criterion 6 — Facilities & Technical Support", score: 92, status: "Compliant", color: "green" },
    { title: "Criterion 7 — Continuous Improvement", score: 70, status: "In Progress", color: "amber" }
  ];

  listEl.innerHTML = items.map(item => `
    <div class="progress-item">
      <div class="progress-header">
        <span class="progress-title">${item.title}</span>
        <span class="progress-score">${item.score}%</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill ${item.color}" style="width: ${item.score}%;"></div>
      </div>
    </div>
  `).join('');
}

// 5. FACULTY OVERVIEW
function renderFacultyOverview() {
  const el = document.getElementById('faculty-overview-panel');
  if (!el) return;

  el.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <div>
        <div style="font-size: 20px; font-weight: 700; font-family: var(--font-heading); color: var(--slate-900);">24</div>
        <div style="font-size: 11px; color: var(--slate-500);">Total Faculty Members</div>
      </div>
      <span class="kpi-badge green">1:15 SFR</span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 10px; display: flex; justify-content: space-between;">
      <span>Ph.D Holders: <strong>18 (75%)</strong></span>
      <span>Avg Experience: <strong>11.4 Yrs</strong></span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 12px; display: flex; justify-content: space-between;">
      <span>Cadre Ratio (P:Assoc:Asst): <strong>1:2:6</strong></span>
      <span>Profile Ready: <strong style="color: var(--emerald);">92%</strong></span>
    </div>
    <div class="kpi-bar">
      <div class="kpi-bar-fill green" style="width: 92%;"></div>
    </div>
  `;
}

// 6. STUDENT OVERVIEW
function renderStudentOverview() {
  const el = document.getElementById('student-overview-panel');
  if (!el) return;

  el.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <div>
        <div style="font-size: 20px; font-weight: 700; font-family: var(--font-heading); color: var(--slate-900);">240</div>
        <div style="font-size: 11px; color: var(--slate-500);">Total Enrolled Students (B.E AI & ML)</div>
      </div>
      <span class="kpi-badge green">91.4% Pass Rate</span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 10px; display: flex; justify-content: space-between;">
      <span>Placement Rate: <strong style="color: var(--emerald);">86.5%</strong></span>
      <span>Higher Studies: <strong>8.2%</strong></span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 12px; display: flex; justify-content: space-between;">
      <span>At Risk Students: <strong style="color: var(--crimson);">2 Needing Action</strong></span>
      <span>Avg CGPA: <strong>8.12</strong></span>
    </div>
    <div class="kpi-bar">
      <div class="kpi-bar-fill green" style="width: 86%;"></div>
    </div>
  `;
}

// 7. INFRASTRUCTURE OVERVIEW
function renderInfraOverview() {
  const el = document.getElementById('infra-overview-panel');
  if (!el) return;

  el.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
      <div>
        <div style="font-size: 20px; font-weight: 700; font-family: var(--font-heading); color: var(--slate-900);">6 / 6</div>
        <div style="font-size: 11px; color: var(--slate-500);">Smart Classrooms & Specialized Labs</div>
      </div>
      <span class="kpi-badge green">92% Ready</span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 10px; display: flex; justify-content: space-between;">
      <span>AI HPC Cluster: <strong style="color: var(--emerald);">60 GPUs Active</strong></span>
      <span>IoT Lab: <strong>Functional</strong></span>
    </div>
    <div style="font-size: 12px; color: var(--slate-600); margin-bottom: 12px; display: flex; justify-content: space-between;">
      <span>Safety & Accessibility: <strong style="color: var(--emerald);">100% Passed</strong></span>
      <span>Department Books: <strong>1,450+</strong></span>
    </div>
    <div class="kpi-bar">
      <div class="kpi-bar-fill green" style="width: 92%;"></div>
    </div>
  `;
}

// 8. RECENT ALERTS / NOTIFICATIONS
function renderRecentAlerts() {
  const listEl = document.getElementById('recent-alerts-list');
  if (!listEl) return;

  const alerts = [
    {
      title: "CO2 Attainment Gap Alert",
      text: "Machine Learning (21CS61) CO2 attainment is 61% (Target 70%).",
      time: "10m ago",
      type: "critical",
      icon: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`
    },
    {
      title: "Faculty Document Pending",
      text: "Prof. PQR qualification proof upload required for Criterion 5.",
      time: "1h ago",
      type: "warning",
      icon: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`
    },
    {
      title: "IEEE Research Paper Verified",
      text: "Evidence engine parsed & verified Dr. XYZ publication PDF.",
      time: "3h ago",
      type: "success",
      icon: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`
    }
  ];

  listEl.innerHTML = alerts.map(alert => `
    <div class="alert-item ${alert.type}">
      <div class="alert-icon">${alert.icon}</div>
      <div class="alert-content">
        <div class="alert-title">${alert.title} <span class="alert-time">${alert.time}</span></div>
        <div class="alert-desc">${alert.text}</div>
      </div>
    </div>
  `).join('');
}

function renderActivityTimeline() {
  const timelineEl = document.getElementById('dashboard-activity-timeline');
  if (!timelineEl) return;

  timelineEl.innerHTML = appState.activityLogs.map(log => `
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <span class="timeline-text">${log.text}</span>
        <span class="timeline-time">${log.time}</span>
      </div>
    </div>
  `).join('');
}

// C3 ASSESSMENT VIEW RENDERING
function renderC3View() {
  const coBarsListEl = document.getElementById('co-bars-list');
  if (!coBarsListEl) return;

  coBarsListEl.innerHTML = appState.c3Data.outcomes.map(co => {
    const isWeak = co.attainmentPercent < appState.c3Data.targetThreshold;
    const barColor = isWeak ? 'var(--crimson)' : 'var(--emerald)';
    const statusChip = isWeak ? `<span class="badge-status status-critical">WEAK: -${(appState.c3Data.targetThreshold - co.attainmentPercent).toFixed(1)}%</span>` : `<span class="badge-status status-pass">PASS</span>`;
    
    return `
      <div class="co-bar-item" style="margin-bottom: 16px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <div>
            <strong style="font-size: 14px; font-family: var(--font-heading);">${co.code} — ${co.description}</strong>
          </div>
          <div>${statusChip} <strong style="font-family: var(--font-mono); font-size: 16px; margin-left: 10px;">${co.attainmentPercent}%</strong></div>
        </div>
        <div style="height: 12px; background: var(--bg-panel); border-radius: 6px; overflow: hidden; position: relative;">
          <div style="height: 100%; width: ${co.attainmentPercent}%; background: ${barColor}; border-radius: 6px; transition: width 0.8s ease;"></div>
          <div style="position: absolute; top: 0; bottom: 0; left: 70%; width: 2px; background: var(--amber); box-shadow: 0 0 5px var(--amber);" title="Target 70%"></div>
        </div>
      </div>
    `;
  }).join('');

  // Question Mapping Table
  const qTbody = document.getElementById('question-mapping-tbody');
  if (qTbody) {
    qTbody.innerHTML = appState.c3Data.questionMappings.map(q => `
      <tr>
        <td><strong>${q.qNo}</strong></td>
        <td><span class="badge-pill">${q.co}</span></td>
        <td>${q.marks} Marks</td>
        <td><span class="chip-dot" style="background: var(--indigo); display: inline-block;"></span> ${q.blooms}</td>
        <td><span class="badge-chip ${q.difficulty === 'Hard' ? 'red' : 'amber'}">${q.difficulty}</span></td>
        <td><a href="#" style="color: var(--indigo); font-weight: 600;" onclick="alert('Viewing verified evidence PDF: ${q.link}')">📄 ${q.link}</a></td>
      </tr>
    `).join('');
  }

  // CO-PO Matrix Heatmap
  const matrixTable = document.getElementById('copo-heatmap-table');
  if (matrixTable) {
    matrixTable.innerHTML = `
      <thead>
        <tr>
          <th>Course Outcome</th>
          <th>PO1</th><th>PO2</th><th>PO3</th><th>PO4</th><th>PO5</th><th>PSO1</th><th>PSO2</th>
        </tr>
      </thead>
      <tbody>
        ${appState.c3Data.copoMatrix.map(row => `
          <tr>
            <td><strong>${row.co}</strong></td>
            <td class="heatmap-cell level-${row.po1}">${row.po1 || '-'}</td>
            <td class="heatmap-cell level-${row.po2}">${row.po2 || '-'}</td>
            <td class="heatmap-cell level-${row.po3}">${row.po3 || '-'}</td>
            <td class="heatmap-cell level-${row.po4}">${row.po4 || '-'}</td>
            <td class="heatmap-cell level-${row.po5}">${row.po5 || '-'}</td>
            <td class="heatmap-cell level-${row.pso1}">${row.pso1 || '-'}</td>
            <td class="heatmap-cell level-${row.pso2}">${row.pso2 || '-'}</td>
          </tr>
        `).join('')}
      </tbody>
    `;
  }
}

// REMEDIAL ACTION DYNAMIC RESOLUTION FOR CO2 (SHOWS LIVE GAP CLOSING!)
function createRemedialActionForCO2() {
  alert("Action Item ACT-101 created for Dr. XYZ! Directing to Action Center to upload remedial proof and close gap...");
  switchTab('action-center');
}

function resolveActionItem(actionId) {
  const item = appState.actionItems.find(a => a.id === actionId);
  if (item) {
    item.status = "COMPLETED";
    
    if (item.coTargetRef === "CO2") {
      // Dynamic gap resolution! Update CO2 attainment to 73.0%
      const co2 = appState.c3Data.outcomes.find(c => c.code === "CO2");
      if (co2) {
        co2.attainmentPercent = 73.0;
        co2.status = "PASS";
      }
      appState.c3Data.score = 88;
      appState.departmentHealth.readinessScore = 91;
      
      // Update UI elements live!
      document.getElementById('main-readiness-score').innerText = "91%";
      document.getElementById('dashboard-c3-score').innerText = "88%";
      document.getElementById('weak-co-panel').style.borderColor = "var(--emerald)";
      document.getElementById('weak-co-title').innerText = "RESOLUTION VERIFIED: CO2 Attainment upgraded to 73.0% (PASS ✓)";
      
      appState.activityLogs.unshift({ text: "Dr. XYZ completed CO2 remedial action. Attainment updated to 73.0% (PASS)", time: "Just now", type: "action" });
    }

    renderActionCenterView();
    renderC3View();
    renderDashboard();
    renderActivityTimeline();
    alert(`Action ${actionId} successfully resolved and verified by Evidence Engine!`);
  }
}

// C4 STUDENTS VIEW RENDERING
function renderC4View() {
  const tbody = document.getElementById('student-directory-tbody');
  if (!tbody) return;

  const filtered = appState.students.filter(s => {
    if (appState.studentRiskFilter === 'ALL') return true;
    return s.riskLevel === appState.studentRiskFilter;
  });

  tbody.innerHTML = filtered.map(s => {
    let riskBadge = `<span class="badge-status status-pass">ON TRACK 🟢</span>`;
    if (s.riskLevel === 'HIGH_ATTENTION') riskBadge = `<span class="badge-status status-critical">HIGH ATTENTION 🔴</span>`;
    if (s.riskLevel === 'NEEDS_MONITORING') riskBadge = `<span class="badge-status status-warning">NEEDS MONITORING 🟡</span>`;

    return `
      <tr>
        <td><strong style="font-family: var(--font-mono);">${s.usn}</strong></td>
        <td>${s.name}</td>
        <td><strong>${s.cgpa}</strong></td>
        <td>${s.attendance}%</td>
        <td>${s.internalMarks}%</td>
        <td><span class="${s.backlogs > 0 ? 'text-critical' : ''}">${s.backlogs}</span></td>
        <td>${s.activitiesCount} Activities</td>
        <td>${riskBadge}</td>
        <td><button class="btn btn-secondary btn-sm" onclick="showStudentProfile('${s.usn}')">Inspect Profile</button></td>
      </tr>
    `;
  }).join('');

  renderStudentTrendChart();
}

function filterStudents(level) {
  appState.studentRiskFilter = level;
  document.querySelectorAll('#student-risk-filters .pill-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  renderC4View();
}

function showStudentProfile(usn) {
  const s = appState.students.find(x => x.usn === usn);
  if (!s) return;
  Utils.showToast(`Profile: ${s.name} | CGPA: ${s.cgpa} | Attendance: ${s.attendance}% | Risk: ${s.riskLevel}`, 'info');
}

function renderStudentTrendChart() {
  const chartBox = document.getElementById('student-trend-chart');
  if (!chartBox) return;

  chartBox.innerHTML = `
    <svg viewBox="0 0 400 160" style="width: 100%; height: 160px;">
      <!-- Grid Lines -->
      <line x1="40" y1="20" x2="380" y2="20" stroke="var(--border-color)" stroke-dasharray="3"/>
      <line x1="40" y1="70" x2="380" y2="70" stroke="var(--border-color)" stroke-dasharray="3"/>
      <line x1="40" y1="120" x2="380" y2="120" stroke="var(--border-color)"/>

      <!-- Y Axis Labels -->
      <text x="10" y="25" fill="var(--text-dim)" font-size="10">100%</text>
      <text x="15" y="75" fill="var(--text-dim)" font-size="10">90%</text>
      <text x="15" y="125" fill="var(--text-dim)" font-size="10">80%</text>

      <!-- Trend Line (Pass Rate) -->
      <path d="M 60 110 L 140 90 L 220 70 L 300 45 L 360 30" fill="none" stroke="var(--cyan)" stroke-width="3"/>
      <circle cx="60" cy="110" r="4" fill="var(--cyan)"/>
      <circle cx="140" cy="90" r="4" fill="var(--cyan)"/>
      <circle cx="220" cy="70" r="4" fill="var(--cyan)"/>
      <circle cx="300" cy="45" r="4" fill="var(--cyan)"/>
      <circle cx="360" cy="30" r="5" fill="var(--cyan)" stroke="#fff" stroke-width="2"/>

      <!-- X Axis Labels -->
      <text x="50" y="145" fill="var(--text-dim)" font-size="10">AY 22-23</text>
      <text x="130" y="145" fill="var(--text-dim)" font-size="10">AY 23-24</text>
      <text x="210" y="145" fill="var(--text-dim)" font-size="10">AY 24-25</text>
      <text x="290" y="145" fill="var(--text-dim)" font-size="10">AY 25-26</text>
      <text x="350" y="145" fill="var(--cyan)" font-size="10" font-weight="700">Target</text>
    </svg>
  `;
}

// C5 FACULTY VIEW RENDERING
function renderC5View() {
  const tbody = document.getElementById('faculty-directory-tbody');
  if (!tbody) return;

  tbody.innerHTML = appState.faculty.map(f => `
    <tr>
      <td><strong>${f.name}</strong></td>
      <td>${f.designation}</td>
      <td><span class="badge-pill">${f.qualification}</span></td>
      <td>${f.experience} Years</td>
      <td>${f.workload} hrs/wk</td>
      <td>
        <div style="display: flex; align-items: center; gap: 8px;">
          <strong style="font-family: var(--font-mono);">${f.completeness}%</strong>
          <div style="flex: 1; height: 6px; background: var(--bg-panel); border-radius: 3px; overflow: hidden;">
            <div style="height: 100%; width: ${f.completeness}%; background: ${f.completeness === 100 ? 'var(--emerald)' : 'var(--amber)'};"></div>
          </div>
        </div>
      </td>
      <td><span class="badge-status ${f.status === 'VERIFIED' ? 'status-pass' : 'status-warning'}">${f.status}</span></td>
      <td><button class="btn btn-secondary btn-sm" onclick="alert('Faculty Profile Document Verification:\n✓ PhD Certificate\n✓ Experience Record\n✓ Appointment Order')">View Docs</button></td>
    </tr>
  `).join('');

  renderFacultyWorkloadChart();
}

function renderFacultyWorkloadChart() {
  const box = document.getElementById('faculty-workload-chart');
  if (!box) return;

  box.innerHTML = appState.faculty.map(f => `
    <div style="margin-bottom: 12px;">
      <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 4px;">
        <span>${f.name} (${f.designation})</span>
        <strong>${f.workload} hrs / week</strong>
      </div>
      <div style="height: 8px; background: var(--bg-panel); border-radius: 4px; overflow: hidden;">
        <div style="height: 100%; width: ${(f.workload / 24) * 100}%; background: var(--emerald);"></div>
      </div>
    </div>
  `).join('');
}

// C6 CONTRIBUTIONS RENDERING & EVIDENCE CHAIN
function renderC6View() {
  const tbody = document.getElementById('c6-contributions-tbody');
  if (!tbody) return;

  const filtered = appState.contributions.filter(c => {
    if (appState.c6TypeFilter === 'ALL') return true;
    return c.type === appState.c6TypeFilter;
  });

  tbody.innerHTML = filtered.map(c => `
    <tr>
      <td><strong>${c.title}</strong></td>
      <td><span class="badge-pill">${c.type}</span></td>
      <td>${c.facultyName}</td>
      <td>${c.publisher}</td>
      <td>${c.date}</td>
      <td><span class="badge-status status-pass">${c.status} ✓</span></td>
      <td><button class="btn btn-secondary btn-sm" onclick="inspectEvidenceChain('${c.id}')">Inspect Proof Chain</button></td>
    </tr>
  `).join('');

  renderEvidenceVerificationChain();
}

function filterC6Contributions(type) {
  appState.c6TypeFilter = type;
  document.querySelectorAll('#c6-type-filters .pill-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  renderC6View();
}

function renderEvidenceVerificationChain() {
  const chainBox = document.getElementById('evidence-verification-chain');
  if (!chainBox) return;

  chainBox.innerHTML = `
    <div class="chain-node">
      <span class="node-title">1. CLAIM</span>
      <span class="node-val">"Dr. XYZ published IEEE Paper"</span>
    </div>
    <span class="chain-arrow">➔</span>
    <div class="chain-node">
      <span class="node-title">2. RECORD</span>
      <span class="node-val">Publication Entry #C6-01</span>
    </div>
    <span class="chain-arrow">➔</span>
    <div class="chain-node">
      <span class="node-title">3. EVIDENCE</span>
      <span class="node-val">IEEE_Paper_XYZ_2025.pdf</span>
    </div>
    <span class="chain-arrow">➔</span>
    <div class="chain-node">
      <span class="node-title">4. AI VERIFICATION</span>
      <span class="node-val">Author Match ✓ | DOI Valid ✓</span>
    </div>
    <span class="chain-arrow">➔</span>
    <div class="chain-node active">
      <span class="node-title">5. STATUS</span>
      <span class="node-val text-pass">VERIFIED COMPLIANT</span>
    </div>
  `;
}

function inspectEvidenceChain(id) {
  const item = appState.contributions.find(c => c.id === id);
  if (!item) return;
  Utils.showToast(`Evidence Chain VERIFIED ✓ — ${item.title} by ${item.facultyName} | ${item.status}`, 'success');
}

// EVIDENCE CENTER VIEW
function renderEvidenceView() {
  const tbody = document.getElementById('evidence-vault-tbody');
  if (!tbody) return;

  const docs = [
    { name: "Midterm_Q1_Proof.pdf", criterion: "C3", req: "CO1 Question Mapping", faculty: "Dr. K. S. Sharma", date: "2025-05-10", type: "Question Paper", status: "VERIFIED" },
    { name: "IEEE_Paper_XYZ_2025.pdf", criterion: "C6", req: "Faculty Research Publication", faculty: "Dr. XYZ", date: "2025-04-12", type: "Journal PDF", status: "VERIFIED" },
    { name: "Patent_Grant_ABC_2025.pdf", criterion: "C6", req: "Patent Grant Certificate", faculty: "Dr. ABC", date: "2025-02-18", type: "Patent Doc", status: "VERIFIED" },
    { name: "FDP_Cert_XYZ_IITB.pdf", criterion: "C6", req: "FDP Participation Proof", faculty: "Dr. XYZ", date: "2025-06-10", type: "FDP Cert", status: "VERIFIED" },
    { name: "Appointment_Order_PQR.pdf", criterion: "C5", req: "Faculty Cadre Proof", faculty: "Prof. PQR", date: "2025-01-05", type: "Appointment Order", status: "NEEDS_REVIEW" },
    { name: "Remedial_Attendance_CO2.pdf", criterion: "C3", req: "Continuous Improvement", faculty: "Dr. XYZ", date: "2025-08-20", type: "Attendance Log", status: "VERIFIED" }
  ];

  const filtered = docs.filter(d => {
    if (appState.evidenceStatusFilter === 'ALL') return true;
    return d.status === appState.evidenceStatusFilter;
  });

  tbody.innerHTML = filtered.map(d => `
    <tr>
      <td><a href="#" style="color: var(--indigo); font-weight: 600;" onclick="alert('Viewing document: ${d.name}')">📄 ${d.name}</a></td>
      <td><span class="badge-pill">${d.criterion}</span></td>
      <td>${d.req}</td>
      <td>${d.faculty}</td>
      <td>${d.date}</td>
      <td><span class="badge-tag">${d.type}</span></td>
      <td><span class="badge-status ${d.status === 'VERIFIED' ? 'status-pass' : 'status-warning'}">${d.status} ✓</span></td>
      <td><button class="btn btn-secondary btn-sm" onclick="alert('Verified metadata extracted via AI OCR:\nDocument Confidence: 99.4%\nPublisher Checked: Yes')">AI Metadata</button></td>
    </tr>
  `).join('');

  document.getElementById('evidence-count-badge').innerText = docs.length;
}

function filterEvidence(status) {
  appState.evidenceStatusFilter = status;
  document.querySelectorAll('#evidence-status-filters .pill-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  renderEvidenceView();
}

// ACTION CENTER VIEW RENDERING
function renderActionCenterView() {
  const container = document.getElementById('action-items-list');
  if (!container) return;

  container.innerHTML = appState.actionItems.map(item => `
    <div class="action-card ${item.priority.toLowerCase()}">
      <div style="display: flex; flex-direction: column; gap: 8px; flex: 1;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span class="card-badge c3">${item.criterion}</span>
          <strong style="font-size: 15px;">${item.title}</strong>
          <span class="badge-chip ${item.priority === 'CRITICAL' ? 'red' : 'amber'}">${item.priority}</span>
        </div>
        <p style="font-size: 13px; color: var(--text-muted);">${item.problem}</p>
        <div style="background: var(--bg-card); padding: 10px 14px; border-radius: 6px; font-size: 12px;">
          <strong>AI Recommended Action:</strong> ${item.recommendedAction}<br>
          <span style="color: var(--indigo);">Required Evidence: ${item.requiredEvidence}</span>
        </div>
        <div style="font-size: 11px; color: var(--text-dim);">
          Owner: <strong>${item.ownerName}</strong> • Deadline: <strong>${item.deadline}</strong>
        </div>
      </div>
      <div style="display: flex; flex-direction: column; align-items: flex-end; justify-content: space-between; margin-left: 20px;">
        <span class="badge-status ${item.status === 'COMPLETED' ? 'status-pass' : 'status-warning'}">${item.status}</span>
        ${item.status !== 'COMPLETED' ? `<button class="btn btn-primary btn-sm" onclick="resolveActionItem('${item.id}')">Upload Evidence & Complete</button>` : `<span style="font-weight: 700; color: var(--emerald);">GAP CLOSED ✓</span>`}
      </div>
    </div>
  `).join('');

  document.getElementById('action-count-badge').innerText = appState.actionItems.filter(a => a.status !== 'COMPLETED').length;
}

// AI RAG ASSISTANT CHAT ENGINE
function sendPrompt(text) {
  document.getElementById('chat-input-field').value = text;
  sendChatMessage();
}

function sendChatMessage() {
  const input = document.getElementById('chat-input-field');
  const text = input.value.trim();
  if (!text) return;

  const messagesContainer = document.getElementById('chat-messages-container');

  // Append user message
  messagesContainer.innerHTML += `
    <div class="message user-msg">
      <div class="msg-avatar">YOU</div>
      <div class="msg-content">${text}</div>
    </div>
  `;
  input.value = '';
  messagesContainer.scrollTop = messagesContainer.scrollHeight;

  // Simulate RAG answer delay
  setTimeout(() => {
    let reply = "I analyzed the CSE Department Digital Twin database for your query.";
    let sources = "Sources: IEEE_Paper_XYZ_2025.pdf, Midterm_CO_Attainment_Sheet.xlsx";

    if (text.toLowerCase().includes("c6") || text.toLowerCase().includes("evidence")) {
      reply = "<strong>C6 Faculty Contribution Evidence is 94.0% Complete.</strong><br>• 47 total publications recorded, 42 with verified PDF proof.<br>• 12 patents filed, 3 granted.<br>• 8 recent uploads pending final accreditation verification.";
      sources = "Sources: IEEE_Paper_XYZ_2025.pdf, Patent_Grant_ABC_2025.pdf, DST_Funding_Grant.pdf";
    } else if (text.toLowerCase().includes("faculty") || text.toLowerCase().includes("incomplete")) {
      reply = "<strong>Faculty Information Audit (Criterion 5):</strong><br>• 3 faculty profiles have missing document records.<br>• Prof. PQR is missing appointment order copy (Completeness 71%).<br>• Dr. XYZ requires updated experience certificate (Completeness 92%).";
      sources = "Sources: Faculty_Cadre_Master_2025.xlsx, Appointment_Order_PQR.pdf";
    } else if (text.toLowerCase().includes("co") || text.toLowerCase().includes("target")) {
      reply = "<strong>CO Attainment Gap Analysis (Criterion 3):</strong><br>• CO2 (Apply Machine Learning Algorithms) is currently at <strong>61.0%</strong> (Target threshold 70.0%).<br>• Main contributor: Low performance in midterm exam SVM & decision tree numerical questions.<br>• Action Item ACT-101 is active with Dr. XYZ assigned for remedial classes.";
      sources = "Sources: Midterm_Marks_21CS61.xlsx, Remedial_Attendance_CO2.pdf";
    } else if (text.toLowerCase().includes("student") || text.toLowerCase().includes("support")) {
      reply = "<strong>Student Support Risk Radar (Criterion 4):</strong><br>• 8 students flagged in <strong>High Attention 🔴</strong> zone due to low attendance (<65%) and internal marks.<br>• 17 students require monitoring 🟡.<br>• Overall Department Pass Rate is strong at 92.4%.";
      sources = "Sources: Student_Attendance_S6.csv, University_Results_2025.xlsx";
    }

    messagesContainer.innerHTML += `
      <div class="message assistant-msg">
        <div class="msg-avatar">AI</div>
        <div class="msg-content">
          <div class="msg-text">${reply}</div>
          <div style="margin-top: 8px; padding-top: 6px; border-top: 1px solid var(--border-color); font-size: 11px; color: var(--indigo);">
            📁 <em>${sources}</em>
          </div>
        </div>
      </div>
    `;
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }, 600);
}

// VIRTUAL NBA INSPECTION SIMULATOR (THE WOW FEATURE)
function openInspectionModal() {
  document.getElementById('inspection-modal').classList.remove('hidden');
  document.getElementById('inspection-scanning-state').classList.remove('hidden');
  document.getElementById('inspection-results-state').classList.add('hidden');

  // Step 1 scanning simulation
  setTimeout(() => {
    document.getElementById('scan-step-c3').querySelector('.step-status').innerText = 'PASS ✓ (82%)';
    document.getElementById('scan-step-c3').querySelector('.step-status').classList.remove('status-spin');
    document.getElementById('scan-step-c3').querySelector('.step-status').classList.add('text-pass');
    
    document.getElementById('scan-step-c4').querySelector('.step-status').innerText = 'PASS ✓ (91%)';
    document.getElementById('scan-step-c4').querySelector('.step-status').classList.add('text-pass');
  }, 1000);

  setTimeout(() => {
    document.getElementById('scan-step-c5').querySelector('.step-status').innerText = 'PASS ✓ (94%)';
    document.getElementById('scan-step-c5').querySelector('.step-status').classList.add('text-pass');
    
    document.getElementById('scan-step-c6').querySelector('.step-status').innerText = 'WARNING ⚠ (78%)';
    document.getElementById('scan-step-c6').querySelector('.step-status').classList.add('text-amber');
  }, 2000);

  // Show final results state
  setTimeout(() => {
    document.getElementById('inspection-scanning-state').classList.add('hidden');
    document.getElementById('inspection-results-state').classList.remove('hidden');

    document.getElementById('inspection-priority-list').innerHTML = `
      <div class="gap-item critical" style="margin-bottom: 8px;">
        <div><strong>1. 🔴 CO2 Attainment Below Target (61% vs 70%)</strong><br><span style="font-size: 11px; color: var(--text-dim);">Criterion 3 • Action assigned to Dr. XYZ</span></div>
        <button class="btn btn-secondary btn-sm" onclick="closeInspectionModal(); switchTab('action-center');">Fix Gap</button>
      </div>
      <div class="gap-item warning" style="margin-bottom: 8px;">
        <div><strong>2. 🟡 3 Incomplete Faculty Qualification Records</strong><br><span style="font-size: 11px; color: var(--text-dim);">Criterion 5 • Missing appointment order for Prof. PQR</span></div>
        <button class="btn btn-secondary btn-sm" onclick="closeInspectionModal(); switchTab('c5-faculty');">Fix Profile</button>
      </div>
      <div class="gap-item warning">
        <div><strong>3. 🟡 8 Research Papers Pending Evidence Verification</strong><br><span style="font-size: 11px; color: var(--text-dim);">Criterion 6 • Upload Scopus DOI verification pdfs</span></div>
        <button class="btn btn-secondary btn-sm" onclick="closeInspectionModal(); switchTab('c6-contributions');">Verify Docs</button>
      </div>
    `;
  }, 2800);
}

function closeInspectionModal() {
  document.getElementById('inspection-modal').classList.add('hidden');
}

// UPLOAD MODAL & SIMULATED AI OCR
function openGlobalUploadModal() {
  document.getElementById('upload-modal').classList.remove('hidden');
}

function closeUploadModal() {
  document.getElementById('upload-modal').classList.add('hidden');
}

function simulateFileSelection(input) {
  const fileName = input.files[0] ? input.files[0].name : 'Selected_Document.pdf';
  const previewBox = document.getElementById('upload-ai-preview');
  const detailsBox = document.getElementById('ai-extracted-details-content');
  const meta = FileUploadComponent.simulateAIExtraction(fileName);

  previewBox.classList.remove('hidden');
  detailsBox.innerHTML = FileUploadComponent.renderAIPreview(meta);
}

function handleUploadSubmit(e) {
  e.preventDefault();
  closeUploadModal();
  appState.activityLogs.unshift({ text: 'AI parsed & verified new evidence document', time: 'Just now', type: 'upload' });
  renderActivityTimeline();
  Utils.showToast('Document uploaded & AI-verified successfully! Linked to Evidence Center.', 'success');
}

// SEARCH ENGINE
function setupGlobalSearch() {
  const input = document.getElementById('global-search-input');
  const dropdown = document.getElementById('search-results-dropdown');
  if (!input || !dropdown) return;

  input.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    if (!query) {
      dropdown.classList.add('hidden');
      return;
    }

    const items = [
      { text: "CO2 Attainment Gap (61.0% 🔴)", tab: "c3-assessment" },
      { text: "Dr. XYZ (Assoc. Professor, 18 hrs workload)", tab: "c5-faculty" },
      { text: "Student Anagha D K (USN 1BM23CS001)", tab: "c4-students" },
      { text: "IEEE Medical Image Segmentation Paper", tab: "c6-contributions" },
      { text: "Missing Faculty Documents (Prof. PQR)", tab: "c5-faculty" }
    ].filter(i => i.text.toLowerCase().includes(query));

    if (items.length > 0) {
      dropdown.innerHTML = items.map(i => `
        <div class="search-result-item" onclick="switchTab('${i.tab}'); document.getElementById('search-results-dropdown').classList.add('hidden');">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          <span>${i.text}</span>
        </div>
      `).join('');
      dropdown.classList.remove('hidden');
    } else {
      dropdown.innerHTML = `<div class="search-result-item"><span>No matching compliance data found</span></div>`;
      dropdown.classList.remove('hidden');
    }
  });
}

function downloadArchitecturePDF() {
  const link = document.createElement('a');
  link.href = 'ACCREDIX_System_Architecture_Doc.pdf';
  link.download = 'ACCREDIX_System_Architecture_Doc.pdf';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  Utils.showToast('Downloading ACCREDIX System Architecture & Technical Guide PDF...', 'success');
}

function downloadDiagramPDF() {
  const link = document.createElement('a');
  link.href = 'ACCREDIX_System_High_Level_Architecture_Diagram.pdf';
  link.download = 'ACCREDIX_System_High_Level_Architecture_Diagram.pdf';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  Utils.showToast('Downloading ACCREDIX High-Level System Architecture Diagram PDF...', 'success');
}

function simulateReportDownload(filename) {
  const link = document.createElement('a');
  link.href = 'ACCREDIX_System_Architecture_Doc.pdf';
  link.download = filename || 'ACCREDIX_NBA_SAR_Report.pdf';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  Utils.showToast(`Downloading: ${filename} — PDF export ready!`, 'success');
}

function toggleNotifDrawer() {
  const drawer = document.getElementById('notif-drawer');
  const notifList = document.getElementById('notif-list-body');
  drawer.classList.toggle('hidden');

  notifList.innerHTML = `
    <div class="notif-card" style="border-left: 3px solid var(--crimson);">
      <strong style="color: var(--crimson);">Critical Gap Alert</strong><br>CO2 attainment is below 70% threshold.
    </div>
    <div class="notif-card" style="border-left: 3px solid var(--amber);">
      <strong style="color: var(--amber);">Action Due Soon</strong><br>Prof. PQR qualification document upload due tomorrow.
    </div>
    <div class="notif-card" style="border-left: 3px solid var(--emerald);">
      <strong style="color: var(--emerald);">Evidence Verified</strong><br>IEEE_Paper_XYZ_2025.pdf verified by Evidence Engine.
    </div>
  `;
}

function openC3UploadModal() { openGlobalUploadModal(); }
function openC4DataUploadModal() { openGlobalUploadModal(); }
function openContributionModal() { openGlobalUploadModal(); }
