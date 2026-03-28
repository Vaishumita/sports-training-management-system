from utils import PROGRAMS_FILE, SEP, read_lines, write_lines, skip_line


def show_my_programs(coach_id):
    lines = read_lines(PROGRAMS_FILE)
    found = False

    print("\n=== MY PROGRAMS ===")
    for line in lines:
        if skip_line(line):
            continue

        parts = line.split(SEP)
        if len(parts) >= 5 and parts[4] == coach_id:
            print(f"{parts[0]} - {parts[1]} | RM{parts[2]} | {parts[3]}")
            found = True

    if not found:
        print("You have no programs assigned.")


def update_program(coach_id):
    print("\n=== UPDATE TRAINING PROGRAM ===")
    show_my_programs(coach_id)

    program_id = input("Enter Program ID to update: ").strip().upper()

    if program_id == "":
        print("Program ID cannot be empty.")
        return

    lines = read_lines(PROGRAMS_FILE)
    updated_lines = []
    found = False

    for line in lines:
        if skip_line(line):
            updated_lines.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 5 and parts[0].upper() == program_id and parts[4] == coach_id:
            found = True

            print(f"\nCurrent Program Name: {parts[1]}")
            print(f"Current Charges     : RM{parts[2]}")
            print(f"Current Schedule    : {parts[3]}")

            new_name = input("Enter New Program Name (press Enter to keep current): ").strip()
            new_charges = input("Enter New Charges (press Enter to keep current): ").strip()
            new_schedule = input("Enter New Schedule (press Enter to keep current): ").strip()

            if new_name == "":
                new_name = parts[1]

            if new_charges == "":
                charge_value = float(parts[2])
            else:
                new_charges = new_charges.replace("RM", "").replace("rm", "").strip()
                try:
                    charge_value = float(new_charges)
                    if charge_value <= 0:
                        print("Charges must be greater than 0.")
                        return
                except:
                    print("Invalid charges.")
                    return

            if new_schedule == "":
                new_schedule = parts[3]

            new_line = SEP.join([
                parts[0],
                new_name,
                f"{charge_value:.2f}",
                new_schedule,
                coach_id
            ])
            updated_lines.append(new_line)
        else:
            updated_lines.append(line)

    if not found:
        print("Program not found or not assigned to you.")
        return

    write_lines(PROGRAMS_FILE, updated_lines)
    print("Program updated successfully.")


def delete_program(coach_id):
    print("\n=== DELETE TRAINING PROGRAM ===")
    show_my_programs(coach_id)

    program_id = input("Enter Program ID to delete: ").strip().upper()

    if program_id == "":
        print("Program ID cannot be empty.")
        return

    lines = read_lines(PROGRAMS_FILE)
    updated_lines = []
    found = False

    for line in lines:
        if skip_line(line):
            updated_lines.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 5 and parts[0].upper() == program_id and parts[4] == coach_id:
            found = True
            continue
        else:
            updated_lines.append(line)

    if not found:
        print("Program not found or not assigned to you.")
        return

    write_lines(PROGRAMS_FILE, updated_lines)
    print("Program deleted successfully.")