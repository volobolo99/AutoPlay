#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace autoplay::native {

// Capability-level contracts. Concrete Windows implementations are kept separate
// so the Python planner can select screen, memory, hook, packet or HID channels.
struct ControlResult { bool accepted{false}; std::string message; };

class MemoryControl {
public: virtual ~MemoryControl() = default;
    virtual ControlResult write(std::uintptr_t address, const std::vector<std::uint8_t>& bytes) = 0;
};

class HookControl {
public: virtual ~HookControl() = default;
    virtual ControlResult install(const std::string& symbol, std::uintptr_t target) = 0;
    virtual ControlResult remove(const std::string& symbol) = 0;
};

class PacketChannel {
public: virtual ~PacketChannel() = default;
    virtual ControlResult send(const std::vector<std::uint8_t>& packet) = 0;
};

class HidChannel {
public: virtual ~HidChannel() = default;
    virtual ControlResult send_report(const std::vector<std::uint8_t>& report) = 0;
};

} // namespace autoplay::native
