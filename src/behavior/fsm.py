"""Deterministic behavior layer inspired by MMORPG bot FSM patterns."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable

class Mode(str, Enum):
    IDLE = "idle"
    NAVIGATE = "navigate"
    COMBAT = "combat"
    LOOT = "loot"
    RECOVER = "recover"
    EMERGENCY = "emergency"

@dataclass
class Context:
    mode: Mode = Mode.IDLE
    data: dict = field(default_factory=dict)

class BehaviorFSM:
    def __init__(self) -> None:
        self.ctx = Context()
        self._handlers: dict[Mode, Callable[[Context], Mode]] = {}

    def register(self, mode: Mode, handler: Callable[[Context], Mode]) -> None:
        self._handlers[mode] = handler

    def tick(self) -> Mode:
        handler = self._handlers.get(self.ctx.mode)
        if handler is None:
            return self.ctx.mode
        self.ctx.mode = handler(self.ctx)
        return self.ctx.mode
