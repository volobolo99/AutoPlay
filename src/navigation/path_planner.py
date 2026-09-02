"""Navigation facade for grid/pathfinding implementations.

The facade keeps the game-specific world model separate from the algorithm.
Install `pathfinding` (MIT) when using the external implementation.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class GridPoint:
    x: int
    y: int

class NavigationMap:
    def __init__(self, walkable: Iterable[Iterable[bool]]) -> None:
        self.cells = [list(row) for row in walkable]

    def is_walkable(self, p: GridPoint) -> bool:
        return (0 <= p.y < len(self.cells) and 0 <= p.x < len(self.cells[p.y])
                and bool(self.cells[p.y][p.x]))

class PathPlanner:
    """Adapter boundary for A*/Dijkstra/BFS implementations."""
    def __init__(self, algorithm: str = "astar") -> None:
        self.algorithm = algorithm.lower()

    def plan(self, world: NavigationMap, start: GridPoint, goal: GridPoint) -> list[GridPoint]:
        if not world.is_walkable(start) or not world.is_walkable(goal):
            return []
        # A small dependency-free fallback keeps AutoPlay runnable before the
        # optional `pathfinding` package is installed.
        from collections import deque
        q = deque([start])
        prev = {start: None}
        while q:
            cur = q.popleft()
            if cur == goal:
                break
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nxt = GridPoint(cur.x + dx, cur.y + dy)
                if nxt not in prev and world.is_walkable(nxt):
                    prev[nxt] = cur
                    q.append(nxt)
        if goal not in prev:
            return []
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        return list(reversed(path))
