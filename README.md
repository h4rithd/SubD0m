# SubD0m
SubD0m is a Python script to fetch subdomains for a given domain using crt.sh certificate transparency logs.

```
................................
 _____     _   ____  ___       
|   __|_ _| |_|    \|   |_____ 
|__   | | | . |  |  | | |     |
|_____|___|___|____/|___|_|_|_|
                               
...............| by h4rithd.com

usage: subdom.py [-h] -d DOMAIN [-o OUTPUT]
subdom.py: error: the following arguments are required: -d/--domain
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/h4rithd/SubD0m.git
cd SubD0m

2. Install the required libraries:
``` bash
pip install argparse tqdm requests

3. Run the script:
```bash
python subdom.py -d example.com -o subdomains.txt
```

4. Replace example.com with your domain of interest. If you don't specify an output file, subdomains will be printed to the console:
```bash
python subdom.py -d example.com
```

### Command-line Arguments
```bash
-d or --domain: Specifies the domain for which subdomains should be fetched.
-o or --output: Specifies an optional output file to save the subdomains.
```

### Dependencies 
- requests: HTTP library to fetch data from crt.sh.
- tqdm: Library to display progress bars.

### Notes
- The script uses crt.sh's API to fetch subdomains. It may not return all possible subdomains due to limitations in the API.
- The fetched subdomains are sorted alphabetically and duplicates are removed.
- Progress bars are displayed using tqdm during the fetching process.
