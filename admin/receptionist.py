from utils import SEP, USERS_FILE, read_lines, write_lines, skip_line, generate_new_id

def register_receptionist():
    print("\n=== REGISTER RECEPTIONIST ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    contact = input("Contact No: ").strip()

    if username == "" or password == "" or name == "":
        print("Username/Password/Name cannot be empty.")
        return

    users = read_lines(USERS_FILE)
    for line in users:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 2 and parts[1] == username:
            print("Username already exists.")
            return

    new_id = generate_new_id("U", USERS_FILE)
    users.append(SEP.join([new_id, username, password, "RECEPTIONIST", name, email, contact]))
    write_lines(USERS_FILE, users)
    print(f"Receptionist registered! ID: {new_id}")

def delete_receptionist():
    print("\n=== DELETE RECEPTIONIST ===")
    rec_id = input("Enter Receptionist ID (e.g., U002): ").strip()

    users = read_lines(USERS_FILE)
    new_users = []
    deleted = False

    for line in users:
        if skip_line(line):
            new_users.append(line)
            continue

        parts = line.split(SEP)
        if len(parts) >= 4 and parts[0] == rec_id and parts[3] == "RECEPTIONIST":
            deleted = True
            continue
        new_users.append(line)

    if not deleted:
        print("Receptionist not found.")
        return

    write_lines(USERS_FILE, new_users)
    print("Receptionist deleted.")
