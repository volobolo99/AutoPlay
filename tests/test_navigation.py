from navigation.path_planner import GridPoint, NavigationMap, PathPlanner

def test_bfs_fallback_finds_path():
    world = NavigationMap([[True, True, True], [False, False, True], [True, True, True]])
    path = PathPlanner("bfs").plan(world, GridPoint(0, 0), GridPoint(2, 2))
    assert path[0] == GridPoint(0, 0)
    assert path[-1] == GridPoint(2, 2)

def test_blocked_goal_returns_empty():
    world = NavigationMap([[True, False]])
    assert PathPlanner("bfs").plan(world, GridPoint(0, 0), GridPoint(1, 0)) == []
