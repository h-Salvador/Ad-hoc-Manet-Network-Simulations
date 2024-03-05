# Project Title

A brief description of what this project does and who it's for.

## Project Overview

Welcome to the Wireless Ad Hoc Network Performance Comparison website! This project evaluates the performance of various routing protocols under security attacks in wireless ad hoc networks. These networks are crucial for applications such as military operations, disaster management, healthcare, and remote sensing. The project aims to provide insights into the strengths and weaknesses of protocols like AODV, DSR, and OLSR under attack scenarios, aiding in the selection of appropriate protocols for secure and efficient communication[1].

## Installation
### Prerequisites

Before you begin the installation, ensure that you have the following prerequisites installed:

- A C++ compiler
- Python3 support
- The CMake build system
- One of the following build systems: make, ninja, or Xcode (for macOS)

### Installation Options

There are two main ways to install ns-3 on Windows:

### Option 1: Windows Subsystem for Linux (WSL)

1. Install WSL2, which runs a real Linux kernel on Windows's Hyper-V hypervisor, providing 100% code compatibility with Linux.
2. Install the WSL extension in Visual Studio Code for better integration.
3. Follow the Linux installation instructions for ns-3, as WSL2 allows you to use Linux commands and packages directly on Windows.

### Option 2: Msys2/MinGW64 Toolchain

1. Install the Msys2 environment, which includes ports of Unix tools for Windows built with multiple toolchains, including MinGW64.
2. Use the MinGW64 (GCC) toolchain, as ns-3 has been tested with it and does not support the 32-bit MinGW32.

## Step-by-Step Installation for Msys2/MinGW64

1. Download and install Msys2 from the official website.
2. Open the Msys2 terminal and update the package database and base packages with:
   ```bash
   pacman -Syu

3. Close the terminal if needed and restart Msys2.
4. Install the necessary packages using:
   ```bash
    pacman -S mingw-w64-x86_64-toolchain mingw-w64-x86_64-cmake make python3
5. Add the MinGW64 binary path to your Windows environment PATH variable.
6. Download the ns-3.41 source code from the ns-3 website.
7. Extract the source code to a directory of your choice.
8. Navigate to the ns-3.41 directory in the Msys2 terminal.
9. Build ns-3 using the following commands:
   ```bash
   mkdir build
   cd build
   cmake ../ -G "MinGW Makefiles"
   make
After Installing ns3 run Simulation.cc .
