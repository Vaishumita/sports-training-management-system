from utils import PROGRAMS_FILE, SEP, read_lines, write_lines, generate_new_id

def add_program(coach_id):
    print("\n=== ADD TRAINING PROGRAM ===")
    program_name = input("Enter Program Name: ").strip()
    charges = input("Enter Charges (RM): ").strip()
    schedule = input("Enter Schedule: ").strip()

    if program_name == "" or charges == "" or schedule == "":
        print("All fields are required.")
        return

    try:
        charges = charges.replace("RM", "").replace("rm", "").strip()
        charge_value = float(charges)
        if charge_value <= 0:
            print("Charges must be greater than 0.")
            return
    except:
        print("Invalid charges.")
        return

    program_id = generate_new_id("P", PROGRAMS_FILE)

    new_line = SEP.join([
        program_id,
        program_name,
        f"{charge_value:.2f}",
        schedule,
        coach_id
    ])

    lines = read_lines(PROGRAMS_FILE)
    lines.append(new_line)
    write_lines(PROGRAMS_FILE, lines)

    print(f"Program added successfully! Program ID: {program_id}")