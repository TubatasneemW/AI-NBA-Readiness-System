/**
 * ============================================================================
 * NBA DIGITAL TWIN - APPLICATION JAVASCRIPT
 * AI & ML Department | Continuous Accreditation Readiness System
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initCopoChart();
  initFacultyData();
  initStudentData();
  initAttainmentTable();
  initDocumentsData();
  initAiAssistant();
  initFilterControls();
  initModals();

  window.addEventListener('resize', () => {
    initCopoChart();
  });
});

/* ============================================================================
   1. NAVIGATION & MODULE SWITCHER
   ============================================================================ */
const moduleTitles = {
  'dashboard': { title: 'Dashboard', subtitle: 'AI & ML Department Digital Twin – NBA Accreditation' },
  'programme-info': { title: 'Programme Information', subtitle: 'Criterion 1: Vision, Mission, PEOs, PSOs & Objectives' },
  'faculty-twin': { title: 'Faculty Twin', subtitle: 'Criterion 5 & 6: Qualifications, Cadre Ratio, SFR & Contributions' },
  'student-twin': { title: 'Student Twin', subtitle: 'Criterion 4: Academic Performance, At-Risk Diagnostic & Success Rate' },
  'course-curriculum': { title: 'Course & Curriculum', subtitle: 'Criterion 1 & 2: Course Files, Lesson Plans & Syllabus Schemes' },
  'copo-mapping': { title: 'CO-PO-PSO Mapping Matrix', subtitle: 'Criterion 3: Outcome Correlation Matrix & Bloom Taxonomy' },
  'attainment-analysis': { title: 'Attainment Analysis', subtitle: 'Criterion 3: Direct, Indirect & Program Outcome Attainment' },
  'research-publications': { title: 'Research & Publications', subtitle: 'Criterion 6: SCI/Scopus Papers, Patents, Grants & Consultancy' },
  'infrastructure-twin': { title: 'Infrastructure Twin', subtitle: 'Criterion 7: Laboratories, GPU Systems, Calibration & Safety' },
  'placements': { title: 'Placements & Internships', subtitle: 'Criterion 4: Placement Records, Higher Studies & Industry MoUs' },
  'nba-criteria': { title: 'NBA Criteria & Compliance', subtitle: 'Master Accreditation Rulebook & Evaluation Engine (C1 to C9)' },
  'document-repository': { title: 'Document Repository', subtitle: 'Contextual Evidence Engine & Document AI Extraction' },
  'reports': { title: 'Accreditation Reports', subtitle: 'Automated Tier-I SAR Generation & Continuous Improvement Dossiers' },
  'gap-analysis': { title: 'Gap Analysis & Continuous Improvement', subtitle: 'Criterion 8: Closed Loop Problem-to-Action Tracking' },
  'ai-assistant': { title: 'AI Accreditation Assistant', subtitle: 'RAG Knowledge Engine & Autonomous Accreditation Agents' }
};

function initNavigation() {
  const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
  const sidebar = document.getElementById('sidebar');
  const menuToggleBtn = document.getElementById('menuToggleBtn');

  // Sidebar link clicks
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const moduleKey = item.getAttribute('data-module');
      switchModule(moduleKey);

      if (window.innerWidth <= 768 && sidebar) {
        sidebar.classList.remove('mobile-open');
      }
    });
  });

  // Action links inside cards ("View Details", "View All", etc.)
  document.querySelectorAll('[data-switch-to]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetModule = link.getAttribute('data-switch-to');
      switchModule(targetModule);
    });
  });

  // Hamburger toggle button
  if (menuToggleBtn && sidebar) {
    menuToggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('mobile-open');
    });
  }
}

function switchModule(moduleKey) {
  // Update sidebar active status
  document.querySelectorAll('.sidebar-nav .nav-item').forEach(item => {
    if (item.getAttribute('data-module') === moduleKey) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  // Update headers
  if (moduleTitles[moduleKey]) {
    document.getElementById('pageTitle').textContent = moduleTitles[moduleKey].title;
    document.getElementById('pageSubtitle').textContent = moduleTitles[moduleKey].subtitle;
  }

  // Switch visible view
  document.querySelectorAll('.module-view').forEach(view => {
    view.classList.remove('active');
  });

  const targetView = document.getElementById(`view-${moduleKey}`);
  if (targetView) {
    targetView.classList.add('active');
    if (moduleKey === 'dashboard') {
      setTimeout(initCopoChart, 50);
    }
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

/* ============================================================================
   2. CO - PO ATTAINMENT CHART (Pixel-Perfect Alignment)
   ============================================================================ */
const copoData = [
  { po: 'PO1', target: 82, attainment: 82, desc: 'Engineering Knowledge: Apply mathematics, science & AI engineering fundamentals.' },
  { po: 'PO2', target: 82, attainment: 70, desc: 'Problem Analysis: Identify, formulate and solve complex ML problems.' },
  { po: 'PO3', target: 82, attainment: 58, desc: 'Design/Development: Design intelligent systems meeting user constraints.' },
  { po: 'PO4', target: 82, attainment: 65, desc: 'Conduct Investigations: Use research-based methods and statistical data analysis.' },
  { po: 'PO5', target: 82, attainment: 64, desc: 'Modern Tool Usage: Select and apply modern GPU frameworks (PyTorch, TensorFlow).' },
  { po: 'PO6', target: 82, attainment: 72, desc: 'Engineer and Society: Apply reasoning informed by contextual societal knowledge.' },
  { po: 'PO7', target: 82, attainment: 50, desc: 'Environment and Sustainability: Understand sustainable AI compute implications.' },
  { po: 'PO8', target: 82, attainment: 68, desc: 'Ethics: Commit to professional ethics, algorithmic fairness & data privacy.' },
  { po: 'PO9', target: 82, attainment: 64, desc: 'Individual and Team Work: Function effectively in multidisciplinary teams.' },
  { po: 'PO10', target: 82, attainment: 66, desc: 'Communication: Communicate effectively on complex AI activities.' },
  { po: 'PO11', target: 82, attainment: 74, desc: 'Project Management: Apply engineering and software management principles.' },
  { po: 'PO12', target: 82, attainment: 64, desc: 'Life-long Learning: Recognize the need for independent and life-long learning.' }
];

function initCopoChart() {
  const container = document.getElementById('copoChartContainer');
  if (!container) return;

  const width = 560;
  const height = 195;
  const padding = { top: 12, right: 14, bottom: 34, left: 30 };

  const chartW = width - padding.left - padding.right;
  const chartH = height - padding.top - padding.bottom;

  const yTicks = [0, 20, 40, 60, 80, 100];
  const barGroupWidth = chartW / copoData.length;
  const singleBarW = 6.5;
  const barGap = 2.5;

  // Build grid lines and labels
  let gridSvg = '';
  yTicks.forEach(tick => {
    const yPos = padding.top + chartH - (tick / 100) * chartH;
    gridSvg += `
      <line x1="${padding.left}" y1="${yPos}" x2="${width - padding.right}" y2="${yPos}" class="chart-grid-line" />
      <text x="${padding.left - 6}" y="${yPos + 3}" text-anchor="end" class="chart-axis-text">${tick}</text>
    `;
  });

  // Build bars
  let barsSvg = '';
  copoData.forEach((item, index) => {
    const groupX = padding.left + index * barGroupWidth + (barGroupWidth - (singleBarW * 2 + barGap)) / 2;
    
    // Target Bar (Blue)
    const targetH = (item.target / 100) * chartH;
    const targetY = padding.top + chartH - targetH;
    
    // Attainment Bar (Green)
    const attainH = (item.attainment / 100) * chartH;
    const attainY = padding.top + chartH - attainH;

    barsSvg += `
      <g class="chart-bar-group" data-index="${index}" style="cursor: pointer;">
        <!-- Target Bar -->
        <rect x="${groupX}" y="${targetY}" width="${singleBarW}" height="${targetH}" class="bar-target" />
        <!-- Attainment Bar -->
        <rect x="${groupX + singleBarW + barGap}" y="${attainY}" width="${singleBarW}" height="${attainH}" class="bar-attainment" />
        <!-- X Label -->
        <text x="${groupX + singleBarW + barGap / 2}" y="${height - 18}" text-anchor="middle" class="chart-axis-text" style="font-weight: 600; fill: #475569;">${item.po}</text>
      </g>
    `;
  });

  const svgContent = `
    <svg viewBox="0 0 ${width} ${height}" class="chart-svg" preserveAspectRatio="xMidYMid meet">
      <!-- Y-Axis Label -->
      <text x="-${height / 2 - 4}" y="10" transform="rotate(-90)" class="chart-axis-label">Percentage (%)</text>
      
      <!-- Grid Lines -->
      ${gridSvg}

      <!-- Bottom X-Axis Line -->
      <line x1="${padding.left}" y1="${padding.top + chartH}" x2="${width - padding.right}" y2="${padding.top + chartH}" stroke="#cbd5e1" stroke-width="1" />

      <!-- Bars -->
      ${barsSvg}

      <!-- X-Axis Title -->
      <text x="${width / 2}" y="${height - 2}" class="chart-axis-label">Program Outcomes</text>
    </svg>
  `;

  container.innerHTML = svgContent;
  setupChartTooltips();
}

function setupChartTooltips() {
  const tooltip = document.getElementById('chartTooltip');
  const barGroups = document.querySelectorAll('.chart-bar-group');

  barGroups.forEach(group => {
    group.addEventListener('mouseenter', () => {
      const idx = group.getAttribute('data-index');
      const item = copoData[idx];
      const gap = item.target - item.attainment;
      const statusText = gap <= 0 ? '🟢 Met Target' : `⚠️ Gap: ${gap}% Below Target`;

      tooltip.innerHTML = `
        <div style="font-weight: 700; color: #60a5fa; margin-bottom: 2px;">${item.po} - Attainment Overview</div>
        <div style="font-size: 9.5px; color: #cbd5e1; margin-bottom: 4px; max-width: 200px;">${item.desc}</div>
        <div>Target: <strong>${item.target}%</strong> &nbsp;|&nbsp; Attained: <strong>${item.attainment}%</strong></div>
        <div style="margin-top: 3px; font-weight: 600;">${statusText}</div>
      `;
      tooltip.style.opacity = '1';
    });

    group.addEventListener('mousemove', (e) => {
      tooltip.style.left = (e.pageX + 10) + 'px';
      tooltip.style.top = (e.pageY - 55) + 'px';
    });

    group.addEventListener('mouseleave', () => {
      tooltip.style.opacity = '0';
    });
  });
}

/* ============================================================================
   3. FACULTY DATA
   ============================================================================ */
const facultyList = [
  { name: 'Dr. Bharati Reshmi', desig: 'Professor & HOD', qual: 'Ph.D.', load: 14, pubs: 12, fdp: 4, status: 'Verified' },
  { name: 'Dr. Anand Rao', desig: 'Associate Professor', qual: 'Ph.D.', load: 16, pubs: 8, fdp: 3, status: 'Needs Review' },
  { name: 'Prof. Sneha Deshmukh', desig: 'Assistant Professor', qual: 'M.Tech (Ph.D. Reg)', load: 18, pubs: 4, fdp: 3, status: 'Verified' },
  { name: 'Prof. Rajesh Kumar', desig: 'Assistant Professor', qual: 'M.Tech', load: 18, pubs: 3, fdp: 2, status: 'Verified' },
  { name: 'Dr. Sunita Patil', desig: 'Associate Professor', qual: 'Ph.D.', load: 16, pubs: 6, fdp: 4, status: 'Verified' },
  { name: 'Prof. Vikram Malhotra', desig: 'Assistant Professor', qual: 'M.Tech', load: 18, pubs: 2, fdp: 1, status: 'Missing' },
  { name: 'Dr. P. K. Sharma', desig: 'Professor', qual: 'Ph.D.', load: 12, pubs: 9, fdp: 5, status: 'Verified' },
  { name: 'Prof. Megha Kulkarni', desig: 'Assistant Professor', qual: 'M.Tech', load: 18, pubs: 3, fdp: 2, status: 'Verified' }
];

function initFacultyData() {
  const tbody = document.getElementById('facultyTableBody');
  if (!tbody) return;

  tbody.innerHTML = facultyList.map(f => {
    let statusBadge = '<span class="status-pill success">Verified ✅</span>';
    if (f.status === 'Needs Review') statusBadge = '<span class="status-pill warning">Needs Review ⚠️</span>';
    if (f.status === 'Missing') statusBadge = '<span class="status-pill danger">Missing Doc ❌</span>';

    return `
      <tr>
        <td><strong>${f.name}</strong></td>
        <td>${f.desig}</td>
        <td>${f.qual}</td>
        <td>${f.load} hrs</td>
        <td>${f.pubs}</td>
        <td>${f.fdp}</td>
        <td>${statusBadge}</td>
        <td><button class="btn-secondary" style="padding: 2px 6px; font-size: 10px;" onclick="alert('Viewing digital dossier for ${f.name}')">Dossier</button></td>
      </tr>
    `;
  }).join('');
}

function filterFacultyTable() {
  const query = document.getElementById('facultySearchInput').value.toLowerCase();
  const rows = document.querySelectorAll('#facultyTableBody tr');
  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  });
}

/* ============================================================================
   4. STUDENT DATA
   ============================================================================ */
const studentList = [
  { usn: '1RV22AI001', name: 'Aarav Sharma', sem: '6th Sem', cgpa: 8.92, att: 94, backlogs: 0, intern: 'Placed (Microsoft)', status: 'Excellent' },
  { usn: '1RV22AI014', name: 'Ananya Deshpande', sem: '6th Sem', cgpa: 8.45, att: 91, backlogs: 0, intern: 'Adobe Labs', status: 'Good' },
  { usn: '1RV22AI028', name: 'Chetan Verma', sem: '6th Sem', cgpa: 6.20, att: 72, backlogs: 2, intern: 'Pending', status: 'At-Risk ⚠️' },
  { usn: '1RV22AI042', name: 'Divya Nair', sem: '6th Sem', cgpa: 9.15, att: 96, backlogs: 0, intern: 'Amazon AWS', status: 'Excellent' },
  { usn: '1RV22AI059', name: 'Farhan Akhtar', sem: '6th Sem', cgpa: 7.40, att: 85, backlogs: 0, intern: 'Infosys InStep', status: 'Good' },
  { usn: '1RV22AI077', name: 'Gautam Iyer', sem: '6th Sem', cgpa: 5.80, att: 68, backlogs: 3, intern: 'Not Eligible', status: 'Critical 🔴' }
];

function initStudentData() {
  const tbody = document.getElementById('studentTableBody');
  if (!tbody) return;

  tbody.innerHTML = studentList.map(s => {
    let statusClass = 'success';
    if (s.status.includes('At-Risk')) statusClass = 'warning';
    if (s.status.includes('Critical')) statusClass = 'danger';

    return `
      <tr>
        <td><strong>${s.usn}</strong></td>
        <td>${s.name}</td>
        <td>${s.sem}</td>
        <td>${s.cgpa.toFixed(2)}</td>
        <td>${s.att}%</td>
        <td>${s.backlogs}</td>
        <td>${s.intern}</td>
        <td><span class="status-pill ${statusClass}">${s.status}</span></td>
      </tr>
    `;
  }).join('');
}

function filterStudentTable() {
  const query = document.getElementById('studentSearchInput').value.toLowerCase();
  const rows = document.querySelectorAll('#studentTableBody tr');
  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  });
}

/* ============================================================================
   5. ATTAINMENT SUMMARY
   ============================================================================ */
function initAttainmentTable() {
  const tbody = document.getElementById('attainmentTableBody');
  if (!tbody) return;

  tbody.innerHTML = copoData.map(item => {
    const direct = (item.attainment * 0.95).toFixed(1);
    const indirect = (item.attainment * 1.08 > 100 ? 98 : item.attainment * 1.08).toFixed(1);
    const gap = item.target - item.attainment;
    const isGap = gap > 0;

    return `
      <tr>
        <td><strong>${item.po}</strong></td>
        <td>${item.target}%</td>
        <td>${direct}%</td>
        <td>${indirect}%</td>
        <td><strong>${item.attainment}%</strong></td>
        <td><span style="color: ${isGap ? '#dc2626' : '#16a34a'}; font-weight: 700;">${isGap ? `-${gap}%` : 'Target Met'}</span></td>
        <td>${isGap ? '<span class="status-pill warning">Remedial Class ATR</span>' : '<span class="status-pill success">Compliant</span>'}</td>
      </tr>
    `;
  }).join('');
}

/* ============================================================================
   6. EVIDENCE DOCUMENT REPOSITORY
   ============================================================================ */
let documentsList = [
  { name: '22AI61_Course_File_Final.pdf', crit: 'Criterion 2 & 3', context: 'Machine Learning / Dr. Anand Rao', by: 'Dr. Anand Rao', date: '2026-10-15', aiType: 'Course File & Lesson Plan', status: 'Needs Review ⚠️' },
  { name: '22AI62_Deep_Learning_Syllabus_Approval.pdf', crit: 'Criterion 1', context: 'Curriculum / Dr. Bharati Reshmi', by: 'Dr. Bharati Reshmi', date: '2026-09-20', aiType: 'DAB Minutes & Syllabus', status: 'Verified ✅' },
  { name: 'FDP_Certificate_AICTE_DrBharati.pdf', crit: 'Criterion 5', context: 'Faculty / Dr. Bharati Reshmi', by: 'Dr. Bharati Reshmi', date: '2026-08-12', aiType: 'FDP Certificate (5 Days)', status: 'Verified ✅' },
  { name: 'GPU_Server_Calibration_Certificate.pdf', crit: 'Criterion 7', context: 'AI Lab 301 / Dr. Anand Rao', by: 'Lab Incharge', date: '2026-07-28', aiType: 'Equipment Calibration & Safety', status: 'Verified ✅' },
  { name: 'Student_Exit_Survey_2025_Indirect_Attainment.xlsx', crit: 'Criterion 3', context: 'Batch 2021-25 Exit Feedback', by: 'NBA Coordinator', date: '2026-06-30', aiType: 'Survey Marks Matrix', status: 'Verified ✅' }
];

function initDocumentsData() {
  const tbody = document.getElementById('documentsTableBody');
  if (!tbody) return;

  tbody.innerHTML = documentsList.map(doc => {
    let statusBadge = '<span class="status-pill success">Verified ✅</span>';
    if (doc.status.includes('Needs Review')) statusBadge = '<span class="status-pill warning">Needs Review ⚠️</span>';

    return `
      <tr>
        <td><strong>${doc.name}</strong></td>
        <td>${doc.crit}</td>
        <td>${doc.context}</td>
        <td>${doc.by}</td>
        <td>${doc.date}</td>
        <td><span style="font-size: 10px; background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px;">${doc.aiType}</span></td>
        <td>${statusBadge}</td>
        <td><button class="btn-secondary" style="padding: 2px 6px; font-size: 10px;" onclick="alert('Viewing extracted metadata for ${doc.name}')">Verify</button></td>
      </tr>
    `;
  }).join('');
}

function filterDocsTable() {
  const query = document.getElementById('docSearchInput').value.toLowerCase();
  const rows = document.querySelectorAll('#documentsTableBody tr');
  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  });
}

/* ============================================================================
   7. AI ASSISTANT
   ============================================================================ */
const aiKnowledgeResponses = {
  'co attainment status': `
    <strong>CO Attainment Analysis for Academic Year 2025-26:</strong><br>
    • Overall CO Attainment across all department courses is currently at <strong>72%</strong>.<br>
    • <strong>Strong Performing Courses:</strong> 22AI62 Deep Neural Networks (88% attainment), 22AI63 Natural Language Processing (82% attainment).<br>
    • <strong>Action Required:</strong> 22AI61 Machine Learning is currently at <strong>62% for CO2</strong> (Target 80%). The Remedial Assessment cycle is recommended to improve attainment before the NBA committee visit.
  `,
  'po gap analysis': `
    <strong>Program Outcome Gap Breakdown:</strong><br>
    • <strong>PO3 (Design/Development of Solutions):</strong> Target 82% vs Attained <strong>58%</strong> (Critical Gap of 24%). Root cause identified in complex optimization questions in Internal Assessment 2.<br>
    • <strong>PO7 (Environment & Sustainability):</strong> Attained <strong>50%</strong>. Recommendation: Inculcate green AI / low-carbon computing assignments.<br>
    • <strong>PO1, PO6, PO11:</strong> Fully satisfied above benchmark (82%, 72%, 74%).
  `,
  'missing documents': `
    <strong>Document AI Audit - Missing Evidence Identified:</strong><br>
    • <strong>Criterion 2 (Course Files):</strong> Machine Learning (22AI61) missing <em>Remedial Class Attendance Log</em> and <em>Feedback Action Taken Report</em>.<br>
    • <strong>Criterion 4 (Students):</strong> 4 internship offer verification letters pending upload from industry portal.<br>
    • <strong>Criterion 5 (Faculty):</strong> FDP attendance certificates pending for 3 junior faculty members.
  `,
  'research summary': `
    <strong>AI & ML Department Research Productivity (2025-26):</strong><br>
    • <strong>Publications:</strong> 42 papers (24 SCI/Scopus indexed journals, 18 IEEE/ACM international conferences).<br>
    • <strong>Patents:</strong> 6 published, 2 granted.<br>
    • <strong>Sponsored Research Grants:</strong> ₹48.5 Lakhs secured from DST and VGST.<br>
    • <strong>Faculty Cadre Participation:</strong> 57% of faculty holding Ph.D., exceeding the NBA minimum cadre recommendation.
  `,
  'readiness suggestions': `
    <strong>Top 3 AI Recommendations to Boost NBA Readiness Score from 78% to 88%+:</strong><br>
    1. <strong>Close Criterion 2 & 8 Loop:</strong> Complete the 3 pending course files (specifically Machine Learning remedial logs).<br>
    2. <strong>Conduct Remedial Assessment for PO3:</strong> Re-test weak students in 22AI61 to demonstrate continuous improvement and elevate PO3 attainment from 58% to 75%+.<br>
    3. <strong>Upload FDP Evidence:</strong> Submit certificates for the 3 faculty members to achieve 100% compliance in Criterion 5.
  `
};

function initAiAssistant() {
  document.querySelectorAll('.ai-chip-btn[data-query]').forEach(btn => {
    btn.addEventListener('click', () => {
      const query = btn.getAttribute('data-query');
      handleAiQuery(query);
    });
  });

  const bannerInput = document.getElementById('bannerAiInput');
  const bannerSendBtn = document.getElementById('bannerAiSendBtn');
  if (bannerSendBtn && bannerInput) {
    bannerSendBtn.addEventListener('click', () => {
      const q = bannerInput.value.trim();
      if (q) {
        handleAiQuery(q);
        bannerInput.value = '';
      }
    });
    bannerInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        const q = bannerInput.value.trim();
        if (q) {
          handleAiQuery(q);
          bannerInput.value = '';
        }
      }
    });
  }
}

function handleAiQuery(query) {
  switchModule('ai-assistant');
  
  const container = document.getElementById('fullChatContainer');
  if (!container) return;

  const userBubble = document.createElement('div');
  userBubble.className = 'chat-bubble user';
  userBubble.innerHTML = `
    <div class="chat-bubble-avatar">You</div>
    <div class="chat-bubble-content">${escapeHtml(query)}</div>
  `;
  container.appendChild(userBubble);

  setTimeout(() => {
    let matchedAnswer = null;
    const lowerQ = query.toLowerCase();

    for (const key in aiKnowledgeResponses) {
      if (lowerQ.includes(key) || key.includes(lowerQ)) {
        matchedAnswer = aiKnowledgeResponses[key];
        break;
      }
    }

    if (!matchedAnswer) {
      matchedAnswer = `
        <strong>Compliance Engine Findings for: "${escapeHtml(query)}"</strong><br>
        Based on the current NBA Digital Twin index for <strong>B.E AI & ML</strong>:<br>
        • All requirements for Criteria 1, 5, 8 and 9 are actively tracked.<br>
        • Department Readiness score stands at <strong>78%</strong>.<br>
        • You can run a full <strong>Virtual NBA Inspection</strong> anytime using the top button to test comprehensive readiness against all 9 NBA evaluators.
      `;
    }

    const botBubble = document.createElement('div');
    botBubble.className = 'chat-bubble bot';
    botBubble.innerHTML = `
      <div class="chat-bubble-avatar">AI</div>
      <div class="chat-bubble-content">${matchedAnswer}</div>
    `;
    container.appendChild(botBubble);
    container.scrollTop = container.scrollHeight;
  }, 350);
}

function sendFullChatMessage() {
  const input = document.getElementById('fullChatInput');
  if (!input) return;
  const q = input.value.trim();
  if (q) {
    handleAiQuery(q);
    input.value = '';
  }
}

function handleFullChatKeypress(e) {
  if (e.key === 'Enter') {
    sendFullChatMessage();
  }
}

function clearChat() {
  const container = document.getElementById('fullChatContainer');
  if (container) {
    container.innerHTML = `
      <div class="chat-bubble bot">
        <div class="chat-bubble-avatar">AI</div>
        <div class="chat-bubble-content">
          Chat cleared. Ask anything regarding NBA criteria, SAR preparation, faculty SFR, or CO-PO calculations!
        </div>
      </div>
    `;
  }
}

/* ============================================================================
   8. VIRTUAL NBA INSPECTION SIMULATION
   ============================================================================ */
function runInspectionSimulation() {
  const startBtn = document.getElementById('btnStartInspectionSimulation');
  const stageText = document.getElementById('inspectStageText');
  const percentText = document.getElementById('inspectPercentText');
  const progressBar = document.getElementById('inspectProgressBar');
  const summaryBox = document.getElementById('inspectSummaryBox');
  const findingsBox = document.getElementById('inspectFindingsBox');

  startBtn.disabled = true;
  summaryBox.style.display = 'none';
  findingsBox.style.display = 'none';

  const stages = [
    { p: 12, text: 'Auditing C1: Vision, Mission & PEO Consistency...' },
    { p: 25, text: 'Evaluating C2: Teaching-Learning & Course Files...' },
    { p: 38, text: 'Analyzing C3: Direct & Indirect Attainment Matrices...' },
    { p: 52, text: 'Verifying C4: Student Performance & Placements...' },
    { p: 65, text: 'Validating C5: Faculty SFR, Cadre & Qualifications...' },
    { p: 78, text: 'Auditing C6: Research, Patents & Consultancy...' },
    { p: 88, text: 'Inspecting C7: Labs, GPUs & Safety Compliance...' },
    { p: 95, text: 'Verifying C8 & C9: Continuous Improvement Loop...' },
    { p: 100, text: 'Virtual NBA Inspection Complete!' }
  ];

  let step = 0;
  const interval = setInterval(() => {
    if (step < stages.length) {
      const current = stages[step];
      stageText.textContent = current.text;
      percentText.textContent = `${current.p}%`;
      progressBar.style.width = `${current.p}%`;
      step++;
    } else {
      clearInterval(interval);
      startBtn.disabled = false;
      startBtn.textContent = 'Re-Run Inspection';
      summaryBox.style.display = 'grid';
      findingsBox.style.display = 'block';
    }
  }, 300);
}

function triggerMachineLearningFix() {
  closeModal('inspectionModal');

  const confirmed = confirm("Simulate Dr. Anand Rao uploading the 2 missing documents (Student Feedback Analysis & Remedial Class Attendance Logs)?");
  if (!confirmed) return;

  const sidebarVal = document.getElementById('sidebar-readiness-val');
  const sidebarBar = document.getElementById('sidebar-readiness-bar');
  const kpiReadiness = document.getElementById('kpi-readiness-val');
  const gaugeReadiness = document.getElementById('gauge-readiness');
  const kpiDocs = document.getElementById('kpi-docs-val');
  const kpiCriteria = document.getElementById('kpi-criteria-val');

  if (sidebarVal) sidebarVal.textContent = '82%';
  if (sidebarBar) sidebarBar.style.width = '82%';
  if (kpiReadiness) kpiReadiness.textContent = '82%';
  if (gaugeReadiness) gaugeReadiness.setAttribute('stroke-dasharray', '82, 100');
  if (kpiDocs) kpiDocs.textContent = '128 / 180';
  if (kpiCriteria) kpiCriteria.textContent = '7 / 10';

  const mlBadge = document.getElementById('ml-coursefile-badge');
  if (mlBadge) {
    mlBadge.className = 'status-pill success';
    mlBadge.textContent = '100% Complete 🟢';
  }

  const gapStatus = document.getElementById('gapCourseFileStatus');
  const resolveBtn = document.getElementById('btnResolveCriticalGap');
  if (gapStatus) {
    gapStatus.textContent = '100% Complete 🟢 (VERIFIED)';
    gapStatus.style.color = '#16a34a';
  }
  if (resolveBtn) {
    resolveBtn.textContent = '✅ Gap Resolved (Evidence Verified)';
    resolveBtn.disabled = true;
    resolveBtn.style.backgroundColor = '#64748b';
  }

  const modalState = document.getElementById('modalCourseFileState');
  if (modalState) {
    modalState.textContent = '100% Complete 🟢';
    modalState.style.color = '#16a34a';
  }

  documentsList.unshift({
    name: '22AI61_Remedial_Classes_Log_Signed.pdf',
    crit: 'Criterion 2 & 8',
    context: 'Machine Learning / Dr. Anand Rao',
    by: 'Dr. Anand Rao',
    date: 'Today',
    aiType: 'Remedial Class Evidence',
    status: 'Verified ✅'
  });
  initDocumentsData();

  alert("🎉 Evidence Verified by Document AI!\n\n1. Feedback analysis & remedial log validated.\n2. Course file 22AI61 is now 100% Complete.\n3. Continuous improvement loop closed.\n4. Department NBA Readiness elevated to 82%!");
}

/* ============================================================================
   9. MODALS & EXPORTS
   ============================================================================ */
function initModals() {
  const btnRunInspection = document.getElementById('btnRunInspection');
  const btnDownloadReport = document.getElementById('btnDownloadReport');
  const notificationBtn = document.getElementById('notificationBtn');
  const btnViewAllAlerts = document.getElementById('btnViewAllAlerts');

  if (btnRunInspection) {
    btnRunInspection.addEventListener('click', () => {
      openModal('inspectionModal');
    });
  }

  if (btnDownloadReport) {
    btnDownloadReport.addEventListener('click', () => {
      openModal('reportModal');
    });
  }

  if (notificationBtn) {
    notificationBtn.addEventListener('click', () => {
      openModal('notificationsModal');
    });
  }

  if (btnViewAllAlerts) {
    btnViewAllAlerts.addEventListener('click', () => {
      openModal('notificationsModal');
    });
  }

  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        overlay.classList.remove('active');
      }
    });
  });
}

function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add('active');
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove('active');
}

function openUploadModal(context) {
  openModal('uploadModal');
}

function simulateFilePick() {
  const extractBox = document.getElementById('documentAiExtractBox');
  const details = document.getElementById('documentAiDetails');
  
  if (extractBox && details) {
    extractBox.style.display = 'block';
    details.innerHTML = `
      <strong>File:</strong> FDP_Certificate_AICTE_DrXYZ.pdf<br>
      <strong>Detected Faculty:</strong> Dr. Anand Rao<br>
      <strong>Program:</strong> Generative AI & Large Language Models FDP<br>
      <strong>Organizer:</strong> National Institute of Technology<br>
      <strong>Duration:</strong> 5 Days (40 Hours)<br>
      <strong>Classification:</strong> FDP Evidence (Criterion 5.3) ✅
    `;
  }
}

function processDocumentUpload() {
  closeModal('uploadModal');
  alert("Document uploaded and indexed! Document AI verified signatures and matched requirements.");
}

function openReportModal() {
  openModal('reportModal');
}

function generateSelectedReport() {
  closeModal('reportModal');
  downloadSampleReport('NBA_Tier1_SAR_Dossier_AIML.pdf');
}

function downloadSampleReport(filename) {
  const blob = new Blob([
    `NBA DIGITAL TWIN - OFFICIAL ACCREDITATION DOSSIER\nDepartment: Artificial Intelligence & Machine Learning\nAcademic Year: 2025-26\nOverall Readiness Score: 82%\nStatus: Compliant\nGenerated On: ${new Date().toLocaleString()}`
  ], { type: 'text/plain' });

  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function exportModuleData(moduleName) {
  downloadSampleReport(`${moduleName}_SAR_Table.csv`);
}

function initFilterControls() {
  const yearSelect = document.getElementById('academicYearSelect');
  const semSelect = document.getElementById('semesterSelect');
  const progSelect = document.getElementById('programmeSelect');

  const handleFilterChange = () => {
    const kpiReadiness = document.getElementById('kpi-readiness-val');
    if (kpiReadiness) {
      kpiReadiness.style.opacity = '0.5';
      setTimeout(() => {
        kpiReadiness.style.opacity = '1';
      }, 200);
    }
  };

  if (yearSelect) yearSelect.addEventListener('change', handleFilterChange);
  if (semSelect) semSelect.addEventListener('change', handleFilterChange);
  if (progSelect) progSelect.addEventListener('change', handleFilterChange);
}

function escapeHtml(string) {
  const div = document.createElement('div');
  div.textContent = string;
  return div.innerHTML;
}
