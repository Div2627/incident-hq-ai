# IncidentHQ AI: Autonomous Multi-Agent DevOps Incident Mitigation Engine

IncidentHQ AI is a decentralized, self-healing orchestration framework designed to minimize **Mean Time to Resolution (MTTR)** for critical production system anomalies. By decommissioning complex infrastructure incident analysis into isolated, domain-specific intelligent agent nodes, the platform safely identifies root causes, cross-references internal documentation, generates production-grade hotfixes, and runs semantic safety audits within milliseconds.

## 🌐 Live Prototype Console
👉 **Interactive Control Center:** [<PASTE_YOUR_HUGGING_FACE_OR_NGROK_URL_HERE>](<PASTE_YOUR_HUGGING_FACE_OR_NGROK_URL_HERE>)

---

## 🛠️ System Architecture (Sequential Stateful Mesh)
To ensure maximum operational stability, fault isolation, and deterministic execution, the framework utilizes a cooperative multi-agent workflow wrapper instead of monolithic single-prompt architectures:

* **Node 01: Telemetry Triager Agent:** Processes raw incoming runtime error payload streams, isolates the breaking service components (e.g., resource leaks in `database_pool.py`), and builds a target investigation roadmap.
* **Node 02: Infrastructure Investigator Agent:** Executes context-aware semantic retrieval lookups across localized technical documentation stores (`internal_docs.md`) to cross-reference historical configurations and design constraints.
* **Node 03: Remediation Patch Engineer Agent:** Constructs isolated, syntactically correct source-level hotfixes (utilizing safe Python `try/except/finally` structures) to force-close leaking active connection handles.
* **Node 04: Security QA Inspector Agent:** Performs automated syntax profile checks (AST structures) and security verification protocols before authorizing the deployment pipeline wrapper.

## 💻 Tech Stack & Dependencies
- **Core Framework:** FastAPI (Asynchronous High-Performance Web Routing Grid)
- **Application Server:** Uvicorn (Lightning-fast ASGI Implementation)
- **Validation Layer:** Pydantic (Strict Parameter Constraint Enforcement)
- **Interface Layer:** TailwindCSS (Cinematic Deep-Space Telemetry Dashboard)

## 🏃‍♂️ Sandbox Simulation Mode (Local Run)
To facilitate deterministic architecture testing and bypass external API key validation constraints during evaluation cycles, this repository features a localized execution engine that emulates high-fidelity agent token outputs out-of-the-box.

### Installation & Initialization
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Div2627/incident-hq-ai.git](https://github.com/Div2627/incident-hq-ai.git)
   cd incident-hq-ai

   Install dependency packages:
   pip install -r requirements.txt

   Initialize the local runtime server:
   uvicorn main:app --reload --port 8000

   Access the Telemetry Console Dashboard: Open your web browser and navigate to 
   http://127.0.0.1:8000
