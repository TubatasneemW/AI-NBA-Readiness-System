/**
 * StudentTable Component - Student Performance Tracking & Risk Filter
 */

export function renderStudentTable(students) {
  const rowsHtml = students.map(s => {
    let badgeClass = 'badge-success';
    let statusText = 'Satisfactory';

    if (s.riskStatus === 'AT_RISK') {
      badgeClass = 'badge-warning';
      statusText = 'At Risk (< 60%)';
    } else if (s.riskStatus === 'EXCEEDS') {
      badgeClass = 'badge-info';
      statusText = 'Exceeds Target';
    }

    return `
      <tr class="student-row" data-risk="${s.riskStatus}">
        <td><strong>${s.usn}</strong></td>
        <td>${s.name}</td>
        <td>${s.cie1} / 25</td>
        <td>${s.cie2} / 25</td>
        <td>${s.assign} / 10</td>
        <td>${s.lab} / 20</td>
        <td class="${s.co2Score < 60 ? 'text-warning' : 'text-success'}"><strong>${s.co2Score}%</strong></td>
        <td><span class="badge ${badgeClass}">${statusText}</span></td>
      </tr>
    `;
  }).join('');

  return `
    <div class="card">
      <div class="card-header">
        <div>
          <h2 class="card-title">Student Performance Tracking (CIE & CO2)</h2>
          <span class="card-subtitle">Performance breakdown for Machine Learning Algorithms (22UAI608C)</span>
        </div>

        <div style="display: flex; gap: 10px;">
          <input type="text" id="student-search" placeholder="Search USN or Name..." class="filter-select" style="width: 200px;">
          <select id="filter-risk" class="filter-select">
            <option value="ALL">All Students</option>
            <option value="AT_RISK">At Risk Only (< 60%)</option>
            <option value="SATISFACTORY">Satisfactory</option>
            <option value="EXCEEDS">Exceeds Target</option>
          </select>
        </div>
      </div>

      <div class="table-responsive">
        <table class="custom-table" id="student-table-elem">
          <thead>
            <tr>
              <th>USN</th>
              <th>Student Name</th>
              <th>CIE-I (25)</th>
              <th>CIE-II (25)</th>
              <th>Assign (10)</th>
              <th>Lab (20)</th>
              <th>CO2 Attainment %</th>
              <th>Risk Status</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>
      </div>
    </div>
  `;
}
