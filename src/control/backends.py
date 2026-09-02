"""Unified control backends for AutoPlay.

The project deliberately keeps multiple control transports available:
OS input, HID, process/memory, injected/internal control, and packet-level
transport. Implementations can be plugged in independently.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Action:
    kind: str
    value: Any = None
    duration_ms: int = 0

class ControlBackend(ABC):
    name = "abstract"

    @abstractmethod
    def execute(self, action: Action) -> None:
        raise NotImplementedError

    def available(self) -> bool:
        return True

class CompositeControl(ControlBackend):
    name = "composite"

    def __init__(self, backends: list[ControlBackend]) -> None:
        self.backends = backends

    def execute(self, action: Action) -> None:
        for backend in self.backends:
            if backend.available():
                backend.execute(action)
                return
        raise RuntimeError("No available control backend")

class KeyboardMouseBackend(ControlBackend):
    name = "os-input"
    def execute(self, action: Action) -> None:
        raise NotImplementedError("Bind this adapter to the project's OS input layer")

class HIDBackend(ControlBackend):
    name = "hid"
    def execute(self, action: Action) -> None:
        raise NotImplementedError("Bind this adapter to a dedicated HID implementation")

class MemoryBackend(ControlBackend):
    name = "process-memory"
    def execute(self, action: Action) -> None:
        raise NotImplementedError("Bind this adapter to a process-memory implementation")

class InjectionBackend(ControlBackend):
    name = "dll-injection"
    def execute(self, action: Action) -> None:
        raise NotImplementedError("Bind this adapter to the platform-specific injected module")

class PacketBackend(ControlBackend):
    name = "packet"
    def execute(self, action: Action) -> None:
        raise NotImplementedError("Bind this adapter to the project's protocol layer")
