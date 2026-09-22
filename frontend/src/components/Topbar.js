/**
 * Topbar Component - Header, User Persona & Global Academic Year Filters
 */

export function renderTopbar(course, currentUser) {
  const user = currentUser || {
    name: "Dr. Bharati Reshmi",
    title: "Criterion 3 Lead — AI & ML",
    avatar: "BR"
  };

  return `
    <header class="topbar">
      <div class="topbar-left">
        <button class="toggle-sidebar-btn" id="toggle-sidebar">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
        <div class="page-header-info">
          <h1 class="page-title">Criterion 3 — Outcome-Based Assessment</h1>
          <span class="page-subtext">AI & ML Department Digital Twin — NBA Accreditation</span>
        </div>
      </div>

      <div class="topbar-right">
        <button class="btn btn-primary" id="download-sar-report">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Download C3 SAR Report</span>
        </button>

        <div class="user-profile">
          <div class="user-avatar">${user.avatar}</div>
          <div class="user-meta">
            <span class="user-name">${user.name}</span>
            <span class="user-role">${user.title}</span>
          </div>
        </div>

        <button class="btn btn-secondary btn-sm" id="logout-btn" title="Switch Persona / Logout">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
          <span>Switch Persona</span>
        </button>
      </div>
    </header>

    <div class="filter-bar">
      <div class="filter-group">
        <div class="filter-item">
          <span class="filter-label">Academic Year:</span>
          <select class="filter-select" id="year-select">
            <option selected>2025-26</option>
            <option>2024-25</option>
          </select>
        </div>

        <div class="filter-item">
          <span class="filter-label">Semester:</span>
          <select class="filter-select" id="sem-select">
            <option selected>Even Semester (Semester VI)</option>
            <option>Odd Semester (Semester V)</option>
          </select>
        </div>

        <div class="filter-item">
          <span class="filter-label">Course:</span>
          <select class="filter-select" id="course-select">
            <option selected value="1">${course.name} (${course.code})</option>
          </select>
        </div>
      </div>

      <div class="badge badge-success">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
        <span>Active Persona: ${user.roleName || 'HOD'}</span>
      </div>
    </div>
  `;
}
