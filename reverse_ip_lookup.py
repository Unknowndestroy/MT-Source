import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Reverse IP Lookup Tool")
    parser.add_argument("ip", help="IP adresi gir")
    args = parser.parse_args()
    response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={args.ip}")
    print(response.text)

if __name__ == "__main__":
    main()
