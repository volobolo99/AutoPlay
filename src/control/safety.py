"""Action safety gate shared by every control backend."""
from __future__ import annotations
from dataclasses import dataclass
from control.backends import Action

@dataclass
class SafetyLimits:
    max_duration_ms: int = 3000
    enabled: bool = True

class SafetyGate:
    def __init__(self, limits: SafetyLimits | None = None):
        self.limits = limits or SafetyLimits()

    def validate(self, action: Action) -> Action:
        if not self.limits.enabled:
            return action
        if action.duration_ms < 0 or action.duration_ms > self.limits.max_duration_ms:
            raise ValueError(f"Action duration outside safety limit: {action.duration_ms}ms")
        if not action.kind:
            raise ValueError("Action kind cannot be empty")
        return action
