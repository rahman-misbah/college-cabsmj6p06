ip_set_1 = set()
ip_set_2 = set()

def ip_input(ip_set: set, set_id : int) -> None:
    ip = None

    print(f"IDs from Log {set_id}. Write 0 to end input...\n")

    while ip != "0":
        ip = input("Enter IP: ")
        if ip != "0": ip_set.add(ip)
    
    print()

ip_input(ip_set_1, 1)
ip_input(ip_set_2, 2)

print("Suspicious IPs:", set.intersection(ip_set_1, ip_set_2))
    