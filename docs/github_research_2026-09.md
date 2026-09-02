# GitHub research — low-level AutoPlay expansion

## Decision

The repository should not be limited to `screen -> YOLO -> mouse/keyboard`. Research confirmed useful building blocks for a multimodal agent architecture in which vision, process state and network telemetry are parallel sensors, and keyboard, HID, memory, hook and packet transports are parallel action channels.

## High-value references

| Project | Useful material | AutoPlay treatment |
|---|---|---|
| `ReClassNET/ReClass.NET` | process inspection, memory structure reconstruction, plugins | research reference |
| `TsudaKageyu/minhook` | x86/x64 API hooking | external dependency/adapter |
| `seladb/PcapPlusPlus` | packet capture and protocol parsing | external dependency/adapter |
| `libusb/hidapi` | HID device access | external dependency/adapter |
| `NiiightmareXD/windows-capture` | Windows capture implementation ideas | targeted HWND capture reference |
| `GGotha/tibiaeye` | MMORPG state, waypoint, loot, combat, overlay and telemetry architecture | architecture reference |
| `ckazi/pilot` | visual targeting, combat cycle, waypoint navigation and overlay | architecture reference |
| `doaneruby970-hub/wow-bot` | FSM combat, loot, HP/MP and waypoint flow | architecture reference |
| `wojtas99/Nostale_Bot` | NosTale-specific internal-control architecture | research reference; no blind copying |
| `gmh5225/awesome-game-security` | reverse-engineering workflow and tooling references | research index |

## Native layer now present

`native/` contains an auditable C++20 foundation for process memory, memory-region enumeration, module enumeration, AOB scanning, pointer chains, IPC and channel contracts. It deliberately avoids hard-coded NosTale offsets because those are client-build-specific and should be validated independently.

## License policy

Before vendoring upstream source, AutoPlay records the license and preserves required notices. MinHook was checked directly and permits source/binary redistribution subject to its BSD-style conditions. HIDAPI documents BSD/original licensing choices. PcapPlusPlus currently declares the Unlicense. Sources with unclear licensing remain references only.

## Next technical targets

1. Windows HWND-targeted Graphics Capture backend for the NosTale client surface.
2. Native/Python IPC transport (named pipe or shared memory) with timestamps and sequence numbers.
3. Process-state provider that publishes validated reads into the existing `WorldModel` rather than bypassing it.
4. Signature registry + per-client-build validation and diagnostics.
5. Optional MinHook adapter for observing client events/functions.
6. Packet capture/parser adapter that feeds telemetry into the same world-state fusion layer.
7. HID adapter and capability negotiation.
8. NosTale-specific semantic model: player, NPC, monster, item, portal, map, target, skill and combat state.
9. Replay/telemetry tooling so every decision can be inspected in the overlay.
