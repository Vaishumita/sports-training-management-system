from utils import SEP, USERS_FILE, ENROLL_FILE, read_lines, write_lines, skip_line

def delete_trainee():
    print("\n=== DELETE TRAINEE ===")
    trainee_id = input("Enter Trainee ID to delete: ").strip()

    # check trainee exists
    users = read_lines(USERS_FILE)
    new_users = []
    found = False

    for line in users:
        if skip_line(line):
            new_users.append(line)
            continue

        parts = line.split(SEP)
        if len(parts) >= 4 and parts[0] == trainee_id and parts[3] == "TRAINEE":
            found = True
            continue

        new_users.append(line)

    if not found:
        print("Trainee not found.")
        return

    # remove trainee enrollments too
    enrollments = read_lines(ENROLL_FILE)
    new_enrollments = []

    for line in enrollments:
        if skip_line(line):
            new_enrollments.append(line)
            continue

        parts = line.split(SEP)
        if len(parts) >= 3 and parts[1] == trainee_id:
            continue

        new_enrollments.append(line)

    write_lines(USERS_FILE, new_users)
    write_lines(ENROLL_FILE, new_enrollments)

    print("Trainee deleted successfully.")