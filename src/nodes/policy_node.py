from src.schemas.models import PolicyCheckResult

def policy_node(state: dict) -> dict:
    # Mock database result wrapped in Pydantic contract
    policy_data = PolicyCheckResult(
        is_active=True,
        deductible=500.0,
        fraud_risk_score=0.05
    )
    return {
        "policy_status": policy_data.model_dump(),
        "logs": ["Policy Node: Verified active status and fraud risk score."]
    }