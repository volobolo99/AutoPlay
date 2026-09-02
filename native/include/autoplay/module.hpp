#pragma once

#include "autoplay/process.hpp"
#include <cstdint>
#include <string>
#include <vector>

namespace autoplay::native {

struct ModuleInfo {
    std::string name;
    std::uintptr_t base{0};
    std::size_t size{0};
};

std::vector<ModuleInfo> modules(const Process& process);

} // namespace autoplay::native
