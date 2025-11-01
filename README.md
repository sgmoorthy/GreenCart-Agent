# GreenCart Agent

GreenCart Agent is an open-source, fully autonomous booking assistant and microservice stack for organic food marketplaces. It combines product discovery, conversational Q&A (with RAG), session-long personalization, and end-to-end order APIs wrapped in a modern Streamlit UI and FastAPI backend.

***

## Features

- Streamlit UI for a fast, interactive user experience
- FastAPI backend exposes a complete organic product/catalog API
- In-memory RAG-based catalog/document search
- Booking and ordering flow with externalized payment flows (never stores card/PII data)
- Memory system for session, short-term, and long-term preferences (with user control/opt-in)
- MCP (Model Control Plane) compliant model selection and safety policy hooks
- CI/CD with Docker and GitHub Actions
- Audit logging for observability and debugging

***

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (for containerized usage)
- Redis (for production-grade memory, optional for demo)
- [Optional] Chroma/FAISS for scalable vector DB

### Installation

```bash
git clone https://github.com/yourusername/greencart-agent.git
cd greencart-agent
pip install -r requirements.txt
```

### Running Locally

Start Backend:
```bash
uvicorn greencart_backend.main:app --host 0.0.0.0 --port 8000
```

Start Frontend (in another terminal):
```bash
streamlit run greencart_ui/app.py --server.port=8501
```

### Docker

```bash
docker build -t greencart-agent .
docker run -p 8000:8000 -p 8501:8501 greencart-agent
```

***

## Usage

- Access UI at `http://localhost:8501`
- Backend API docs available at `http://localhost:8000/docs`

***

## TODO Checklist

- [x] Streamlit UI for product search, add-to-cart, and checkout
- [x] FastAPI backend with all endpoints from system design
- [x] RAG catalog/document search with provenance in responses
- [x] Booking/order API and fake payment token workflow
- [x] Session and short-term memory support
- [x] Simple audit logging
- [x] Dockerfile for reproducible builds
- [x] GitHub Actions pipeline for CI/CD
- [ ] Switch to persistent Redis/Chroma for production memory (current: in-memory/dict)
- [ ] Extend RAG to use real vector database embeddings
- [ ] Implement user opt-in UI component for long-term memory
- [ ] Add robust error handling and backend health checks
- [ ] Support vendor escalation ("escalate to vendor" button on low RAG score)
- [ ] Integrate secure authentication and authorization (optional)
- [ ] Multi-language support and locale detection

***

## Proposed New Features

- Integrate web scraping for live organic product price/availability updates
- Mobile and PWA-friendly UI enhancements
- Personalized diet/recommendation engine (using embedded preferences)
- OpenAPI/Swagger-first development for stronger API contracts
- Vendor/producer dashboard for inventory management
- Integration with third-party delivery scheduling APIs
- Real-time agent chat history
- LLM-based customer support chatbot in post-booking flow
- End-to-end encrypted memory for maximum privacy

***

## Contributing

PRs are welcome! Please open issues for suggestions and feedback.

***

## License

MIT License

***

If you have ideas for further improvements or see a feature you want to prioritize, [open an issue](https://github.com/yourusername/greencart-agent/issues) or contribute a pull request!