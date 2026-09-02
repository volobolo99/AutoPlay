#include "autoplay/pattern_scanner.hpp"
#include <algorithm>
#include <cctype>
#include <sstream>

namespace autoplay::native {

Pattern parse_pattern(const std::string& text) {
    Pattern p;
    std::istringstream in(text);
    std::string token;
    while (in >> token) {
        if (token == "?" || token == "??") p.bytes.push_back(-1);
        else {
            unsigned int value = 0;
            std::stringstream ss;
            ss << std::hex << token;
            ss >> value;
            p.bytes.push_back(static_cast<int>(value & 0xff));
        }
    }
    return p;
}

static bool match_at(const std::vector<std::uint8_t>& data, const Pattern& p, std::size_t i) {
    if (p.bytes.empty() || i + p.bytes.size() > data.size()) return false;
    for (std::size_t j = 0; j < p.bytes.size(); ++j)
        if (p.bytes[j] >= 0 && data[i + j] != static_cast<std::uint8_t>(p.bytes[j])) return false;
    return true;
}

std::vector<PatternMatch> scan(const Process& process, const Pattern& pattern, bool executable_only) {
    std::vector<PatternMatch> hits;
    if (!process.valid() || pattern.bytes.empty()) return hits;

    for (const auto& region : readable_regions(process)) {
#ifdef _WIN32
        constexpr std::uint32_t EXEC_MASK = 0xF0;
        if (executable_only && (region.protection & EXEC_MASK) == 0) continue;
#endif
        std::vector<std::uint8_t> buffer(region.size);
        if (!process.read(region.base, buffer.data(), buffer.size())) continue;
        for (std::size_t i = 0; i + pattern.bytes.size() <= buffer.size(); ++i)
            if (match_at(buffer, pattern, i)) hits.push_back({region.base + i, pattern.name});
    }
    return hits;
}

} // namespace autoplay::native
