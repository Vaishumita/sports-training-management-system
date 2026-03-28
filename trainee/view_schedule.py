from utils import ENROLL_FILE, PROGRAMS_FILE, SEP, read_lines, skip_line


def view_schedule(trainee_id):
    print("\n=== VIEW TRAINING SCHEDULE ===")

    enrollments = read_lines(ENROLL_FILE)
    programs = read_lines(PROGRAMS_FILE)

    found = False

    for e_line in enrollments:
        if skip_line(e_line):
            continue

        e = e_line.split(SEP)

        if len(e) >= 5 and e[1] == trainee_id and e[3] == "ACTIVE":
            program_id = e[2]

            for p_line in programs:
                if skip_line(p_line):
                    continue

                p = p_line.split(SEP)

                if len(p) >= 5 and p[0] == program_id:
                    print(f"Program ID   : {p[0]}")
                    print(f"Program Name : {p[1]}")
                    print(f"Charges      : RM{p[2]}")
                    print(f"Schedule     : {p[3]}")
                    print(f"Coach ID     : {p[4]}")
                    print("-" * 30)
                    found = True

    if not found:
        print("No active training schedule found.")