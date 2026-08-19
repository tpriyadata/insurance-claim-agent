def router_keeper_node(state: dict) -> str:
    policy = state["policy_status"]
    damage = state["damage_analysis"]
    
    if not policy["is_active"]:
        return "reject"
    if policy["fraud_risk_score"] > 0.15 or not damage["matches_report"]:
        return "escalate"
    
    return "approve"