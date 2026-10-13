SEVERE_RISK = 80


def overall_risk(risks: dict[str, int]) -> float | None:
    if not risks:
        return None
    return sum(risks.values()) / len(risks)
