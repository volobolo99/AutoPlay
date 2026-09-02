"""Pluggable capture and perception interfaces."""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
import numpy as np
from core.models import Observation

@dataclass
class Frame:
    image: np.ndarray
    timestamp: float
    source: str = "screen"
    metadata: dict[str, Any] | None = None

class CaptureBackend(ABC):
    @abstractmethod
    def capture(self) -> Frame:
        raise NotImplementedError

class PerceptionBackend(ABC):
    @abstractmethod
    def observe(self, frame: Frame) -> Observation:
        raise NotImplementedError

class NullPerception(PerceptionBackend):
    def observe(self, frame: Frame) -> Observation:
        return Observation(raw={"frame_source": frame.source})
