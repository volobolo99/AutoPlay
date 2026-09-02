"""Optional adapter around the MIT-licensed python-pathfinding package.

This keeps the external implementation behind an AutoPlay interface so the
rest of the agent does not depend on a third-party API.
"""
from __future__ import annotations

from typing import Iterable

try:
    from pathfinding.core.diagonal_movement import DiagonalMovement
    from pathfinding.core.grid import Grid
    from pathfinding.finder.a_star import AStarFinder
except ImportError:  # optional dependency
    DiagonalMovement = None
    Grid = None
    AStarFinder = None


class AStarAdapter:
    """Plan paths on a 2-D walkability matrix.

    Matrix convention: truthy values are walkable, falsy values are blocked.
    Returned points are ``(x, y)`` tuples, excluding the start point.
    """

    def __init__(self, allow_diagonal: bool = False) -> None:
        self.allow_diagonal = allow_diagonal

    @property
    def available(self) -> bool:
        return Grid is not None and AStarFinder is not None

    def find_path(
        self,
        matrix: Iterable[Iterable[int]],
        start: tuple[int, int],
        goal: tuple[int, int],
    ) -> list[tuple[int, int]]:
        if not self.available:
            raise RuntimeError("Install AutoPlay's 'pathfinding' extra first")

        grid = Grid(matrix=[list(row) for row in matrix], inverse=False)
        start_node = grid.node(*start)
        end_node = grid.node(*goal)
        movement = (
            DiagonalMovement.always
            if self.allow_diagonal
            else DiagonalMovement.never
        )
        finder = AStarFinder(diagonal_movement=movement)
        path, _ = finder.find_path(start_node, end_node, grid)
        return [(node.x, node.y) for node in path[1:]]
