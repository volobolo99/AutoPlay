# AutoPlay Native Layer

The Python layer remains the AI/planning brain. This C++20 layer provides optional low-level channels for Windows builds:

- process memory read/write and region enumeration;
- module enumeration;
- AOB/signature scanning;
- pointer-chain resolution;
- a stable Python/native IPC contract;
- capability contracts for memory, hooks, packet transport and HID.

## External components researched

- **MinHook** (`TsudaKageyu/minhook`): x86/x64 API hooking. Its upstream license permits redistribution with attribution and disclaimer retention.
- **PcapPlusPlus** (`seladb/PcapPlusPlus`): packet capture/analysis. Upstream repository currently publishes an Unlicense declaration.
- **HIDAPI** (`libusb/hidapi`): cross-platform HID access; upstream offers BSD-style/original licensing suitable for this architecture.
- **ReClass.NET** (`ReClassNET/ReClass.NET`): useful reverse-engineering/structure-reconstruction reference; kept as a research dependency, not copied wholesale.
- **windows.graphics.capture** and `windows-capture`: useful references for targeted Windows Graphics Capture; the production capture adapter should target the NosTale HWND/client surface rather than the desktop.

No third-party binary, proprietary client data, credentials, or NosTale offsets are committed here. Game-specific addresses/signatures belong in a separate configuration layer and must be discovered/validated for the exact client build.

## Design rule

All channels are peers. The planner can consume fused state from vision, process memory and network telemetry, and the action engine can choose keyboard, HID, memory, hook or packet transport according to capability, confidence and policy.
