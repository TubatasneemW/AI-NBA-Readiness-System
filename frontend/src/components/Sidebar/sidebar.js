/**
 * ACCREDIX — Sidebar Component
 * Handles sidebar navigation rendering and active state management
 */

const SidebarComponent = {
  items: [
    { section: 'OVERVIEW' },
    { id: 'dashboard', icon: 'grid', label: 'Dashboard', sub: null },

    { section: 'ACCREDITATION CRITERIA' },
    { id: 'c3-assessment', badge: 'C3', badgeClass: 'c3-accent', label: 'Assessment & Attainment', sub: 'Outcome Learning (82%)' },
    { id: 'c4-students',   badge: 'C4', badgeClass: 'c4-accent', label: 'Student Performance',     sub: 'Pass & Risk Radar (91%)' },
    { id: 'c5-faculty',    badge: 'C5', badgeClass: 'c5-accent', label: 'Faculty Information',     sub: 'Capacity & Ratio (94%)' },
    { id: 'c6-contributions', badge: 'C6', badgeClass: 'c6-accent', label: 'Faculty Contributions', sub: 'Research & Impact (78%)' },

    { section: 'INTELLIGENCE HUB' },
    { id: 'evidence-center',  iconSvg: 'file-arrow',  label: 'Evidence Center',    badge2: '42',   badge2Class: '' },
    { id: 'ai-assistant',     iconSvg: 'brain',        label: 'AI RAG Assistant',  badge2: 'AI',   badge2Class: 'badge-tag' },
    { id: 'action-center',    iconSvg: 'bolt',         label: 'Action Center',     badge2: '3',    badge2Class: 'count-urgent', id2: 'action-count-badge' },

    { section: 'AUDIT & REPORTING' },
    { id: 'reports', iconSvg: 'document', label: 'SAR & Report Center', sub: null }
  ],

  setActive(tabId) {
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-tab') === tabId);
    });
  }
};
