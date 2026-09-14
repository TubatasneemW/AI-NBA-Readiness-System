/**
 * ACCREDIX — DataTable Component
 * Renders searchable, filterable data tables from array data
 */

const DataTableComponent = {
  /**
   * Render a data table into a container
   * @param {string} tbodyId - ID of the <tbody> element
   * @param {Array<Object>} rows - Data rows
   * @param {Function} rowRenderer - Function(row) => HTML string for each <tr>
   * @param {Array<Object>} [filter] - Optional filter. Each item: {key, value, operator}
   */
  render(tbodyId, rows, rowRenderer, filter) {
    const tbody = document.getElementById(tbodyId);
    if (!tbody) return;

    let filtered = rows;
    if (filter && filter.value !== 'ALL') {
      filtered = rows.filter(r => r[filter.key] === filter.value);
    }

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="99" style="text-align:center; padding:20px; color:var(--text-dim);">No records match the current filter.</td></tr>`;
      return;
    }

    tbody.innerHTML = filtered.map(rowRenderer).join('');
  }
};
