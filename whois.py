import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Whois Lookup Tool")
    parser.add_argument("query", help="Domain veya IP adresi")
    args = parser.parse_args()
    result = subprocess.run(["whois", args.query], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    main()
