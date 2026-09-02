#include "autoplay/pointer_chain.hpp"

namespace autoplay::native {

std::uintptr_t resolve_pointer_chain(const Process& process, std::uintptr_t base, const std::vector<std::uintptr_t>& offsets) {
    std::uintptr_t current = base;
    for (std::uintptr_t offset : offsets) {
        std::uintptr_t next = 0;
        if (!process.read(current + offset, next)) return 0;
        if (next == 0) return 0;
        current = next;
    }
    return current;
}

} // namespace autoplay::native
