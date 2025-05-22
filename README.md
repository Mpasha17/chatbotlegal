Architecture of the multi-agent system
The system follows a modular architecture with clear separation of concerns between two specialized agents:
Multi-Agent System Design
Query Agent
Uses vector search to find relevant document sections
Implements document loading, chunking, and embedding
Utilizes Mistral AI embeddings for semantic search
Returns the most relevant document chunks for a given query
Summarization Agent
Extracts key explanations from complex legal topics
Converts legal jargon into plain language
Uses Gemini 2.0 to generate simplified answers
Preserves accuracy while improving readability
System Structure
legal_chatbot/
├── agents/
│   ├── __init__.py
│   ├── query_agent.py       # Handles document retrieval
│   └── summarization_agent.py  # Handles text simplification
├── data/
│   ├── Guide-to-Litigation-in-India.pdf
│   └── Legal-Compliance-Corporate-Laws.pdf
├── __init__.py
├── main.py                  # CLI interface
├── app.py                   # Streamlit web interface
└── requirements.txt         # Dependencies
Flow Diagram
User Query → Query Agent → Relevant Documents → Summarization Agent → Simplified Answer → User
Demo showcasing how the chatbot responds to legal queries
Example Flow
User asks: "What are the steps involved in filing a lawsuit in India?"
Query Agent retrieves relevant sections from legal documents
Summarization Agent converts legal terms into simple steps
System responds with a clear, concise answer
