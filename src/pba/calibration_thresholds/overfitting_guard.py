from __future__ import annotations


def overfitting_penalty(internal_advantage: float, external_advantage: float, stress_advantage: float) -> float:
    return round(abs(float(internal_advantage) - float(external_advantage)) + abs(float(external_advantage) - float(stress_advantage)), 6)


def overfitting_guard_passed(penalty: float, tolerance: float) -> bool:
    return float(penalty) <= float(tolerance)


def overfitting_status(internal_advantage: float, external_advantage: float, stress_advantage: float, tolerance: float) -> dict:
    penalty = overfitting_penalty(internal_advantage, external_advantage, stress_advantage)
    return {
        "overfitting_penalty": penalty,
        "overfitting_tolerance": float(tolerance),
        "overfitting_guard_passed": overfitting_guard_passed(penalty, tolerance),
    }
