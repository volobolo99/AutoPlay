#include "autoplay/module.hpp"

#ifdef _WIN32
#define NOMINMAX
#include <windows.h>
#include <psapi.h>
#endif

namespace autoplay::native {

std::vector<ModuleInfo> modules(const Process& process) {
    std::vector<ModuleInfo> out;
#ifdef _WIN32
    if (!process.valid()) return out;
    HMODULE list[1024]{};
    DWORD needed = 0;
    if (!EnumProcessModulesEx(static_cast<HANDLE>(process.native_handle()), list, sizeof(list), &needed, LIST_MODULES_ALL)) return out;
    const unsigned count = needed / sizeof(HMODULE);
    for (unsigned i = 0; i < count; ++i) {
        MODULEINFO info{};
        if (!GetModuleInformation(static_cast<HANDLE>(process.native_handle()), list[i], &info, sizeof(info))) continue;
        char name[MAX_PATH]{};
        if (!GetModuleBaseNameA(static_cast<HANDLE>(process.native_handle()), list[i], name, MAX_PATH)) continue;
        out.push_back({name, reinterpret_cast<std::uintptr_t>(info.lpBaseOfDll), static_cast<std::size_t>(info.SizeOfImage)});
    }
#else
    (void)process;
#endif
    return out;
}

} // namespace autoplay::native
