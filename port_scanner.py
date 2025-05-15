import os
import socket
from colorama import Fore, Style, init
import time
import argparse

init(autoreset=True)

def print_banner_scanner():
    print(Fore.CYAN + Style.BRIGHT + "#################################")
    print(Fore.YELLOW + "      Port Tarayıcı")
    print(Fore.CYAN + "#################################\n")

def scan_port(target, port, open_ports, closed_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result = s.connect_ex((target, port))
    if result == 0:
        os.system(f'title ✔️ Port {port} açık.')
        print(Fore.GREEN + f"✔️ Port {port} açık.")
        open_ports.append(port)
    else:
        print(Fore.RED + f"❌ Port {port} kapalı.")
        closed_ports.append(port)
    s.close()

def port_scanner(target, start_port, end_port):
    print_banner_scanner()
    print(Fore.MAGENTA + f"{target} adresi {start_port} ile {end_port} portları arasında taranıyor...\n")
    time.sleep(1)

    open_ports = []
    closed_ports = []

    for port in range(start_port, end_port + 1):
        scan_port(target, port, open_ports, closed_ports)

    with open("openports.txt", "w") as f:
        f.write("Açık Portlar:\n")
        for port in open_ports:
            f.write(f"Port {port} açık\n")
        f.write("\nKapalı Portlar:\n")
        for port in closed_ports:
            f.write(f"Port {port} kapalı\n")

    print(Fore.CYAN + "\nPort tarama sonuçları openports.txt dosyasına kaydedildi.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Tarayıcı Aracı")
    parser.add_argument("target", help="Taramak için hedef IP veya alan adı")
    parser.add_argument("-s", "--start", type=int, default=1, help="Başlangıç portu (varsayılan: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Bitiş portu (varsayılan: 1024)")

    args = parser.parse_args()

    port_scanner(args.target, args.start, args.end)
