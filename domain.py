import subprocess

def run_dig(domain):
    try:
        command = f"dig @1.1.1.1 {domain} CNAME"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error while running dig for {domain}: {e}")
        return None

def check_cname_output(output):
    return "ns-422.awsdns-52.com. awsdns-hostmaster.amazon.com" in output

def main():
    domains = [
        "example.com",
        "google.com",
        "amazon.com",
        "stackoverflow.com"
    ]

    domains_without_cname = []

    for domain in domains:
        output = run_dig(domain)
        if output and not check_cname_output(output):
            domains_without_cname.append(domain)

    print("Domains without the specified CNAME:")
    for domain in domains_without_cname:
        print(domain)

if __name__ == "__main__":
    main()
