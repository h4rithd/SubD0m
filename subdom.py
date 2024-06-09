import argparse
import requests
import json
from tqdm import tqdm

BANNER = """
................................
 _____     _   ____  ___       
|   __|_ _| |_|    \|   |_____ 
|__   | | | . |  |  | | |     |
|_____|___|___|____/|___|_|_|_|
                               
...............| by h4rithd.com
"""

def get_subdomains(domain, output_file=None):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    response = requests.get(url, stream=True)
    
    if response.status_code != 200:
        print(f"Error fetching data from crt.sh: {response.status_code}")
        return []

    try:
        cert_data = response.json()
    except json.JSONDecodeError:
        print("Error decoding JSON response")
        return []

    subdomains = set()
    for entry in tqdm(cert_data, desc="Fetching subdomains", unit=" entries"):
        if 'name_value' in entry:
            names = entry['name_value'].split('\n')
            for name in names:
                name = name.strip()
                if name.endswith(domain):
                    subdomains.add(name)
    
    if output_file:
        with open(output_file, 'w') as f:
            for subdomain in subdomains:
                f.write(subdomain + '\n')
    
    return sorted(subdomains)

def main():
    parser = argparse.ArgumentParser(description="SubD0m - Fetch subdomains using crt.sh")
    parser.add_argument('-d', '--domain', required=True, help="Domain to fetch subdomains for")
    parser.add_argument('-o', '--output', help="Output file to save subdomains")
    args = parser.parse_args()
    
    domain = args.domain
    output_file = args.output
    
    subdomains = get_subdomains(domain, output_file)
    
    if not output_file:
        for subdomain in subdomains:
            print(subdomain)

if __name__ == "__main__":
    print(BANNER)
    main()

