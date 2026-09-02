#pragma once

#include "autoplay/process.hpp"
#include <cstdint>
#include <string>
#include <vector>

namespace autoplay::native {

struct Pattern {
    std::vector<int> bytes; // 0..255 = exact byte, -1 = wildcard
    std::string name;
};

struct PatternMatch {
    std::uintptr_t address{0};
    std::string name;
};

Pattern parse_pattern(const std::string& text);
std::vector<PatternMatch> scan(const Process& process, const Pattern& pattern, bool executable_only = false);

} // namespace autoplay::native
