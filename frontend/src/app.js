/**
 * Main Application Router & Controller - NBA Digital Twin (Criterion 3 Focus)
 */

import { api } from './services/api.js';
import { renderSidebar } from './components/Sidebar.js';
import { renderTopbar } from './components/Topbar.js';
import { renderKPICards } from './components/KPICards.js';
import { renderAttainmentCharts } from './components/AttainmentChart.js';
import { renderMappingTable } from './components/MappingTable.js';
import { renderStudentTable } from './components/StudentTable.js';
import { renderGapAnalysis } from './components/GapAnalysis.js';
import { renderAIAssistantModal } from './components/AIAssistantModal.js';
import { renderLoginPage, PRESET_PERSONAS } from './components/LoginPage.js';

class App {
  constructor() {
    this.isLoggedIn = false;
    this.selectedRoleId = 'hod';
    this.currentUser = PRESET_PERSONAS.hod;
    this.currentView = 'dashboard';
    this.data = null;
  }

  async init() {
    // Load dataset from backend API or mock service
    const course = await api.getCourseDetails();
    const outcomes = await api.getOutcomes();
    const mapping = await api.getMapping();
    const assessments = await api.getAssessments();
    const students = await api.getStudents();
    const attainment = await api.getAttainment();

    this.data = { course, outcomes, mapping, assessments, students, attainment };

    this.render();
  }

  render() {
    const container = document.getElementById('app-container');
    if (!container) return;

    if (!this.isLoggedIn) {
      container.innerHTML = renderLoginPage(this.selectedRoleId);
      this.attachLoginEvents();
    } else {
      container.innerHTML = `
        ${renderSidebar(this.currentView)}
        <div id="main-wrapper">
          ${renderTopbar(this.data.course, this.currentUser)}
          <main class="content-body" id="content-body"></main>
        </div>
        ${renderAIAssistantModal()}
      `;
      this.renderCurrentView();
      this.attachDashboardEvents();
    }
  }

  attachLoginEvents() {
    // Role selection grid cards
    document.querySelectorAll('.role-card').forEach(card => {
      card.addEventListener('click', () => {
        const role = card.getAttribute('data-role');
        if (role && PRESET_PERSONAS[role]) {
          this.selectedRoleId = role;
          this.render();
        }
      });
    });

    // Quick demo preset chips
    document.querySelectorAll('[data-quick-login]').forEach(chip => {
      chip.addEventListener('click', () => {
        const role = chip.getAttribute('data-quick-login');
        if (role && PRESET_PERSONAS[role]) {
          this.selectedRoleId = role;
          this.currentUser = PRESET_PERSONAS[role];
          this.isLoggedIn = true;
          this.render();
        }
      });
    });

    // Form submission
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
      loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        this.currentUser = PRESET_PERSONAS[this.selectedRoleId];
        this.isLoggedIn = true;
        this.render();
      });
    }
  }

  renderCurrentView() {
    const contentElem = document.getElementById('content-body');
    if (!contentElem) return;

    const { course, outcomes, mapping, assessments, students, attainment } = this.data;

    if (this.currentView === 'dashboard') {
      contentElem.innerHTML = `
        ${renderKPICards(attainment, outcomes, assessments, students)}
        ${renderGapAnalysis(attainment)}
        ${renderAttainmentCharts(outcomes, attainment)}
      `;
    } else if (this.currentView === 'course-details') {
      contentElem.innerHTML = `
        <div class="card" style="margin-bottom:20px;">
          <div class="card-header">
            <h2 class="card-title">${course.name} (${course.code})</h2>
            <span class="badge badge-info">${course.department}</span>
          </div>
          <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:16px;">
            <div><strong>Credits:</strong> ${course.credits}</div>
            <div><strong>Lecture Hours:</strong> ${course.lectureHours} hrs</div>
            <div><strong>Practical Hours:</strong> ${course.practicalHours} hrs</div>
            <div><strong>Course Coordinator:</strong> ${course.coordinator}</div>
            <div><strong>Target Threshold:</strong> ${course.assessmentScheme.attainmentTarget}%</div>
          </div>
        </div>

        <div class="card">
          <h3 class="card-title" style="margin-bottom:12px;">Criterion 3 Course Objectives & Syllabus Scope</h3>
          <p class="text-muted">This course covers supervised, unsupervised, and deep learning algorithms, enabling students to formulate COs, evaluate predictive performance, and map outcomes directly to NBA Program Outcomes (POs).</p>
        </div>
      `;
    } else if (this.currentView === 'outcomes') {
      const coCardsHtml = outcomes.map(co => `
        <div class="co-card" style="border-left: 4px solid ${co.actualAttainment >= co.target ? '#10b981' : '#ef4444'};">
          <div class="co-card-header">
            <span class="co-tag">${co.id}</span>
            <span class="badge ${co.actualAttainment >= co.target ? 'badge-success' : 'badge-warning'}">${co.status}</span>
          </div>
          <p class="co-statement">${co.statement}</p>
          <div class="co-footer">
            <span>Bloom's: <strong>${co.taxonomy}</strong></span>
            <span>Target: <strong>${co.target}%</strong> | Actual: <strong class="${co.actualAttainment < co.target ? 'text-warning' : 'text-success'}">${co.actualAttainment}%</strong></span>
          </div>
        </div>
      `).join('');

      contentElem.innerHTML = `
        <div class="card-header">
          <h2 class="card-title">Course Outcomes (COs) — Machine Learning Algorithms</h2>
          <span class="badge badge-info">6 COs Defined</span>
        </div>
        <div class="co-card-grid">
          ${coCardsHtml}
        </div>
      `;
    } else if (this.currentView === 'mapping') {
      contentElem.innerHTML = renderMappingTable(mapping);
    } else if (this.currentView === 'assessments') {
      const rowsHtml = assessments.map(a => `
        <tr>
          <td><strong>${a.code}</strong></td>
          <td>${a.name}</td>
          <td>${a.maxMarks} Marks</td>
          <td>${a.mappedCOs.map(co => `<span class="badge badge-info">${co}</span>`).join(' ')}</td>
          <td>${a.date}</td>
          <td><strong>${a.avgScore} / ${a.maxMarks}</strong></td>
        </tr>
      `).join('');

      contentElem.innerHTML = `
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">Criterion 3 Assessment Scheme & Mappings</h2>
            <span class="badge badge-success">CIE 50% | SEE 50%</span>
          </div>
          <div class="table-responsive">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Assessment Code</th>
                  <th>Assessment Description</th>
                  <th>Max Marks</th>
                  <th>Mapped COs</th>
                  <th>Evaluation Date</th>
                  <th>Batch Average</th>
                </tr>
              </thead>
              <tbody>
                ${rowsHtml}
              </tbody>
            </table>
          </div>
        </div>
      `;
    } else if (this.currentView === 'students') {
      contentElem.innerHTML = renderStudentTable(students);
      this.attachStudentFilterEvents();
    } else if (this.currentView === 'attainment') {
      contentElem.innerHTML = `
        ${renderGapAnalysis(attainment)}
        ${renderAttainmentCharts(outcomes, attainment)}
      `;
    }
  }

  attachDashboardEvents() {
    // Navigation items
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const view = link.getAttribute('data-view');
        if (view) {
          this.currentView = view;
          document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
          link.closest('.nav-item').classList.add('active');
          this.renderCurrentView();
        }
      });
    });

    // Switch Role / Logout
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
      logoutBtn.addEventListener('click', () => {
        this.isLoggedIn = false;
        this.render();
      });
    }

    // AI Assistant Modal trigger
    const aiBtn = document.getElementById('open-ai-assistant');
    const aiModal = document.getElementById('ai-modal-backdrop');
    const closeAiBtn = document.getElementById('close-ai-modal');

    if (aiBtn && aiModal) {
      aiBtn.addEventListener('click', () => aiModal.classList.add('active'));
    }
    if (closeAiBtn && aiModal) {
      closeAiBtn.addEventListener('click', () => aiModal.classList.remove('active'));
    }

    // Chat functionality
    const sendBtn = document.getElementById('send-chat-btn');
    const chatInput = document.getElementById('chat-input-text');

    if (sendBtn && chatInput) {
      sendBtn.addEventListener('click', () => this.handleUserQuery(chatInput.value));
      chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') this.handleUserQuery(chatInput.value);
      });
    }

    // Chip suggestions
    document.querySelectorAll('.chip-btn').forEach(chip => {
      chip.addEventListener('click', () => {
        const query = chip.getAttribute('data-query');
        this.handleUserQuery(query);
      });
    });

    // Download SAR Report Button
    const reportBtn = document.getElementById('download-sar-report');
    if (reportBtn) {
      reportBtn.addEventListener('click', () => {
        alert("Generating Criterion 3 SAR PDF Report for Machine Learning Algorithms (22UAI608C)...");
      });
    }
  }

  async handleUserQuery(text) {
    if (!text || !text.trim()) return;
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input-text');
    chatInput.value = '';

    // Append User Message
    const userMsgHtml = `
      <div class="chat-message user">
        <div class="chat-bubble">${text}</div>
      </div>
    `;
    chatMessages.innerHTML += userMsgHtml;
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Query API agent
    const res = await api.queryAIAssistant(text);

    // Append Assistant Response
    const assistantMsgHtml = `
      <div class="chat-message assistant">
        <div class="chat-avatar">AI</div>
        <div>
          <span class="agent-badge">${res.agent}</span>
          <div class="chat-bubble">${res.response.replace(/\n/g, '<br>')}</div>
        </div>
      </div>
    `;
    chatMessages.innerHTML += assistantMsgHtml;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  attachStudentFilterEvents() {
    const searchInput = document.getElementById('student-search');
    const riskSelect = document.getElementById('filter-risk');

    const filterFn = () => {
      const query = searchInput ? searchInput.value.toLowerCase() : '';
      const riskVal = riskSelect ? riskSelect.value : 'ALL';

      document.querySelectorAll('.student-row').forEach(row => {
        const usn = row.cells[0].innerText.toLowerCase();
        const name = row.cells[1].innerText.toLowerCase();
        const risk = row.getAttribute('data-risk');

        const matchesQuery = usn.includes(query) || name.includes(query);
        const matchesRisk = riskVal === 'ALL' || risk === riskVal;

        if (matchesQuery && matchesRisk) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    };

    if (searchInput) searchInput.addEventListener('input', filterFn);
    if (riskSelect) riskSelect.addEventListener('change', filterFn);
  }
}

// Instantiate and launch App on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  const app = new App();
  app.init();
});
