#include "autoplay/process.hpp"

#ifdef _WIN32
#define NOMINMAX
#include <windows.h>
#include <psapi.h>
#endif

namespace autoplay::native {

Process::Process(std::uint32_t pid) { open(pid); }
Process::~Process() { close(); }

bool Process::open(std::uint32_t pid, bool write_access) {
    close();
#ifdef _WIN32
    const DWORD access = PROCESS_QUERY_INFORMATION | PROCESS_VM_READ |
        (write_access ? PROCESS_VM_WRITE | PROCESS_VM_OPERATION : 0);
    HANDLE h = OpenProcess(access, FALSE, static_cast<DWORD>(pid));
    if (!h) return false;
    handle_ = h;
    pid_ = pid;
    write_access_ = write_access;
    return true;
#else
    (void)pid; (void)write_access;
    return false;
#endif
}

void Process::close() {
#ifdef _WIN32
    if (handle_) CloseHandle(static_cast<HANDLE>(handle_));
#endif
    handle_ = nullptr;
    pid_ = 0;
    write_access_ = false;
}

bool Process::valid() const noexcept { return handle_ != nullptr; }
std::uint32_t Process::pid() const noexcept { return pid_; }

bool Process::read(std::uintptr_t address, void* out, std::size_t size) const {
#ifdef _WIN32
    if (!handle_ || !out || size == 0) return false;
    SIZE_T done = 0;
    return ReadProcessMemory(static_cast<HANDLE>(handle_), reinterpret_cast<LPCVOID>(address), out, size, &done) && done == size;
#else
    (void)address; (void)out; (void)size;
    return false;
#endif
}

bool Process::write(std::uintptr_t address, const void* data, std::size_t size) const {
#ifdef _WIN32
    if (!handle_ || !write_access_ || !data || size == 0) return false;
    SIZE_T done = 0;
    return WriteProcessMemory(static_cast<HANDLE>(handle_), reinterpret_cast<LPVOID>(address), data, size, &done) && done == size;
#else
    (void)address; (void)data; (void)size;
    return false;
#endif
}

std::vector<MemoryRegion> readable_regions(const Process& process) {
    std::vector<MemoryRegion> result;
#ifdef _WIN32
    if (!process.valid()) return result;
    std::uintptr_t address = 0;
    MEMORY_BASIC_INFORMATION mbi{};
    while (VirtualQueryEx(static_cast<HANDLE>(process.handle_), reinterpret_cast<LPCVOID>(address), &mbi, sizeof(mbi)) == sizeof(mbi)) {
        const DWORD p = mbi.Protect & 0xff;
        const bool readable = mbi.State == MEM_COMMIT &&
            p != PAGE_NOACCESS && p != PAGE_GUARD &&
            (p == PAGE_READONLY || p == PAGE_READWRITE || p == PAGE_WRITECOPY ||
             p == PAGE_EXECUTE_READ || p == PAGE_EXECUTE_READWRITE || p == PAGE_EXECUTE_WRITECOPY);
        if (readable) result.push_back({reinterpret_cast<std::uintptr_t>(mbi.BaseAddress), mbi.RegionSize, mbi.Protect, mbi.State, mbi.Type});
        address = reinterpret_cast<std::uintptr_t>(mbi.BaseAddress) + mbi.RegionSize;
        if (address == 0) break;
    }
#else
    (void)process;
#endif
    return result;
}

} // namespace autoplay::native
