"""Closed-loop agent orchestrator: observe -> model -> decide -> act -> remember."""
from __future__ import annotations
from dataclasses import dataclass
from time import sleep
from typing import Callable
from perception.interfaces import CaptureBackend, PerceptionBackend
from world.fusion import WorldModel
from memory.episodic import EpisodicMemory
from control.backends import Action, ControlBackend

@dataclass
class Decision:
    action: Action
    thought: str = ""
    reward: float = 0.0

class AgentLoop:
    def __init__(self, capture: CaptureBackend, perception: PerceptionBackend,
                 control: ControlBackend, decide: Callable, memory: EpisodicMemory | None = None):
        self.capture = capture
        self.perception = perception
        self.control = control
        self.decide = decide
        self.world = WorldModel()
        self.memory = memory or EpisodicMemory()
        self.running = False

    def step(self) -> Decision:
        frame = self.capture.capture()
        observation = self.perception.observe(frame)
        state = self.world.update(observation)
        decision = self.decide(state, self.memory)
        self.control.execute(decision.action)
        self.memory.add(observation, decision.action, decision.reward, decision.thought)
        state.last_action = decision.action
        return decision

    def run(self, hz: float = 10.0) -> None:
        self.running = True
        period = 1.0 / max(hz, 0.1)
        while self.running:
            started = __import__('time').monotonic()
            self.step()
            sleep(max(0.0, period - (__import__('time').monotonic() - started)))

    def stop(self) -> None:
        self.running = False
