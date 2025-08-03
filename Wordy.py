import argparse
import random

COMMON_PREFIXES = ["dev", "test", "stage", "prod", "api", "app", "web", "internal", "beta", "admin"]
COMMON_SUFFIXES = ["dev", "test", "stage", "old", "v1", "v2", "secure", "new", "01", "backup"]

def generate_wordlist(mode, base, depth):
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

def main():
    parser = argparse.ArgumentParser(description="Fuzzing Wordlist Generator")
    parser.add_argument("--mode", choices=["subdomain", "domain"], required=True, help="Type of fuzzing wordlist")
    parser.add_argument("--base", required=True, help="Base word (e.g. site name)")
    parser.add_argument("--output", required=True, help="Output wordlist file name")
    parser.add_argument("--depth", type=int, default=100, help="How many words to generate (default: 100)")

    args = parser.parse_args()

    wordlist = generate_wordlist(args.mode, args.base, args.depth)

    with open(args.output, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"[+] Wordlist with {len(wordlist)} entries saved to {args.output}")

if __name__ == "__main__":
    main()
