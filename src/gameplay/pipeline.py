"""Lightweight Context -> Context gameplay pipeline.

This makes perception middleware independently schedulable, which is useful
for expensive OCR/detection tasks that should not run on every frame.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic
from typing import Any, Callable


@dataclass
class PipelineContext:
    frame: Any = None
    state: dict[str, Any] = field(default_factory=dict)
    events: list[str] = field(default_factory=list)
    timestamp: float = field(default_factory=monotonic)


Middleware = Callable[[PipelineContext], PipelineContext]


class ScheduledPipeline:
    """Execute middleware at individual tick intervals."""

    def __init__(self) -> None:
        self._steps: list[tuple[str, int, Middleware, int]] = []
        self._tick = 0

    def add(self, name: str, middleware: Middleware, every: int = 1) -> None:
        if every < 1:
            raise ValueError("every must be >= 1")
        self._steps.append((name, every, middleware, 0))

    def run(self, context: PipelineContext) -> PipelineContext:
        self._tick += 1
        current = context
        updated: list[tuple[str, int, Middleware, int]] = []
        for name, every, middleware, last_tick in self._steps:
            if self._tick - last_tick >= every:
                current = middleware(current)
                last_tick = self._tick
            updated.append((name, every, middleware, last_tick))
        self._steps = updated
        current.timestamp = monotonic()
        return current

    @property
    def tick(self) -> int:
        return self._tick
