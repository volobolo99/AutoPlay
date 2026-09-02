#pragma once

#include <cstddef>
#include <cstdint>
#include <string>
#include <vector>

namespace autoplay::native {

class Process {
public:
    Process() = default;
    explicit Process(std::uint32_t pid);
    ~Process();

    Process(const Process&) = delete;
    Process& operator=(const Process&) = delete;

    bool open(std::uint32_t pid, bool write_access = false);
    void close();
    bool valid() const noexcept;
    std::uint32_t pid() const noexcept;

    bool read(std::uintptr_t address, void* out, std::size_t size) const;
    bool write(std::uintptr_t address, const void* data, std::size_t size) const;

    template <typename T>
    bool read(std::uintptr_t address, T& out) const { return read(address, &out, sizeof(T)); }

    template <typename T>
    bool write(std::uintptr_t address, const T& value) const { return write(address, &value, sizeof(T)); }

private:
    void* handle_{nullptr};
    std::uint32_t pid_{0};
    bool write_access_{false};
};

struct MemoryRegion {
    std::uintptr_t base{0};
    std::size_t size{0};
    std::uint32_t protection{0};
    std::uint32_t state{0};
    std::uint32_t type{0};
};

std::vector<MemoryRegion> readable_regions(const Process& process);

} // namespace autoplay::native
