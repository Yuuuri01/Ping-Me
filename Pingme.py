#!/usr/bin/env python3


import os
import sys
import time
import subprocess
from theme import theme

C_file: str = "engine.c"
BINARY: str = "ping_me"

def cleanup_binary():
    if os.path.exists(BINARY):
        try:
            os.remove(BINARY)
            print(f"\n{theme.GRAY}[|--->] Engine binary cleaned up successfully.{theme.RESET}")
        except Exception as e:
            print(f"{theme.RED}Error cleaning binary: {e}{theme.RESET}")

def install(cmd: str) ->None:
    print(f"{theme.YELLOW}Loading...{theme.RESET}")
    try:
        ins = subprocess.run(
            ["sudo", "apt", "install", "-y", cmd],
            capture_output=True,
            text=True,
            check=True
        )
        print("###################################")
        print(ins.stdout)
        print(f"{theme.GRAY}###################################{theme.RESET}")
        print(f"{theme.GREEN}figlet: Installed successfully!{theme.RESET}")
        print(f"{theme.GRAY}###################################{theme.RESET}\n")
    except:
        print(f"{theme.RED}Error: 'figlet' not found or already installed!{theme.RESET}")
        

def banner() ->None:
    try:
        ins: str = subprocess.run(
            ["figlet", "-f", "slant", "PING-ME"],
            capture_output=True,
            text=True
        )
        print(ins.stdout)
    except:
        check: str = input("'Filget' not found did you want to download it(y/n): ")
        if check in ('y', 'yes'):
            try:
                install("figlet")
                ins: str = subprocess.run(
                    ["figlet", "-f", "slant", "PING-ME"],
                    capture_output=True,
                    text=True
                )
                print(ins.stdout)
            except:
                print(f"{theme.RED}ERROR!{theme.RESET}")

def setup_engine() ->bool:
    # print(f"{theme.GREEN}running the engine...{theme.RESET}")
    out = subprocess.run(
        ["gcc", "-Wall", "-Wextra", "-Werror", C_file, "-o", BINARY],
        capture_output=True,
        text=True
    )

    if out.returncode != 0:
        print(f"{theme.RED}--|>compilation faild: {out.stderr}{theme.RESET}")
        return False
    print(f"{theme.GREEN}--|>Everything is OkEy (wait...)\n{theme.RESET}")
    return True
def cpy_scanner_without_op(ip: str) ->None:
    s_time = time.time()
    try:
        cmd = [f"./{BINARY}", ip]
        res = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        i = 0
        for line in res.stdout:
            if i < 5:
                print(line, end="|->", flush=True)
                i += 1
            else:
                print(line, end=" ", flush=True)
            

        res.wait()
        print("l")

        duration = time.time() - s_time
        print(f"{theme.GREEN}{theme.BOLD}[SUCCESS] Target ip: {ip} scanned in {duration:.2f}s{theme.RESET}\n")
    except Exception as e:
        print(f"{theme.RED}{theme.BOLD}ERROR: {e}{theme.RESET}")
def cpy_scanner_with_op(ip: str, option: str, count: str) ->None:
    s_time = time.time()
    try:
        cmd = [f"./{BINARY}", option, count, ip]
        res = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        i = 0
        flag = 0
        for line in res.stdout:
            if i < int(count):
                print(line, end="|->", flush=True)
                i += 1
                flag = 1
            else:
                print(line, end=" ", flush=True)
        duration = time.time() - s_time
        if flag:
            print(f"{theme.GREEN}{theme.BOLD}[SUCCESS]: Target ip: {ip} scanned in {duration:.2f}s{theme.RESET}")
        
    except Exception as e:
        print(f"{theme.RED}{theme.BOLD}ERROR: {e}{theme.RESET}")

def main():
    banner()
    if len(sys.argv) == 4:
        if setup_engine():
            cpy_scanner_with_op(sys.argv[3], sys.argv[1], sys.argv[2])
            cleanup_binary()

    elif len(sys.argv) == 2 and sys.argv[1] in ("--help", '-h'):
        if setup_engine():
            try:
                cmd = [f"./{BINARY}", sys.argv[1]]
                out = subprocess.run(
                        [f"./{BINARY}", sys.argv[1]],
                        capture_output=True,
                        text=True
                )
                if out.returncode == 0:
                    print(out.stdout)
                else:
                    print(out.stderr)
                cleanup_binary()

            except:
                print(f"{theme.RED}{theme.BOLD}NO MANUAL (Compilation failed){theme.RESET}")
    elif len(sys.argv) == 2:
        if setup_engine():
            cpy_scanner_without_op(sys.argv[1])
            cleanup_binary()

    else:
        print(f"{theme.YELLOW}{theme.BOLD}try: ./cpy_scanner --help{theme.RESET}")

if __name__ == "__main__":
    main()