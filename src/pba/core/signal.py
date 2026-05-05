def preserve_signal(previous_signal: float, delta_phi: float, alpha: float, kappa: float) -> float:
    omega = 1.0 / (1.0 + abs(delta_phi))
    candidate = alpha * previous_signal + (1.0 - alpha) * omega
    return max(kappa, min(1.0, candidate))