email_set_1 = set()
email_set_2 = set()

def email_input(email_set: set, set_id : int) -> None:
    email = None

    print(f"Emails for Campaign {set_id}. Write 0 to end input...\n")

    while email != "0":
        email = input("Enter email: ")
        if email != "0": email_set.add(email)
    
    print()

email_input(email_set_1, 1)
email_input(email_set_2, 2)

print("Master List:", set.union(email_set_1, email_set_2))
    