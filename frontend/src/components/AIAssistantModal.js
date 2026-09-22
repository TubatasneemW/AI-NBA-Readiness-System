/**
 * AIAssistantModal Component - Criterion 3 AI Agent Chat UI
 */

export function renderAIAssistantModal() {
  return `
    <div class="modal-backdrop" id="ai-modal-backdrop">
      <div class="modal-container ai-modal-container">
        <div class="modal-header">
          <div class="modal-title">
            <div class="logo-icon" style="width:28px; height:28px; font-size:12px;">AI</div>
            <span>Criterion 3 Multi-Agent Assistant</span>
          </div>
          <button class="close-modal-btn" id="close-ai-modal">&times;</button>
        </div>

        <div class="modal-body" id="chat-body">
          <div class="chat-history" id="chat-messages">
            <div class="chat-message assistant">
              <div class="chat-avatar">AI</div>
              <div>
                <span class="agent-badge">coordinator_agent</span>
                <div class="chat-bubble">
                  Hello Dr. Bharati! I am your <strong>Criterion 3 AI Assistant</strong> powered by the Assessment Agent, Student Agent, and Coordinator Agent.<br><br>
                  I can analyze CO attainments, student performance, assessment mappings, and suggest remedial actions for Machine Learning Algorithms (22UAI608C). How can I assist you today?
                </div>
              </div>
            </div>
          </div>

          <div class="chip-suggestions">
            <button class="chip-btn" data-query="What is the attainment of CO2?">"What is the attainment of CO2?"</button>
            <button class="chip-btn" data-query="Which students scored below the threshold in CIE-I?">"Which students scored below threshold?"</button>
            <button class="chip-btn" data-query="What remedial action is recommended for CO2?">"What remedial action for CO2?"</button>
            <button class="chip-btn" data-query="Give me a summary of Criterion 3 status">"Give C3 status summary"</button>
          </div>
        </div>

        <div class="chat-input-bar">
          <input type="text" class="chat-input" id="chat-input-text" placeholder="Ask a question about Criterion 3, COs, students or attainment...">
          <button class="btn btn-primary" id="send-chat-btn">Send</button>
        </div>
      </div>
    </div>
  `;
}
