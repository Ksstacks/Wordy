import argparse
import random
from urllib.parse import urlparse

COMMON_PREFIXES = ["dev", "test", "stage", "prod", "api", "app", "web", "internal", "beta", "admin"]
COMMON_SUFFIXES = ["dev", "test", "stage", "old", "v1", "v2", "secure", "new", "01", "backup"]
COMMON_SUBDOMAINS = ["www", "mail", "ftp", "api", "dev", "test", "staging", "admin", "internal", "portal", "vpn", "cpanel", "webmail", "blog", "m"]
COMMON_TLDS = [".com", ".net", ".org", ".dev", ".app", ".xyz"]

def extract_base_domain(domain):
    domain = domain.lower().strip()
    parsed = urlparse(domain)
    hostname = parsed.hostname if parsed.hostname else domain
    parts = hostname.split('.')
    if len(parts) >= 2:
        return parts[-2]  # example.com -> "example"
    return hostname

def generate_manual_wordlist(mode, base, depth):
    wordlist = set()
    if mode == "subdomain":
        for _ in range(depth):
            prefix = random.choice(COMMON_PREFIXES)
            suffix = random.choice(COMMON_SUFFIXES)
            wordlist.add(f"{prefix}-{base}")
            wordlist.add(f"{base}-{suffix}")
            wordlist.add(f"{prefix}.{base}")
            wordlist.add(f"{prefix}{random.randint(1,99)}.{base}")
    elif mode == "domain":
        for _ in range(depth):
            prefix = random.choice(COMMON_PREFIXES)
            suffix = random.choice(COMMON_SUFFIXES)
            wordlist.add(f"{base}{suffix}.com")
            wordlist.add(f"{prefix}{base}.net")
            wordlist.add(f"{base}-{suffix}.org")
            wordlist.add(f"{prefix}-{base}-{suffix}.xyz")
    else:
        raise ValueError("Mode must be 'subdomain' or 'domain'")
    return sorted(wordlist)

def generate_smart_wordlist(domain):
    wordlist = set()
    base = extract_base_domain(domain)
    full = domain.replace("https://", "").replace("http://", "").strip('/')

    # Subdomain patterns
    for sub in COMMON_SUBDOMAINS:
        wordlist.add(f"{sub}.{full}")

    # Variants of the domain itself
    for suffix in COMMON_SUFFIXES:
        wordlist.add(f"{base}-{suffix}")
        wordlist.add(f"{base}{suffix}")
        wordlist.add(f"{suffix}-{base}")
        wordlist.add(f"{base}{suffix}.com")

    # TLD variations
    for tld in COMMON_TLDS:
        wordlist.add(f"{base}{tld}")
        for suffix in COMMON_SUFFIXES:
            wordlist.add(f"{base}-{suffix}{tld}")

    # Numeric variants
    for i in range(1, 4):
        wordlist.add(f"{base}{i}.com")
        wordlist.add(f"{base}-{i}.com")
        wordlist.add(f"{base}{i}")

    return sorted(wordlist)

def main():
    parser = argparse.ArgumentParser(description="Fuzzing Wordlist Generator (Manual & Smart AI-style)")
    parser.add_argument("--mode", choices=["subdomain", "domain"], help="Type of manual wordlist generation")
    parser.add_argument("--base", help="Base name for manual generation (e.g. 'example')")
    parser.add_argument("--depth", type=int, default=100, help="Number of words to generate in manual mode")
    parser.add_argument("--output", required=True, help="Output wordlist file name")
    parser.add_argument("--target", help="Domain name to generate smart AI-style wordlist (e.g. example.com)")

    args = parser.parse_args()

    if args.target:
        wordlist = generate_smart_wordlist(args.target)
        print(f"[+] Smart wordlist generated from domain: {args.target}")
    elif args.mode and args.base:
        wordlist = generate_manual_wordlist(args.mode, args.base, args.depth)
        print(f"[+] Manual wordlist generated in mode '{args.mode}' using base '{args.base}'")
    else:
        parser.error("Either --target or both --mode and --base must be provided.")

    with open(args.output, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"[+] {len(wordlist)} entries written to {args.output}")

if __name__ == "__main__":
    main()
