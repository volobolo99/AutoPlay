cmake_minimum_required(VERSION 3.20)
project(AutoPlayNative LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(autoplay_native STATIC
    src/process/process.cpp
    src/process/pattern_scanner.cpp
    src/process/module.cpp
    src/bridge/bridge.cpp
)

target_include_directories(autoplay_native PUBLIC include)

if(WIN32)
    target_compile_definitions(autoplay_native PRIVATE NOMINMAX WIN32_LEAN_AND_MEAN)
    target_link_libraries(autoplay_native PRIVATE psapi user32)
endif()

option(AUTOPLAY_USE_MINHOOK "Enable MinHook integration when provided by the parent build" OFF)
if(AUTOPLAY_USE_MINHOOK)
    target_compile_definitions(autoplay_native PUBLIC AUTOPLAY_USE_MINHOOK=1)
endif()

option(AUTOPLAY_USE_PCAP "Enable PcapPlusPlus/libpcap adapter" OFF)
if(AUTOPLAY_USE_PCAP)
    target_compile_definitions(autoplay_native PUBLIC AUTOPLAY_USE_PCAP=1)
endif()

option(AUTOPLAY_USE_HIDAPI "Enable HIDAPI adapter" OFF)
if(AUTOPLAY_USE_HIDAPI)
    target_compile_definitions(autoplay_native PUBLIC AUTOPLAY_USE_HIDAPI=1)
endif()
