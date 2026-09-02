"""Shared data contracts used by perception, planning, memory and control."""
from __future__ import annotations
from dataclasses import dataclass, field
from time import monotonic
from typing import Any

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass
class Entity:
    id: str
    kind: str
    position: Point | None = None
    confidence: float = 1.0
    hp: float | None = None
    max_hp: float | None = None
    distance: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class Observation:
    timestamp: float = field(default_factory=monotonic)
    frame_id: int = 0
    player: Entity | None = None
    entities: list[Entity] = field(default_factory=list)
    map_name: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)

    def nearby(self, kind: str | None = None) -> list[Entity]:
        result = [e for e in self.entities if kind is None or e.kind == kind]
        return sorted(result, key=lambda e: e.distance if e.distance is not None else float("inf"))

@dataclass(frozen=True)
class Goal:
    kind: str
    target_id: str | None = None
    target_position: Point | None = None
    priority: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class WorldState:
    observation: Observation = field(default_factory=Observation)
    active_goal: Goal | None = None
    mode: str = "idle"
    confidence: float = 0.0
    last_action: Any = None
