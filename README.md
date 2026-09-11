
<div align="center">
  <h1>🛡️ PING-ME</h1>
  <p><strong>A Low-Level Hybrid Cybersecurity & Network Diagnostic Tool</strong></p>
  
  ![C99](https://img.shields.io/badge/Language-C99-blue.svg)
  ![Python](https://img.shields.io/badge/Orchestrator-Python_3-yellow.svg)
  ![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)
  ![License](https://img.shields.io/badge/License-MIT-green.svg)
</div>

---

## 📖 Overview

**PING-ME** (formerly `PingMe`) is a professional-grade network diagnostic tool that bridges the gap between high-level user interface control and uncompromising low-level system execution. 

Designed with modern systems engineering principles, this tool features a strict separation of concerns:
* 🐍 **Python Orchestrator**: Manages the CLI, dynamic compilation, real-time output streaming, and automatic workspace cleanup.
* ⚙️ **C99 Execution Engine**: Handles strict parameter validation and safe, low-level process creation using POSIX system calls (`fork`, `execlp`).

## ✨ Key Features

* **Hybrid Architecture**: Combines the rapid development and rich UI of Python with the speed and system-level control of C.
* **Real-Time Streaming**: Utilizes non-blocking pipes (`subprocess.Popen`) to stream ICMP packets exactly like the native `ping` utility.
* **Zero-Persistence Footprint**: The C engine is compiled on-the-fly just before execution and safely purged (`os.remove`) immediately after. No stale binaries are left behind.
* **Strict Compilation**: Built using maximum compiler protection flags (`-Wall -Wextra -Werror`) to ensure secure and warning-free binaries.
* **Interactive UI**: Custom CLI banners (auto-installs `figlet`), color-coded terminal outputs, and built-in manual rendering.

## 🧠 Under the Hood

When you execute `PING-ME`, the following lifecycle occurs:
1. **Validation & UI**: Python parses the arguments and prints the startup banner.
2. **Dynamic Compilation**: Python spawns a compiler process to build `engine.c` into a temporary binary (`pingme`).
3. **Execution & Sandboxing**: 
   * Python invokes the binary and attaches to its `stdout` pipe.
   * The C binary validates inputs (IP, options) and uses `fork()` to spawn a child process.
   * The child process safely replaces its image via `execlp("ping", ...)` while the parent waits.
4. **Data Streaming**: Python continuously reads the pipe in real-time and flushes the output to the user's terminal.
5. **Clean Exit**: Once the scan is complete (or interrupted), execution time is calculated, and the binary is deleted.

## ⚙️ Prerequisites

To run PING-ME, you need a Linux environment (e.g., Kali Linux, Ubuntu) with the following installed:
* Python 3.x
* `gcc` (GNU Compiler Collection)
* `sudo` access (optional, for auto-installing `figlet` banner)

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pingme.git
   cd pingme
   ```

2. **Make the orchestrator executable:**
   ```bash
   chmod +x shield.py
   ```
3. **System-Wide Installation**
  
   If you want to run `pingme` from anywhere in your terminal without typing the full path, run this single command from inside   the `pingme` directory:

```bash
    sudo ln -s $(pwd)/Pingme.py /usr/local/bin/Pingme
```

4. **Run a basic scan:**
   ```bash
   ./shield.py 8.8.8.8
   ```
   *(Defaults to 5 packets)*

5. **Run a custom scan with specific counts:**
   ```bash
   ./shield.py -c 10 1.1.1.1
   ```

6. **Read the internal manual:**
   ```bash
   ./shield.py --help
   # Or
   ./shield.py -h
   ```

## 👨‍💻 Author

Built with ❤️ by **Youri** (1337 / 42 Network Student).
Focusing on low-level memory management, process creation, and cybersecurity tools.

---
*“Simplicity is the ultimate sophistication.”*
