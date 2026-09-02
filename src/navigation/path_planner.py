"""Navigation facade with optional A* and dependency-free BFS fallback."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from collections import deque

@dataclass(frozen=True)
class GridPoint:
    x: int
    y: int

class NavigationMap:
    def __init__(self, walkable: Iterable[Iterable[bool]]) -> None:
        self.cells = [list(row) for row in walkable]

    def is_walkable(self, p: GridPoint) -> bool:
        return 0 <= p.y < len(self.cells) and 0 <= p.x < len(self.cells[p.y]) and bool(self.cells[p.y][p.x])

    def neighbors(self, p: GridPoint):
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            q = GridPoint(p.x + dx, p.y + dy)
            if self.is_walkable(q):
                yield q

class PathPlanner:
    def __init__(self, algorithm: str = "astar") -> None:
        self.algorithm = algorithm.lower()

    def plan(self, world: NavigationMap, start: GridPoint, goal: GridPoint) -> list[GridPoint]:
        if not world.is_walkable(start) or not world.is_walkable(goal):
            return []
        if self.algorithm in {"astar", "dijkstra"}:
            try:
                from pathfinding.core.grid import Grid
                from pathfinding.finder.a_star import AStarFinder
                matrix = [[1 if c else 0 for c in row] for row in world.cells]
                grid = Grid(matrix=matrix)
                finder = AStarFinder()
                path, _ = finder.find_path(grid.node(start.x, start.y), grid.node(goal.x, goal.y), grid)
                return [GridPoint(x, y) for x, y in path]
            except ImportError:
                pass
        return self._bfs(world, start, goal)

    @staticmethod
    def _bfs(world, start, goal):
        q = deque([start]); prev = {start: None}
        while q:
            cur = q.popleft()
            if cur == goal: break
            for nxt in world.neighbors(cur):
                if nxt not in prev:
                    prev[nxt] = cur; q.append(nxt)
        if goal not in prev: return []
        path=[]; cur=goal
        while cur is not None:
            path.append(cur); cur=prev[cur]
        return path[::-1]
