"""Memory and episodic context primitives adapted from ideas in LM Games GamingAgent.

The implementation is intentionally independent from GamingAgent's API stack so
AutoPlay can use it with its own perception/control backends.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Optional
import json

@dataclass
class Transition:
    observation: Any
    action: Any
    reward: Optional[float] = None
    thought: Optional[str] = None
    timestamp: str = ""

    def __post_init__(self) -> None:
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

class EpisodicMemory:
    def __init__(self, max_length: int = 32) -> None:
        self._items: deque[Transition] = deque(maxlen=max_length)
        self.max_length = max_length
        self.reflection: str = ""

    def add(self, observation: Any, action: Any, reward: Optional[float] = None,
            thought: Optional[str] = None) -> None:
        self._items.append(Transition(observation, action, reward, thought))

    def recent(self, n: Optional[int] = None) -> list[Transition]:
        items = list(self._items)
        return items[-n:] if n else items

    def summary(self) -> dict[str, Any]:
        return {
            "trajectory": [asdict(x) for x in self.recent()],
            "reflection": self.reflection,
        }

    def to_json(self) -> str:
        return json.dumps(self.summary(), ensure_ascii=False, default=str)

    def set_reflection(self, text: str) -> None:
        self.reflection = text or ""

    def clear(self) -> None:
        self._items.clear()
        self.reflection = ""
