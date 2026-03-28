from datetime import datetime
from utils import REQUESTS_FILE, ENROLL_FILE, PROGRAMS_FILE, SEP, read_lines, write_lines, skip_line, generate_new_id


def send_request(trainee_id):
    print("\n=== SEND REQUEST TO CHANGE PROGRAM ===")

    active_program_id = None

    for line in read_lines(ENROLL_FILE):
        if skip_line(line):
            continue

        parts = [x.strip() for x in line.split(SEP)]
        if len(parts) >= 5 and parts[1] == trainee_id and parts[3].upper() == "ACTIVE":
            active_program_id = parts[2]
            break

    if active_program_id is None:
        print("You do not have any active program.")
        return

    print(f"Current Program ID: {active_program_id}")

    print("\nAvailable Programs:")
    for line in read_lines(PROGRAMS_FILE):
        if skip_line(line):
            continue

        p = [x.strip() for x in line.split(SEP)]
        if len(p) >= 5:
            print(f"{p[0]} - {p[1]} | RM{p[2]} | {p[3]}")

    new_program_id = input("Enter New Program ID: ").strip()

    if new_program_id == "":
        print("Program ID cannot be empty.")
        return

    if new_program_id == active_program_id:
        print("New program cannot be the same as current program.")
        return

    program_exists = False
    for line in read_lines(PROGRAMS_FILE):
        if skip_line(line):
            continue
        p = [x.strip() for x in line.split(SEP)]
        if len(p) >= 5 and p[0] == new_program_id:
            program_exists = True
            break

    if not program_exists:
        print("Program ID not found.")
        return

    request_id = generate_new_id("Q", REQUESTS_FILE)
    request_date = datetime.now().strftime("%Y-%m-%d")

    new_line = SEP.join([
        request_id,
        trainee_id,
        active_program_id,
        new_program_id,
        "PENDING",
        request_date
    ])

    lines = read_lines(REQUESTS_FILE)
    lines.append(new_line)
    write_lines(REQUESTS_FILE, lines)

    print(f"Request submitted successfully!")
    print(f"Your Request ID is: {request_id}")