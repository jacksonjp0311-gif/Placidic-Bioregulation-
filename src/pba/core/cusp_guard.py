def cusp_state(delta_phi: float, tau_1: float, tau_2: float) -> str:
    if delta_phi < tau_1:
        return "continue"
    if delta_phi < tau_2:
        return "caution"
    return "halt-audit"