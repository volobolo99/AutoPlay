#pragma once
#include "autoplay/process.hpp"
#include <cstdint>
#include <vector>

namespace autoplay::native {

// Resolves a conventional pointer chain: [base] -> +offset0 -> +offset1 ...
// Each dereference is validated through Process::read; no unchecked pointer arithmetic is exposed to Python.
std::uintptr_t resolve_pointer_chain(const Process& process, std::uintptr_t base, const std::vector<std::uintptr_t>& offsets);

} // namespace autoplay::native
