# insurance-claim-agent


## Core Architecture & Design

## Core Design Principles
**schemas/state.py:** Isolates the global memory context passed between nodes.

**nodes/ vs tools/:** Keeps LLM reasoning nodes separate from pure API call utilities.

**graph/workflow.py:** Contains the compiled graph logic, checkpointers, and human-in-the-loop interruption entry points.

**tests/evals/:** Houses evaluation tests to catch non-deterministic regressions before pushing to production.

**Orchestration Framework:** Uses LangGraph to build a stateful execution graph that handles complex, multi-step agent reasoning, node transitions, and thread persistence.

**Boundary Validation Engine:** Implements Pydantic models as strict type keepers at every boundary—from initial payload ingestion and LLM structured outputs to tool call arguments and dynamic routing logic.

**Multimodal Intelligence:** Utilizes Claude 3.5 Sonnet to evaluate unstructured claims data (text descriptions cross-referenced with photo evidence) for damage scoring and report consistency.


### Key Results & System Outcomes

**Deterministic Containment:** Eliminates runaway agent loops and unexpected execution failures by enforcing strict schemas and hard limits before any financial action (payout) is executed.

**Human-in-the-Loop (HITL) Safety Net:** Automatically diverts high-risk or ambiguous claims (e.g., elevated fraud risk scores or visual report mismatches) to a paused state checkpoint for manual adjuster review.

Audit Lineage: Appends structured, step-by-step audit logs directly to the global state object (ClaimState), providing complete execution tracing via terminal outputs and LangSmith integration.
