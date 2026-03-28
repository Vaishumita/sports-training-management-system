from utils import SEP, USERS_FILE, read_lines, write_lines, skip_line, generate_new_id

def register_trainee():
    print("\n=== REGISTER TRAINEE ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    name = input("Full Name: ").strip()
    ic = input("IC/Passport: ").strip()
    email = input("Email: ").strip()
    contact = input("Contact No: ").strip()
    address = input("Address: ").strip()

    if username == "" or password == "" or name == "":
        print(" Username/Password/Name cannot be empty.")
        return

    lines = read_lines(USERS_FILE)

    # duplicate username check
    for line in lines:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 2 and parts[1] == username:
            print(" Username already exists.")
            return

    new_id = generate_new_id("U", USERS_FILE)

    new_line = SEP.join([new_id, username, password, "TRAINEE", name, ic, email, contact, address])
    lines.append(new_line)
    write_lines(USERS_FILE, lines)

    print(f" Trainee registered successfully! ID: {new_id}")


