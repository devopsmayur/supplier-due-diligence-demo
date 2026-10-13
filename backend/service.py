from datetime import date
from backend.risk import SEVERE_RISK, overall_risk


def evaluate_supplier(payload: dict) -> dict:
    risks = payload.get("risks", {})
    if not isinstance(risks, dict) or any(
        type(value) is not int or not 0 <= value <= 100
        for value in risks.values()
    ):
        raise ValueError("risks must be an object with integer scores from 0 to 100")
    score = overall_risk(risks)
    assessment_status = payload.get("assessment_status", "missing")
    approved = (
        score is not None
        and score < SEVERE_RISK
    )
    return {"approved": approved, "risk_score": score,
            "assessment_status": assessment_status}


def deletion_eligibility(payload: dict, today: date | None = None) -> dict:
    created = date.fromisoformat(payload["created_at"])
    legal_hold = payload.get("legal_hold", False)
    if type(legal_hold) is not bool:
        raise ValueError("legal_hold must be a boolean")
    today = today or date.today()
    try:
        retain_until = created.replace(year=created.year + 1)
    except ValueError:
        retain_until = date(created.year + 1, 3, 1)
    eligible = today >= retain_until and not legal_hold
    return {"eligible": eligible, "retain_until": retain_until.isoformat(),
            "legal_hold": legal_hold}
