/**
 * ACCREDIX — FileUpload Component
 * Handles drag-and-drop file upload UI with simulated AI OCR extraction
 */

const FileUploadComponent = {
  /**
   * Simulate AI extraction for a given filename
   * @param {string} fileName
   * @returns {Object} Extracted metadata
   */
  simulateAIExtraction(fileName) {
    const lowerName = fileName.toLowerCase();

    if (lowerName.includes('fdp') || lowerName.includes('workshop')) {
      return { type: 'FDP Certificate', criterion: 'C6', faculty: 'Dr. XYZ', date: '10 June 2025', organizer: 'IIT Bombay', confidence: 98.7 };
    } else if (lowerName.includes('patent')) {
      return { type: 'Patent Grant Certificate', criterion: 'C6', faculty: 'Dr. ABC', date: '18 Feb 2025', organizer: 'Indian Patent Office', confidence: 99.1 };
    } else if (lowerName.includes('publication') || lowerName.includes('paper') || lowerName.includes('ieee')) {
      return { type: 'Research Publication PDF', criterion: 'C6', faculty: 'Dr. XYZ', date: '12 Apr 2025', organizer: 'IEEE Transactions', confidence: 97.3 };
    } else if (lowerName.includes('result') || lowerName.includes('marks')) {
      return { type: 'University Exam Result Sheet', criterion: 'C4', faculty: 'N/A', date: 'May 2025', organizer: 'VTU', confidence: 99.5 };
    } else if (lowerName.includes('attendance')) {
      return { type: 'Student Attendance Register', criterion: 'C4', faculty: 'Class Teacher', date: 'Sem VI 2025', organizer: 'CSE Dept.', confidence: 95.2 };
    } else if (lowerName.includes('appointment') || lowerName.includes('degree') || lowerName.includes('phd')) {
      return { type: 'Faculty Qualification Certificate', criterion: 'C5', faculty: 'Prof. PQR', date: '2019', organizer: 'VTU / AICTE', confidence: 96.8 };
    } else {
      return { type: 'Academic Document', criterion: 'C3', faculty: 'Dr. K. S. Sharma', date: 'AY 2025-26', organizer: 'CSE Department', confidence: 88.4 };
    }
  },

  /**
   * Render AI extraction result card HTML
   */
  renderAIPreview(metadata) {
    return `
      <div class="ai-extracted-grid">
        <div><strong>Detected Type:</strong> <span class="badge-tag">${metadata.type}</span></div>
        <div><strong>Mapped Criterion:</strong> <span class="badge-pill">${metadata.criterion}</span></div>
        <div><strong>Faculty / Context:</strong> ${metadata.faculty}</div>
        <div><strong>Date Extracted:</strong> ${metadata.date}</div>
        <div><strong>Organizer / Issuer:</strong> ${metadata.organizer}</div>
        <div><strong>AI Confidence Score:</strong> <span style="color:var(--emerald); font-weight:700;">${metadata.confidence}%</span></div>
      </div>
    `;
  }
};
