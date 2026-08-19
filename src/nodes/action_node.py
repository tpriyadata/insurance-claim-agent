from src.schemas.models import PayoutToolInput

def auto_approve_node(state: dict) -> dict:
    payout = 2500.0 - state["policy_status"]["deductible"]
    
    # Validate payload before issuing payout
    validated_payout = PayoutToolInput(
        claim_id=state["claim_id"],
        amount=payout
    )
    
    return {
        "payout_amount": validated_payout.amount,
        "status": "APPROVED",
        "logs": [f"Action Node: Issued payout of ${validated_payout.amount}"]
    }

def escalate_human_node(state: dict) -> dict:
    return {
        "status": "ESCALATED",
        "logs": ["Action Node: Flagged claim for manual human review."]
    }