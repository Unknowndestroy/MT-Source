import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.MAGENTA + Style.BRIGHT + """

   ▄▄▄▄███▄▄▄▄   ███    █▄   ▄█           ███      ▄█      ███      ▄██████▄   ▄██████▄   ▄█       
 ▄██▀▀▀███▀▀▀██▄ ███    ███ ███       ▀█████████▄ ███  ▀█████████▄ ███    ███ ███    ███ ███       
 ███   ███   ███ ███    ███ ███          ▀███▀▀██ ███▌    ▀███▀▀██ ███    ███ ███    ███ ███       
 ███   ███   ███ ███    ███ ███           ███   ▀ ███▌     ███   ▀ ███    ███ ███    ███ ███       
 ███   ███   ███ ███    ███ ███           ███     ███▌     ███     ███    ███ ███    ███ ███       
 ███   ███   ███ ███    ███ ███           ███     ███      ███     ███    ███ ███    ███ ███       
 ███   ███   ███ ███    ███ ███▌    ▄     ███     ███      ███     ███    ███ ███    ███ ███▌    ▄ 
  ▀█   ███   █▀  ████████▀  █████▄▄██    ▄████▀   █▀      ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ 
                            ▀                                                            ▀         

                     """ + Fore.CYAN + "Unknown Destroyer tarafından yapıldı.\n")

def menu():
    tools = {
        "1": "cms_detector.py",
        "2": "dns_resolver.py",
        "3": "harvester.py",
        "4": "port_scanner.py",
        "5": "proxssscanner.py",
        "6": "reverse_ip_lookup.py",
        "7": "sqlinjectscanner.py",
        "8": "subscanner.py",
        "9": "usernameosint.py",
        "10": "vulnerability_scanner.py",
        "11": "whois.py",
        "0": "ÇIKIŞ"
    }

    while True:
        clear()
        banner()
        print(Fore.YELLOW + Style.BRIGHT + "Seçmek istediğin aracı yaz:\n")
        for key, val in tools.items():
            print(f" {Fore.GREEN}[{key}]{Fore.RESET} {val}")

        secim = input(Fore.CYAN + "\n > ")

        if secim == "0":
            print(Fore.RED + "\nÇıkıyon moruq... hadi eyw")
            break
        elif secim in tools:
            tool_name = tools[secim]
            print(Fore.BLUE + f"\nSeçtin: {tool_name}")
            arguman = input(Fore.CYAN + "Argüman(lar) ne? (örn: -u example.com): ")
            komut = f'python {tool_name} {arguman}'
            print(Fore.LIGHTMAGENTA_EX + f"\n> Çalıştırılıyor: {komut}\n")
            os.system(komut)
            input(Fore.YELLOW + "\nDevam etmek için ENTER bas...")
        else:
            print(Fore.RED + "\nNe yaptın la sen? Düzgün bişey seç.")
            input("Enter'a bas da geri dönelim...")

menu()
