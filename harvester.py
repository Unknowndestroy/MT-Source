#!/usr/bin/env python3
import argparse
import requests
import re
from bs4 import BeautifulSoup

def harvest_emails(domain):
    emails=set()
    url=f"https://duckduckgo.com/html/?q=site%3A{domain}+%40{domain}"
    resp=requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
    soup=BeautifulSoup(resp.text,"html.parser")
    text=soup.get_text()
    for e in re.findall(r"[a-zA-Z0-9._%+-]+@"+re.escape(domain), text):
        emails.add(e)
    return emails

def harvest_hosts(domain):
    hosts=set()
    url=f"https://api.hackertarget.com/hostsearch/?q={domain}"
    resp=requests.get(url)
    for line in resp.text.splitlines():
        parts=line.split(",")
        if len(parts)==2:
            hosts.add(parts[0].strip())
    return hosts

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("domain")
    args=parser.parse_args()
    es=harvest_emails(args.domain)
    hs=harvest_hosts(args.domain)
    print("Emails:")
    for e in sorted(es):
        print(e)
    print("\nHosts:")
    for h in sorted(hs):
        print(h)

if __name__=="__main__":
    main()
