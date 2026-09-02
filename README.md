# AutoPlay

Modular autonomous-agent framework for game interaction research.

## Architecture

`Capture -> Perception -> Sensor Fusion -> World Model -> Planner -> Behavior FSM -> Control -> Memory`

The control layer intentionally supports independent backends for keyboard/mouse OS input, dedicated HID, process-memory integration, injected/internal module integration, and packet/protocol integration. These are interfaces, not bundled game-specific implementations.

## Integrated building blocks

- `src/perception`: capture and perception contracts, MSS baseline capture
- `src/vision`: optional Ultralytics detection/tracking adapter
- `src/world`: sensor-fusion world model
- `src/planning`: priority goal selection
- `src/navigation`: A* facade with BFS fallback
- `src/behavior`: deterministic navigation/combat/loot/recovery FSM
- `src/control`: multi-transport action abstraction and safety gate
- `src/memory`: bounded episodic memory and reflection storage
- `src/agent`: closed-loop autonomous orchestration
- `third_party/`: attribution, licenses and source-selection record

## Optional dependencies

```bash
pip install -e '.[all,test]'
pytest
```

The architecture is deliberately game-specific only at adapter boundaries, so models, planners, memory and behavior can be developed without coupling the core to one capture or control transport.
