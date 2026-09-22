/**
 * MappingTable Component - CO-PO-PSO Mappings 2D Matrix Table
 */

export function renderMappingTable(mapping) {
  const { pos, psos, matrix, averages } = mapping;

  const headerCols = [...pos, ...psos].map(col => `<th>${col}</th>`).join('');

  const rowsHtml = matrix.map(row => {
    const cols = [...pos, ...psos].map(col => {
      const val = row[col];
      let cellClass = 'cell-none';
      if (val === 3) cellClass = 'cell-high';
      else if (val === 2) cellClass = 'cell-medium';
      else if (val === 1) cellClass = 'cell-low';

      return `<td><span class="matrix-cell ${cellClass}">${val}</span></td>`;
    }).join('');

    return `
      <tr>
        <td><strong>${row.co}</strong></td>
        ${cols}
      </tr>
    `;
  }).join('');

  const avgCols = [...pos, ...psos].map(col => {
    return `<td><strong>${averages[col] || '-'}</strong></td>`;
  }).join('');

  return `
    <div class="card">
      <div class="card-header">
        <div>
          <h2 class="card-title">CO–PO & CO–PSO Mapping Matrix</h2>
          <span class="card-subtitle">Level of correlation: 3 - Substantial (High), 2 - Moderate (Medium), 1 - Slight (Low), '-' - No Correlation</span>
        </div>
        <div class="badge badge-info">Criterion 3.1 & 3.3</div>
      </div>

      <div class="table-responsive">
        <table class="custom-table matrix-table">
          <thead>
            <tr>
              <th>CO Code</th>
              ${headerCols}
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
            <tr style="background-color: #f1f5f9; border-top: 2px solid var(--border-color);">
              <td><strong>Average Strength</strong></td>
              ${avgCols}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  `;
}
