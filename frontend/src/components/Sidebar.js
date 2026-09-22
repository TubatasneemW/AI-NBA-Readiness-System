/**
 * Sidebar Component - NBA Digital Twin (Criterion 3 Focus)
 */

export function renderSidebar(currentView = 'dashboard') {
  return `
    <aside class="sidebar">
      <div class="sidebar-header">
        <div class="logo-icon">NBA</div>
        <div class="brand-info">
          <span class="brand-title">NBA DIGITAL TWIN</span>
          <span class="brand-subtitle">AI & ML Department</span>
        </div>
      </div>

      <nav class="sidebar-nav">
        <div class="nav-section-title">Criterion 3 Modules</div>
        <ul class="nav-list">
          <li class="nav-item ${currentView === 'dashboard' ? 'active' : ''}">
            <a class="nav-link" data-view="dashboard">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
              <span>Dashboard</span>
              <span class="criterion-tag">C3</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'course-details' ? 'active' : ''}">
            <a class="nav-link" data-view="course-details">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
              <span>Course Details</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'outcomes' ? 'active' : ''}">
            <a class="nav-link" data-view="outcomes">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
              <span>Course Outcomes (COs)</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'mapping' ? 'active' : ''}">
            <a class="nav-link" data-view="mapping">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>
              <span>CO-PO-PSO Mappings</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'assessments' ? 'active' : ''}">
            <a class="nav-link" data-view="assessments">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
              <span>Assessment Scheme</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'students' ? 'active' : ''}">
            <a class="nav-link" data-view="students">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              <span>Student Performance</span>
            </a>
          </li>

          <li class="nav-item ${currentView === 'attainment' ? 'active' : ''}">
            <a class="nav-link" data-view="attainment">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
              <span>CO/PO Attainment & Gaps</span>
            </a>
          </li>
        </ul>
      </nav>

      <div class="sidebar-footer">
        <button class="ai-assistant-btn" id="open-ai-assistant">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          <span>Criterion 3 AI Agent</span>
        </button>
      </div>
    </aside>
  `;
}
