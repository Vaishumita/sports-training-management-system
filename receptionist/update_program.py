from utils import SEP, USERS_FILE, PROGRAMS_FILE, ENROLL_FILE, read_lines, write_lines, skip_line, generate_new_id
from datetime import datetime

def list_programs():
    lines = read_lines(PROGRAMS_FILE)
    print("\n=== AVAILABLE PROGRAMS ===")
    found = False
    for line in lines:
        if skip_line(line):
            continue
        p = line.split(SEP)
        if len(p) < 5:
            continue
        found = True
        print(f"{p[0]} - {p[1]} | RM{p[2]} | {p[3]} | Coach:{p[4]}")
    if not found:
        print("No programs found.")

def enroll_trainee_to_program():
    print("\n=== ENROLL TRAINEE TO PROGRAM ===")
    trainee_id = input("Enter Trainee ID (e.g., U004): ").strip()

    # validate trainee exists
    users = read_lines(USERS_FILE)
    trainee_ok = False
    for line in users:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 4 and parts[0] == trainee_id and parts[3] == "TRAINEE":
            trainee_ok = True
            break

    if not trainee_ok:
        print("Trainee ID not found.")
        return

    list_programs()
    program_id = input("Enter Program ID to enroll (e.g., P001): ").strip()

    # validate program exists
    programs = read_lines(PROGRAMS_FILE)
    program_ok = False
    for line in programs:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 1 and parts[0] == program_id:
            program_ok = True
            break

    if not program_ok:
        print("Program ID not found.")
        return

    enrollments = read_lines(ENROLL_FILE)

    # prevent duplicate ACTIVE enrollment
    for line in enrollments:
        if skip_line(line):
            continue
        e = line.split(SEP)
        if len(e) >= 5 and e[1] == trainee_id and e[2] == program_id and e[3] == "ACTIVE":
            print("Trainee already enrolled in this program.")
            return

    eid = generate_new_id("E", ENROLL_FILE)
    today = datetime.now().strftime("%Y-%m-%d")
    new_line = SEP.join([eid, trainee_id, program_id, "ACTIVE", today])
    enrollments.append(new_line)
    write_lines(ENROLL_FILE, enrollments)

    print(f"Enrolled successfully! Enrollment ID: {eid}")