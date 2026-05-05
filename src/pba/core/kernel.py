from __future__ import annotations

from .domain import DomainConfig
from .parameters import ParameterManifest
from .state import RuntimeState
from .cusp_guard import cusp_state
from .signal import preserve_signal
from .allostasis import anticipatory_term


def sign(value: float) -> float:
    if value > 0:
        return 1.0
    if value < 0:
        return -1.0
    return 0.0


def run_pba(domain: DomainConfig, params: ParameterManifest, perturbations: list[float]) -> list[dict]:
    x = domain.initial_state
    signal = 1.0
    delta_history: list[float] = []
    records: list[dict] = []

    for t, perturbation in enumerate(perturbations):
        delta_phi = abs(x - domain.target)
        omega = 1.0 / (1.0 + abs(delta_phi))
        grad = sign(x - domain.target)

        signal = preserve_signal(signal, delta_phi, params.alpha, params.kappa)
        allo = anticipatory_term(delta_history, params.gamma)
        correction = -params.eta * omega * grad
        signal_term = params.kappa * (signal - 0.5)
        state = cusp_state(delta_phi, params.tau_1, params.tau_2)

        records.append(
            RuntimeState(
                t=t,
                x_t=x,
                target=domain.target,
                delta_phi=delta_phi,
                omega=omega,
                correction=correction,
                signal=signal,
                allostatic_term=allo,
                perturbation=perturbation,
                cusp_state=state,
            ).to_dict()
        )

        delta_history.append(delta_phi)
        x = x + correction + signal_term + allo + perturbation

    return records