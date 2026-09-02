# Third-party sources mapped into AutoPlay

| Project | Useful area | AutoPlay treatment |
|---|---|---|
| `lmgame-org/GamingAgent` | observation, trajectory, reflection/memory, perception separation | adapted into `src/memory/episodic.py` |
| `brean/python-pathfinding` | A*, Dijkstra, BFS, bidirectional search, weighted grids | represented by `src/navigation/path_planner.py`; optional dependency can replace fallback |
| `NiiightmareXD/windows-capture` | Windows Graphics Capture / DXGI capture | optional capture backend to be wired into `src/vision/` |
| Ultralytics tracking stack | BoT-SORT / ByteTrack object tracking | optional detector/tracker dependency |
| `GGotha/tibiaeye` | MMORPG architecture: cavebot, loot, combat state, telemetry, adaptive loop | reference only; license must be verified before copying source |
| `ckazi/pilot` | MMO targeting, YOLO detection, waypoint/combat loop, overlay | reference/adaptation only |
| `doaneruby970-hub/wow-bot` | FSM combat, loot, HP/MP, waypoint flow | reference/adaptation only |
| `wojtas99/Nostale_Bot` | NosTale-specific target/loot/waypoint/internal architecture | reference only; do not copy without license review |
| Ragnarok bot projects | memory-driven state, map graph, external input patterns | reference only; platform/game-specific code remains separate |

## Rule
Do not copy assets, binaries, proprietary code, or code with an incompatible/unclear license into AutoPlay. Keep source attribution and license notices for every vendored component.
