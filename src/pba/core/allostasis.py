def anticipatory_term(delta_history: list[float], gamma: float) -> float:
    if len(delta_history) < 3:
        return 0.0
    trend = delta_history[-1] - delta_history[-3]
    if trend > 0:
        return -abs(gamma)
    if trend < 0:
        return abs(gamma) * 0.25
    return 0.0