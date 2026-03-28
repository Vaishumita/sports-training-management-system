from utils import USERS_FILE, SEP, read_lines, write_lines, skip_line

def update_profile_coach(coach_id):
    print("\n=== UPDATE COACH PROFILE ===")

    lines = read_lines(USERS_FILE)
    updated_lines = []
    found = False

    for line in lines:
        if skip_line(line):
            updated_lines.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 7 and parts[0] == coach_id and parts[3] == "COACH":
            found = True
            print(f"Current Name   : {parts[4]}")
            print(f"Current Email  : {parts[5]}")
            print(f"Current Contact: {parts[6]}")

            new_name = input("Enter New Name: ").strip()
            new_email = input("Enter New Email: ").strip()
            new_contact = input("Enter New Contact: ").strip()

            if new_name == "":
                new_name = parts[4]
            if new_email == "":
                new_email = parts[5]
            if new_contact == "":
                new_contact = parts[6]

            new_line = SEP.join([
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                new_name,
                new_email,
                new_contact
            ])
            updated_lines.append(new_line)
        else:
            updated_lines.append(line)

    if not found:
        print("Coach profile not found.")
        return

    write_lines(USERS_FILE, updated_lines)
    print("Profile updated successfully.")