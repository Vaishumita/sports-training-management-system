from utils import PROGRAMS_FILE, ENROLL_FILE, USERS_FILE, SEP, read_lines, skip_line

def view_my_trainees(coach_id):
    print("\n=== VIEW ENROLLED TRAINEES ===")

    my_programs = []
    for line in read_lines(PROGRAMS_FILE):
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 5 and parts[4] == coach_id:
            my_programs.append((parts[0], parts[1]))  # (program_id, program_name)

    if not my_programs:
        print("You have no programs assigned.")
        return

    enrollments = []
    for line in read_lines(ENROLL_FILE):
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) >= 5 and parts[2] in [p[0] for p in my_programs] and parts[3] == "ACTIVE":
            enrollments.append(parts)

    if not enrollments:
        print("No trainees enrolled in your programs.")
        return

    users = read_lines(USERS_FILE)

    for program_id, program_name in my_programs:
        print(f"\nProgram: {program_name} ({program_id})")
        found = False

        for e in enrollments:
            if e[2] == program_id:
                trainee_id = e[1]

                for user_line in users:
                    if skip_line(user_line):
                        continue
                    u = user_line.split(SEP)
                    if len(u) >= 5 and u[0] == trainee_id and u[3] == "TRAINEE":
                        print(f"- {u[0]} | {u[4]}")
                        found = True
                        break

        if not found:
            print("No trainees in this program.")