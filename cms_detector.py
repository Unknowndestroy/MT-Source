#!/usr/bin/env python3
# cms_detector.py

import requests
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CMS_SIGNATURES = {
    'WordPress': ['wp-content', 'wp-includes', 'xmlrpc.php'],
    'Joomla': ['templates/', 'com_content', 'index.php?option=com_'],
    'Drupal': ['sites/default', 'drupal.settings', 'misc/drupal.js'],
    'Magento': ['Mage.Cookies', 'index.php/admin', 'media/catalog/'],
}

def detect_cms(target_url):
    try:
        r = requests.get(target_url, timeout=5, verify=False)
    except Exception as e:
        print(f"[!] Bağlantı hatası amk: {e}")
        return

    body = r.text.lower()
    for cms, sigs in CMS_SIGNATURES.items():
        for sig in sigs:
            if sig.lower() in body:
                print(f"[+] Muhtemel CMS bulundu: {cms}")
                return
    print("[-] CMS tespit edilemedi, siktir et işte.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basit CMS Detector – Hacker Tool")
    parser.add_argument("url", help="Hedef URL (http://domain.com)")
    args = parser.parse_args()
    detect_cms(args.url)
