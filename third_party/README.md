# Third-party integration registry

This directory records external projects evaluated for AutoPlay/NosAiProject.

Important: source code is only vendored when its license permits redistribution and when it is actually useful to the project. Repositories with unclear, proprietary, or incompatible licensing are referenced instead of copied wholesale.

## Sources selected for integration/adaptation

- LM Games `GamingAgent` — MIT. Useful concepts: Observation, bounded game trajectory, reflection/memory context, perception/memory separation.
- brean `python-pathfinding` — MIT. Useful algorithms: A*, Dijkstra, BFS, bidirectional search, weighted grids.
- Ultralytics tracking stack — tracking concepts: BoT-SORT / ByteTrack. Kept as a dependency rather than vendoring the whole framework.
- windows-capture — Windows Graphics Capture/DXGI capture. Kept as an optional dependency/backend.
- Other MMORPG bots (TibiaEye, WoW bots, Ragnarok bots, NosTale_Bot) are treated as reference implementations. Their useful architecture is reimplemented behind AutoPlay interfaces rather than copied without a verified redistribution license.

See `docs/third_party_sources.md` for the detailed mapping.