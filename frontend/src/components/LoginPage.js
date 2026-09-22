/**
 * LoginPage Component - Multi-Persona Professional Login Interface
 */

export const PRESET_PERSONAS = {
  hod: {
    id: "hod",
    roleName: "HOD / Criterion 3 Lead",
    name: "Dr. Bharati Reshmi",
    title: "HOD & Criterion 3 Coordinator — AI & ML",
    email: "bharati.reshmi@nba-digitaltwin.edu",
    avatar: "BR",
    access: "FULL_CRITERION_3"
  },
  teacher: {
    id: "teacher",
    roleName: "Teacher / Faculty",
    name: "Prof. Tuba Tasneem",
    title: "Assistant Professor — Machine Learning",
    email: "tuba.tasneem@nba-digitaltwin.edu",
    avatar: "TT",
    access: "COURSE_FACULTY"
  },
  student: {
    id: "student",
    roleName: "Student",
    name: "Aarav Sharma",
    title: "B.E AI & ML — Sem VI (USN: 1VA23AI001)",
    email: "aarav.sharma@student.nba-digitaltwin.edu",
    avatar: "AS",
    access: "STUDENT_VIEW"
  },
  auditor: {
    id: "auditor",
    roleName: "NBA Auditor / Evaluator",
    name: "Dr. S. K. Verma",
    title: "Senior NBA Accreditation Evaluator",
    email: "sk.verma@nba-india.org",
    avatar: "SV",
    access: "AUDITOR_VIEW"
  }
};

export function renderLoginPage(selectedRoleId = "hod") {
  const currentPersona = PRESET_PERSONAS[selectedRoleId] || PRESET_PERSONAS.hod;

  return `
    <div class="login-wrapper">
      <div class="login-bg-overlay"></div>

      <div class="login-card">
        <div class="login-header">
          <div class="login-logo">NBA</div>
          <h1 class="login-title">NBA DIGITAL TWIN</h1>
          <p class="login-subtitle">AI & ML Department — Accreditation Portal</p>
        </div>

        <div class="role-select-section">
          <span class="role-label">Select Persona / Role:</span>
          <div class="role-grid">
            <div class="role-card ${selectedRoleId === 'hod' ? 'active' : ''}" data-role="hod">
              <div class="role-icon">🏛️</div>
              <div class="role-info">
                <span class="role-name">HOD / C3 Lead</span>
                <span class="role-desc">Full Criterion 3 Audit</span>
              </div>
            </div>

            <div class="role-card ${selectedRoleId === 'teacher' ? 'active' : ''}" data-role="teacher">
              <div class="role-icon">👩‍🏫</div>
              <div class="role-info">
                <span class="role-name">Teacher / Faculty</span>
                <span class="role-desc">Course & Assessment</span>
              </div>
            </div>

            <div class="role-card ${selectedRoleId === 'student' ? 'active' : ''}" data-role="student">
              <div class="role-icon">🎓</div>
              <div class="role-info">
                <span class="role-name">Student</span>
                <span class="role-desc">CO Marks & Feedback</span>
              </div>
            </div>

            <div class="role-card ${selectedRoleId === 'auditor' ? 'active' : ''}" data-role="auditor">
              <div class="role-icon">🔍</div>
              <div class="role-info">
                <span class="role-name">NBA Evaluator</span>
                <span class="role-desc">Virtual Inspection</span>
              </div>
            </div>
          </div>
        </div>

        <form class="login-form" id="login-form">
          <div class="form-group">
            <label class="form-label" for="login-email">Academic Email / ID</label>
            <div class="input-container">
              <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <input type="email" class="form-input" id="login-email" value="${currentPersona.email}" placeholder="name@domain.edu" required>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label" for="login-password">Password</label>
            <div class="input-container">
              <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <input type="password" class="form-input" id="login-password" value="••••••••••••" placeholder="Enter password" required>
            </div>
          </div>

          <div class="form-actions">
            <label class="remember-me">
              <input type="checkbox" checked>
              <span>Remember me</span>
            </label>
            <a href="#" class="forgot-pass" onclick="alert('Password reset link sent to registered email.'); return false;">Forgot Password?</a>
          </div>

          <button type="submit" class="login-submit-btn">
            Login as ${currentPersona.roleName}
          </button>
        </form>

        <div class="demo-preset-section">
          <div class="preset-title">⚡ Quick Demo Login Shortcuts:</div>
          <div class="preset-chips">
            <button class="preset-chip" data-quick-login="hod">🏛️ Dr. Bharati (HOD)</button>
            <button class="preset-chip" data-quick-login="teacher">👩‍🏫 Prof. Tuba (Faculty)</button>
            <button class="preset-chip" data-quick-login="student">🎓 Aarav (Student)</button>
            <button class="preset-chip" data-quick-login="auditor">🔍 Evaluator (Auditor)</button>
          </div>
        </div>
      </div>
    </div>
  `;
}
