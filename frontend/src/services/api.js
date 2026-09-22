/**
 * Criterion 3 API Service Layer
 * Consumes backend APIs for Course Details, COs, CO-PO/PSO Mapping,
 * Assessment Mappings, Student Performance, and CO/PO Attainment.
 */

const API_BASE_URL = 'http://localhost:8000/api';

// Realistic Criterion 3 Dataset matching NBA Accreditation Specs & PDF requirements
const CRITERION_3_MOCK_DATA = {
  course: {
    id: "1",
    code: "22UAI608C",
    name: "Machine Learning Algorithms",
    department: "AI & ML Department",
    academicYear: "2025-26",
    semester: "Even Semester (Semester VI)",
    credits: 4,
    lectureHours: 40,
    practicalHours: 30,
    coordinator: "Dr. Bharati Reshmi",
    assessmentScheme: {
      cieWeightage: "50%",
      seeWeightage: "50%",
      attainmentTarget: 70.0
    }
  },

  outcomes: [
    { id: "CO1", statement: "Understand fundamental principles, paradigms, and mathematical foundations of Machine Learning.", taxonomy: "Understand (L2)", target: 70.0, actualAttainment: 82.0, status: "ACHIEVED" },
    { id: "CO2", statement: "Apply supervised learning algorithms (Linear Regression, SVM, Decision Trees) for real-world predictive modeling.", taxonomy: "Apply (L3)", target: 70.0, actualAttainment: 61.0, status: "GAP_IDENTIFIED" },
    { id: "CO3", statement: "Evaluate unsupervised clustering and ensemble learning techniques for pattern analysis.", taxonomy: "Evaluate (L5)", target: 70.0, actualAttainment: 78.0, status: "ACHIEVED" },
    { id: "CO4", statement: "Design and implement artificial neural network architectures and deep learning models.", taxonomy: "Create (L6)", target: 70.0, actualAttainment: 84.0, status: "ACHIEVED" },
    { id: "CO5", statement: "Analyze ethical considerations, bias, and performance metrics in ML deployments.", taxonomy: "Analyze (L4)", target: 70.0, actualAttainment: 76.0, status: "ACHIEVED" },
    { id: "CO6", statement: "Develop hands-on machine learning applications using Python, Scikit-Learn, and PyTorch.", taxonomy: "Apply (L3)", target: 70.0, actualAttainment: 88.0, status: "ACHIEVED" }
  ],

  mapping: {
    pos: ["PO1", "PO2", "PO3", "PO4", "PO5", "PO6", "PO7", "PO8", "PO9", "PO10", "PO11", "PO12"],
    psos: ["PSO1", "PSO2", "PSO3"],
    matrix: [
      // CO1: PO1, PO2, PO3... PSO1
      { co: "CO1", PO1: 3, PO2: 2, PO3: 1, PO4: "-", PO5: 2, PO6: "-", PO7: "-", PO8: "-", PO9: 1, PO10: 1, PO11: "-", PO12: 2, PSO1: 3, PSO2: 2, PSO3: 1 },
      { co: "CO2", PO1: 3, PO2: 3, PO3: 2, PO4: 2, PO5: 3, PO6: 1, PO7: "-", PO8: "-", PO9: 2, PO10: 1, PO11: 1, PO12: 2, PSO1: 3, PSO2: 3, PSO3: 2 },
      { co: "CO3", PO1: 3, PO2: 3, PO3: 3, PO4: 2, PO5: 3, PO6: "-", PO7: "-", PO8: "-", PO9: 1, PO10: 1, PO11: 1, PO12: 2, PSO1: 3, PSO2: 2, PSO3: 2 },
      { co: "CO4", PO1: 3, PO2: 3, PO3: 3, PO4: 3, PO5: 3, PO6: "-", PO7: "-", PO8: 1, PO9: 2, PO10: 1, PO11: 1, PO12: 3, PSO1: 3, PSO2: 3, PSO3: 3 },
      { co: "CO5", PO1: 2, PO2: 2, PO3: 2, PO4: 2, PO5: 2, PO6: 3, PO7: 2, PO8: 3, PO9: 2, PO10: 2, PO11: 1, PO12: 2, PSO1: 2, PSO2: 2, PSO3: 2 },
      { co: "CO6", PO1: 3, PO2: 3, PO3: 3, PO4: 2, PO5: 3, PO6: "-", PO7: "-", PO8: "-", PO9: 3, PO10: 2, PO11: 2, PO12: 3, PSO1: 3, PSO2: 3, PSO3: 3 }
    ],
    averages: {
      PO1: 2.8, PO2: 2.7, PO3: 2.3, PO4: 2.2, PO5: 2.7, PO6: 2.0, PO7: 2.0, PO8: 2.0, PO9: 1.8, PO10: 1.3, PO11: 1.2, PO12: 2.3,
      PSO1: 2.8, PSO2: 2.5, PSO3: 2.0
    }
  },

  assessments: [
    { code: "CIE-I", name: "Continuous Internal Evaluation I", maxMarks: 25, mappedCOs: ["CO1", "CO2"], date: "2026-03-10", avgScore: 18.2 },
    { code: "CIE-II", name: "Continuous Internal Evaluation II", maxMarks: 25, mappedCOs: ["CO3", "CO4"], date: "2026-05-15", avgScore: 19.5 },
    { code: "ASSIGN-1", name: "Supervised Learning Assignment & Case Study", maxMarks: 10, mappedCOs: ["CO2", "CO5"], date: "2026-04-02", avgScore: 7.8 },
    { code: "LAB-EVAL", name: "Practical Lab Examination & Project", maxMarks: 20, mappedCOs: ["CO6"], date: "2026-05-20", avgScore: 17.6 }
  ],

  students: [
    { usn: "1VA23AI001", name: "Aarav Sharma", cie1: 22, cie2: 24, assign: 9, lab: 18, co2Score: 72, riskStatus: "SATISFACTORY" },
    { usn: "1VA23AI002", name: "Ananya Rao", cie1: 14, cie2: 15, assign: 5, lab: 12, co2Score: 52, riskStatus: "AT_RISK" },
    { usn: "1VA23AI003", name: "Dhruv Patel", cie1: 24, cie2: 25, assign: 10, lab: 19, co2Score: 94, riskStatus: "EXCEEDS" },
    { usn: "1VA23AI004", name: "Ishita Verma", cie1: 12, cie2: 14, assign: 6, lab: 11, co2Score: 48, riskStatus: "AT_RISK" },
    { usn: "1VA23AI005", name: "Karthik Nair", cie1: 19, cie2: 21, assign: 8, lab: 16, co2Score: 76, riskStatus: "SATISFACTORY" },
    { usn: "1VA23AI006", name: "Meera Kulkarni", cie1: 21, cie2: 22, assign: 9, lab: 17, co2Score: 82, riskStatus: "SATISFACTORY" },
    { usn: "1VA23AI007", name: "Rohan Gupta", cie1: 11, cie2: 13, assign: 5, lab: 10, co2Score: 44, riskStatus: "AT_RISK" },
    { usn: "1VA23AI008", name: "Sneha Reddy", cie1: 23, cie2: 24, assign: 10, lab: 19, co2Score: 90, riskStatus: "EXCEEDS" }
  ],

  attainmentSummary: {
    overallReadiness: 82,
    attainmentTarget: 70,
    metCOs: 5,
    unmetCOs: 1,
    weakCO: {
      id: "CO2",
      attainment: 61.0,
      target: 70.0,
      gap: -9.0,
      reason: "Students struggled with mathematical formulation of SVM & Logistic Regression decision boundaries in CIE-I and Assignment 1.",
      recommendedAction: "Conduct 2 dedicated practical tutorial sessions on Supervised Learning algorithms, provide hands-on Python notebooks, and conduct a remedial quiz by Oct 15, 2026.",
      assignedFaculty: "Dr. Bharati Reshmi",
      status: "IN_PROGRESS"
    }
  }
};

export const api = {
  async getCourseDetails(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}`);
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Backend API offline; serving Criterion 3 dataset.");
    }
    return CRITERION_3_MOCK_DATA.course;
  },

  async getOutcomes(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}/outcomes`);
      if (res.ok) return await res.json();
    } catch (e) { /* fallback */ }
    return CRITERION_3_MOCK_DATA.outcomes;
  },

  async getMapping(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}/mapping`);
      if (res.ok) return await res.json();
    } catch (e) { /* fallback */ }
    return CRITERION_3_MOCK_DATA.mapping;
  },

  async getAssessments(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}/assessments`);
      if (res.ok) return await res.json();
    } catch (e) { /* fallback */ }
    return CRITERION_3_MOCK_DATA.assessments;
  },

  async getStudents(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}/students`);
      if (res.ok) return await res.json();
    } catch (e) { /* fallback */ }
    return CRITERION_3_MOCK_DATA.students;
  },

  async getAttainment(courseId = "1") {
    try {
      const res = await fetch(`${API_BASE_URL}/courses/${courseId}/attainment`);
      if (res.ok) return await res.json();
    } catch (e) { /* fallback */ }
    return CRITERION_3_MOCK_DATA.attainmentSummary;
  },

  // Simulating Tuba's AI Agents (Coordinator Agent, Assessment Agent, Student Agent)
  async queryAIAssistant(prompt) {
    const p = prompt.toLowerCase();
    
    if (p.includes("co2") || p.includes("attainment of co2")) {
      return {
        agent: "assessment_agent",
        response: "CO2 ('Apply supervised learning techniques') has an actual calculated attainment of **61.0%**, which is **9.0% below the configured target threshold of 70.0%**. The weak performance originated primarily from student performance in CIE-I question Q2 (SVM Formulation)."
      };
    } else if (p.includes("student") || p.includes("cie-i") || p.includes("below threshold")) {
      return {
        agent: "student_agent",
        response: "Analysis of student performance shows **3 out of 60 students scored below the 50% threshold** in CO2:\n- Ananya Rao (USN: 1VA23AI002) - 52%\n- Ishita Verma (USN: 1VA23AI004) - 48%\n- Rohan Gupta (USN: 1VA23AI007) - 44%\nAverage CIE-I score was 18.2 / 25."
      };
    } else if (p.includes("remedial") || p.includes("action") || p.includes("gap")) {
      return {
        agent: "coordinator_agent",
        response: "For the identified CO2 attainment gap (61%), the system recommends the following continuous improvement action:\n1. Conduct 2 extra practical lab tutorials on Supervised Learning.\n2. Re-assess via a remedial quiz by Oct 15, 2026.\nAssigned to: **Dr. Bharati Reshmi**. Status: **In Progress**."
      };
    } else {
      return {
        agent: "coordinator_agent",
        response: "Criterion 3 (Outcome-Based Assessment) status for **Machine Learning Algorithms (22UAI608C)**:\n- **Overall Criterion 3 Readiness**: 82% (Compliant)\n- **COs Met**: 5 of 6 (CO1, CO3, CO4, CO5, CO6 achieved)\n- **Weak CO**: CO2 (61.0% attainment)\n- **Assessments Completed**: 4 / 4"
      };
    }
  }
};
