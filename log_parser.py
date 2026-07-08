import re

log_file = "sample.log"

try:
    with open(log_file, "r") as file:
        data = file.read()

    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)

    print("IP Addresses Found:\n")

    for ip in sorted(set(ips)):
        print(ip)

except FileNotFoundError:
    print("sample.log not found.")
