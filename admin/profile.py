from utils import SEP, USERS_FILE, read_lines, write_lines, skip_line

def update_profile_admin(admin_id):
    print("\n=== UPDATE MY PROFILE ===")
    new_name = input("New Name (leave blank to keep): ").strip()
    new_email = input("New Email (leave blank to keep): ").strip()
    new_contact = input("New Contact (leave blank to keep): ").strip()

    users = read_lines(USERS_FILE)
    updated_lines = []
    updated = False

    for line in users:
        if skip_line(line):
            updated_lines.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 4 and parts[0] == admin_id and parts[3] == "ADMIN":
            while len(parts) < 7:
                parts.append("")

            if new_name != "":
                parts[4] = new_name
            if new_email != "":
                parts[5] = new_email
            if new_contact != "":
                parts[6] = new_contact

            updated_lines.append(SEP.join(parts))
            updated = True
        else:
            updated_lines.append(line)

    if not updated:
        print("Admin record not found.")
        return

    write_lines(USERS_FILE, updated_lines)
    print("Profile updated successfully.")