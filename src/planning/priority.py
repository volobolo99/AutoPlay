"""Goal selection layer: deterministic priorities before an LLM/RL planner is added."""
from __future__ import annotations
from core.models import Goal, WorldState

class PriorityPlanner:
    def choose(self, state: WorldState) -> Goal:
        obs = state.observation
        player = obs.player
        if player and player.hp is not None and player.max_hp and player.hp / player.max_hp < 0.25:
            return Goal("recover", priority=100.0)
        loot = obs.nearby("loot")
        if loot:
            return Goal("loot", target_id=loot[0].id, target_position=loot[0].position, priority=70.0)
        enemies = obs.nearby("enemy")
        if enemies:
            return Goal("combat", target_id=enemies[0].id, target_position=enemies[0].position, priority=60.0)
        return Goal("idle", priority=0.0)
