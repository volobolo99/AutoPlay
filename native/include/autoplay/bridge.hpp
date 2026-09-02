#pragma once

#include <cstdint>
#include <string>

namespace autoplay::native {

struct BridgeMessage {
    std::uint32_t version{1};
    std::uint32_t type{0};
    std::uint64_t sequence{0};
    std::string payload;
};

// Stable boundary for Python <-> native IPC. Transport is intentionally replaceable.
class Bridge {
public:
    virtual ~Bridge() = default;
    virtual bool send(const BridgeMessage& message) = 0;
    virtual bool receive(BridgeMessage& message) = 0;
};

} // namespace autoplay::native
