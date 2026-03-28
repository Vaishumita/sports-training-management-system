from utils import USERS_FILE, SEP, read_lines, write_lines, skip_line


def update_profile_trainee(trainee_id):
    print("\n=== UPDATE TRAINEE PROFILE ===")

    lines = read_lines(USERS_FILE)
    updated_lines = []
    found = False

    for line in lines:
        if skip_line(line):
            updated_lines.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 9 and parts[0] == trainee_id and parts[3] == "TRAINEE":
            found = True

            print(f"Current Name    : {parts[4]}")
            print(f"Current IC      : {parts[5]}")
            print(f"Current Email   : {parts[6]}")
            print(f"Current Contact : {parts[7]}")
            print(f"Current Address : {parts[8]}")

            new_name = input("Enter New Name (press Enter to keep current): ").strip()
            new_ic = input("Enter New IC (press Enter to keep current): ").strip()
            new_email = input("Enter New Email (press Enter to keep current): ").strip()
            new_contact = input("Enter New Contact (press Enter to keep current): ").strip()
            new_address = input("Enter New Address (press Enter to keep current): ").strip()

            if new_name == "":
                new_name = parts[4]
            if new_ic == "":
                new_ic = parts[5]
            if new_email == "":
                new_email = parts[6]
            if new_contact == "":
                new_contact = parts[7]
            if new_address == "":
                new_address = parts[8]

            new_line = SEP.join([
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                new_name,
                new_ic,
                new_email,
                new_contact,
                new_address
            ])
            updated_lines.append(new_line)
        else:
            updated_lines.append(line)

    if not found:
        print("Trainee profile not found.")
        return

    write_lines(USERS_FILE, updated_lines)
    print("Profile updated successfully.")