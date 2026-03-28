from utils import SEP, USERS_FILE, PROGRAMS_FILE, read_lines, write_lines, skip_line, generate_new_id

def register_coach():
    print("\n=== REGISTER COACH ===")
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
    # Format: Uxxx|username|password|COACH|name|email|contact
    users.append(SEP.join([new_id, username, password, "COACH", name, email, contact]))
    write_lines(USERS_FILE, users)
    print(f"Coach registered! ID: {new_id}")

def delete_coach():
    print("\n=== DELETE COACH ===")
    coach_id = input("Enter Coach ID (e.g., U003): ").strip()

    users = read_lines(USERS_FILE)
    new_users = []
    deleted = False

    for line in users:
        if skip_line(line):
            new_users.append(line)
            continue

        parts = line.split(SEP)
        if len(parts) >= 4 and parts[0] == coach_id and parts[3] == "COACH":
            deleted = True
            continue
        new_users.append(line)

    if not deleted:
        print("Coach not found.")
        return

    write_lines(USERS_FILE, new_users)
    print("Coach deleted.")

def assign_coach_to_program():
    print("\n=== ASSIGN COACH TO PROGRAM ===")
    program_id = input("Enter Program ID (e.g., P001): ").strip()
    coach_id = input("Enter Coach ID (e.g., U003): ").strip()

    # validate coach exists
    coach_ok = False
    users = read_lines(USERS_FILE)
    for line in users:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 4 and parts[0] == coach_id and parts[3] == "COACH":
            coach_ok = True
            break
    if not coach_ok:
        print("Coach ID not found.")
        return

    programs = read_lines(PROGRAMS_FILE)
    updated = False
    new_programs = []

    for line in programs:
        if skip_line(line):
            new_programs.append(line)
            continue

        p = line.split(SEP)
        if len(p) < 5:
            new_programs.append(line)
            continue

        if p[0] == program_id:
            # p[4] is coach_id
            p[4] = coach_id
            new_programs.append(SEP.join(p))
            updated = True
        else:
            new_programs.append(line)

    if not updated:
        print("Program ID not found.")
        return

    write_lines(PROGRAMS_FILE, new_programs)
    print(f"Coach {coach_id} assigned to Program {program_id}")
