from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from src.schemas.state import ClaimState
from src.nodes.vision_node import vision_node
from src.nodes.policy_node import policy_node
from src.nodes.action_node import auto_approve_node, escalate_human_node
from src.graph.router import router_keeper_node

workflow = StateGraph(ClaimState)

workflow.add_node("vision_inspection", vision_node)
workflow.add_node("policy_check", policy_node)
workflow.add_node("auto_approve", auto_approve_node)
workflow.add_node("escalate_human", escalate_human_node)

workflow.set_entry_point("vision_inspection")
workflow.add_edge("vision_inspection", "policy_check")

workflow.add_conditional_edges(
    "policy_check",
    router_keeper_node,
    {
        "approve": "auto_approve",
        "escalate": "escalate_human",
        "reject": END
    }
)

workflow.add_edge("auto_approve", END)
workflow.add_edge("escalate_human", END)

app = workflow.compile(checkpointer=MemorySaver())