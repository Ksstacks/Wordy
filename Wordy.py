import argparse
import random
import string
from urllib.parse import urlparse

COMMON_PREFIXES = ["www","localhost", "ftp", "webmail", "smtp", "webdisk", "pop", "cpanel", "whm", "ns1", "ns2", "mail", "autodiscover",
"autoconfig", "ns", "test", "m", "blog", "dev", "www2", "ns3", "pop3", "forum", "admin", "mail2", "vpn", "mx" ,"imap",
"old", "new", "mobile", "mysql", "beta", "support", "cp", "secure", "shop", "demo", "dns2", "ns4", "dns1", "static", "lists",
"web", "www1", "img", "news", "portal", "server", "wiki", "api", "media", "images", "www.blog", "backup", "dns", "sql", 
"intranet", "www.forum", "www.test", "stats", "host","video", "mail1", "mx1", "www3", "staging", "www.m", "sip", 
"ads", "ipv4", "remote", "email", "my", "wap", "svn", "store", "cms", "download", "proxy",
"www.dev, ""dev", "test", "stage", "prod", "api", "app", "web", "internal", "beta", "admin"
"www","localhost", "ftp", "webmail", "smtp", "webdisk", "pop", "cpanel", "whm", "ns1", "ns2", "mail", "autodiscover",
"autoconfig", "ns", "test", "m", "blog", "dev", "www2", "ns3", "pop3", "forum", "admin", "mail2", "vpn", "mx" ,"imap",
"old", "new", "mobile", "mysql", "beta", "support", "cp", "secure", "shop", "demo", "dns2", "ns4", "dns1", "static", "lists",
"web", "www1", "img", "news", "portal", "server", "wiki", "api", "media", "images", "www.blog", "backup", "dns", "sql", 
"intranet", "www.forum", "www.test", "stats", "host","video", "mail1", "mx1", "www3", "staging", "www.m", "sip", 
"ads", "ipv4", "remote", "email", "my", "wap", "svn", "store", "cms", "download"]
COMMON_SUFFIXES = ["dev", "test", "stage", "old", "v1", "v2", "secure", "new", "01", "backup"
"www","localhost", "ftp", "webmail", "smtp", "webdisk", "pop", "cpanel", "whm", "ns1", "ns2", "mail", "autodiscover",
"autoconfig", "ns", "test", "m", "blog", "dev", "www2", "ns3", "pop3", "forum", "admin", "mail2", "vpn", "mx" ,"imap",
"old", "new", "mobile", "mysql", "beta", "support", "cp", "secure", "shop", "demo", "dns2", "ns4", "dns1", "static", "lists",
"web", "www1", "img", "news", "portal", "server", "wiki", "api", "media", "images", "www.blog", "backup", "dns", "sql", 
"intranet", "www.forum", "www.test", "stats", "host","video", "mail1", "mx1", "www3", "staging", "www.m", "sip", 
"ads", "ipv4", "remote", "email", "my", "wap", "svn", "store", "cms", "download"]
COMMON_SUBDOMAINS = ["www", "mail", "ftp", "api", "dev", "test", "staging", "admin", "internal", "portal", "vpn", "cpanel", "webmail", "blog", "m"
"www","localhost", "ftp", "webmail", "smtp", "webdisk", "pop", "cpanel", "whm", "ns1", "ns2", "mail", "autodiscover",
"autoconfig", "ns", "test", "m", "blog", "dev", "www2", "ns3", "pop3", "forum", "admin", "mail2", "vpn", "mx" ,"imap",
"old", "new", "mobile", "mysql", "beta", "support", "cp", "secure", "shop", "demo", "dns2", "ns4", "dns1", "static", "lists",
"web", "www1", "img", "news", "portal", "server", "wiki", "api", "media", "images", "www.blog", "backup", "dns", "sql", 
"intranet", "www.forum", "www.test", "stats", "host","video", "mail1", "mx1", "www3", "staging", "www.m", "sip", 
"ads", "ipv4", "remote", "email", "my", "wap", "svn", "store", "cms", "download"]
COMMON_TLDS = [".com", ".net", ".org", ".dev", ".app", ".xyz"]

def extract_base_directory(domian):
    domian = domian.lower().strip()
    parsed = urlparse(domian)
    hostname = parsed.hostname if parsed.hostname else domian
    parts = hostname.split('.')
    if len(parts) >= 2:
        return parts[-2]  # example.com -> "example"
    return hostname

def generate_manual_wordlist(mode, base, depth):
    wordlist = set()
    base = base.replace("https://", "").replace("http://", "").strip('/')
    if mode == "subdomain":
        for _ in range(depth):
            prefix = random.choice(COMMON_PREFIXES)
            suffix = random.choice(COMMON_SUFFIXES)
            wordlist.add(f"{prefix}-{base}")
            wordlist.add(f"{base}-{suffix}")
            wordlist.add(f"{prefix}.{base}")
            wordlist.add(f"{prefix}")
            wordlist.add(f"{suffix}")
            wordlist.add(f"{prefix}{random.randint(1,99)}.{base}")
    elif mode == "domain":
        for _ in range(depth):
            prefix = random.choice(COMMON_PREFIXES)
            suffix = random.choice(COMMON_SUFFIXES)
            sub = ramdom.choice(COMMON_SUBDOMAINS)
            wordlist.add(f"{base}/{suffix}{COMMON_TLDS}")
            wordlist.add(f"{prefix}/{base}{COMMON_TLDS}")
            wordlist.add(f"{sub}.{base}/{suffix}{COMMON_TLDS}")
            wordlist.add(f"{sub}.{base}-{suffix}{COMMON_TLDS}")
            wordlist.add(f"{sub}.{base}{COMMON_TLDS}")
            wordlist.add(f"{base}-{suffix}{COMMON_TLDS}")
            wordlist.add(f"{prefix}-{base}/{suffix}{COMMON_TLDS}")
            wordlist.add(f"{base}{random.randint(1,99)}/{suffix}")
    elif mode == "directory":
        for _ in range(depth):
            prefix = random.choice(COMMON_PREFIXES)
            suffix = random.choice(COMMON_SUFFIXES)
            wordlist.add(f"{suffix}")
            wordlist.add(f"{prefix}")
            wordlist.add(f"{prefix}-{suffix}")
            wordlist.add(f"{prefix}-{base}/{suffix}{COMMON_TLDS}")
            wordlist.add(f"{suffix}{random.randint(1,99)}/{prefix}")
            wordlist.add(f"{suffix}-{random.randint(1,99)}")
            wordlist.add(f"{suffix}{random.randint(1,99)}")
            wordlist.add(f"{prefix}-{random.randint(1,99)}")
            wordlist.add(f"{prefix}{random.randint(1,99)}")
    else:
        raise ValueError("Mode must be 'subdomain', 'directory', or domain")
    return sorted(wordlist)

def generate_smart_wordlist(domian):
    wordlist = set()
    base = extract_base_directory(domain)
    full = domian.replace("https://", "").replace("http://", "").strip('/')

    # Subdirectory patterns
    for sub in COMMON_SUBDOMAINS:
        wordlist.add(f"{sub}.{full}")

    # Variants of the directory itself
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
    parser.add_argument("-m", "--mode", choices=["subdomain", "directory", "domain"], help="Type of manual wordlist generation")
    parser.add_argument("-b", "--base", help="Base name or url for generation (e.g. 'example')")
    parser.add_argument("-d", "--depth", type=int, default=100, help="Number of words to generate in manual mode")
    parser.add_argument("-o", "--output", required=True, help="Output wordlist file name")
    parser.add_argument("-s", "--smart", help="Smart wordlist generation")

    args = parser.parse_args()

    if args.smart:
        wordlist = generate_smart_wordlist(args.base)
        print(f"[+] Smart wordlist generated from directory: {args.base}")
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
