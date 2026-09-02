# Native dependencies and provenance

These are intentionally external dependencies/references. Pin versions before enabling them in a release build.

## MinHook
- Upstream: `TsudaKageyu/minhook`
- Purpose: x86/x64 API hooking
- License checked: BSD-style terms in upstream `LICENSE.txt`
- AutoPlay policy: use as an external dependency or vendor with the complete upstream notice.

## PcapPlusPlus
- Upstream: `seladb/PcapPlusPlus`
- Purpose: packet capture/analysis and protocol tooling
- License checked: upstream `LICENSE` currently declares the Unlicense
- AutoPlay policy: external dependency preferred; protocol dissectors remain game-build specific.

## HIDAPI
- Upstream: `libusb/hidapi`
- Purpose: HID enumeration and reports
- License checked: upstream documents GPL-3, BSD-style and original license options
- AutoPlay policy: use BSD/original terms as appropriate and retain notices.

## ReClass.NET
- Upstream: `ReClassNET/ReClass.NET`
- Purpose: memory structure reconstruction and process inspection research
- AutoPlay policy: research/reference only unless a specific component is separately reviewed for license compatibility.

## Windows capture references
- `NiiightmareXD/windows-capture`
- `Nettal/windows.graphics.capture`

These are references for implementing the Windows-specific capture backend. AutoPlay should capture the game client surface by HWND/client-area rather than using a full-desktop screenshot as its primary observation source.
