"""Sensor fusion layer: merges vision, memory and optional internal state."""
from __future__ import annotations
from copy import deepcopy
from core.models import Observation, WorldState

class WorldModel:
    def __init__(self) -> None:
        self.state = WorldState()

    def update(self, observation: Observation, *, internal: dict | None = None) -> WorldState:
        obs = deepcopy(observation)
        if internal:
            obs.raw.setdefault("internal", {}).update(internal)
        self.state.observation = obs
        self.state.confidence = self._confidence(obs)
        return self.state

    @staticmethod
    def _confidence(obs: Observation) -> float:
        values = [e.confidence for e in obs.entities]
        if obs.player:
            values.append(obs.player.confidence)
        return sum(values) / len(values) if values else 0.0
