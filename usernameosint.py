import argparse
import requests

def check_username(username, platforms):
    found = {}
    for name, url in platforms.items():
        resp = requests.get(url.format(username=username))
        if resp.status_code == 200:
            found[name] = url.format(username=username)
    return found

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Username OSINT Tool")
    parser.add_argument("username")
    args = parser.parse_args()
    platforms = {
        "Twitter": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}",
        "GitHub": "https://github.com/{username}",
        "Reddit": "https://www.reddit.com/user/{username}",
        "Facebook": "https://www.facebook.com/{username}",
        "TikTok": "https://www.tiktok.com/@{username}",
        "YouTube": "https://www.youtube.com/{username}",
        "Pinterest": "https://www.pinterest.com/{username}",
        "Medium": "https://medium.com/@{username}"
    }
    results = check_username(args.username, platforms)
    if results:
        for platform, link in results.items():
            print(f"{platform}: {link}")
    else:
        print("No accounts found")
