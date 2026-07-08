import ipaddress

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)

    print(f"\nAddress: {ip_obj}")

    if ip_obj.version == 4:
        print("Version: IPv4")
    else:
        print("Version: IPv6")

    print(f"Private : {ip_obj.is_private}")
    print(f"Global  : {ip_obj.is_global}")
    print(f"Loopback: {ip_obj.is_loopback}")
    print(f"Multicast: {ip_obj.is_multicast}")

except ValueError:
    print("Invalid IP Address")
