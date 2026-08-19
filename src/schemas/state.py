from typing import List, Optional, Literal
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

# ==========================================
# 1. Pydantic Models for Data Validation
# ==========================================

class VisionInspectionResult(BaseModel):
    """Output schema for multimodal inspection node."""
    damage_score: float = Field(..., ge=0.0, le=1.0, description="Estimated severity score from 0.0 to 1.0")
    report_matches_image: bool = Field(..., description="Whether user description aligns with image evidence")
    detected_issues: List[str] = Field(default_factory=list, description="List of observed damage points")


class PolicyCheckResult(BaseModel):
    """Output schema for policy verification node."""
    is_active: bool = Field(..., description="Whether the insurance policy is active")
    fraud_risk_score: float = Field(..., ge=0.0, le=1.0, description="Calculated fraud risk score")
    coverage_limit: float = Field(..., ge=0.0, description="Maximum allowed coverage payout")
    deductible: float = Field(..., ge=0.0, description="Policy deductible amount")


class PayoutToolInput(BaseModel):
    """Input payload model required for automated payout tool execution."""
    claim_id: str = Field(..., description="Unique claim identifier")
    approved_amount: float = Field(..., gt=0.0, description="Final approved payout amount")
    recipient_account: str = Field(..., description="Target disbursement account")


# ==========================================
# 2. LangGraph State Object (TypedDict)
# ==========================================

class ClaimState(TypedDict):
    """Global execution graph state tracked across all nodes."""
    claim_id: str
    description: str
    image_url: Optional[str]
    claimed_amount: float
    
    # Node execution results
    vision_result: Optional[VisionInspectionResult]
    policy_result: Optional[PolicyCheckResult]
    
    # Workflow status & lineage
    final_status: Literal["PENDING", "APPROVED", "ESCALATED", "REJECTED"]
    payout_amount: float
    logs: List[str]