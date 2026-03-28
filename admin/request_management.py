from utils import REQUESTS_FILE, ENROLL_FILE, PROGRAMS_FILE, USERS_FILE, PAYMENTS_FILE, SEP, read_lines, write_lines, skip_line


def view_all_requests():
    print("\n=== ALL PROGRAM CHANGE REQUESTS ===")

    lines = read_lines(REQUESTS_FILE)
    found = False

    for line in lines:
        if skip_line(line):
            continue

        parts = line.split(SEP)

        if len(parts) >= 6:
            print(f"Request ID   : {parts[0]}")
            print(f"Trainee ID   : {parts[1]}")
            print(f"Old Program  : {parts[2]}")
            print(f"New Program  : {parts[3]}")
            print(f"Status       : {parts[4]}")
            print(f"Request Date : {parts[5]}")
            print("-" * 35)
            found = True

    if not found:
        print("No requests found.")


def approve_reject_request():
    print("\n=== APPROVE / REJECT REQUEST ===")
    view_all_requests()

    request_id = input("Enter Request ID: ").strip()
    action = input("Enter action (APPROVE / REJECT): ").strip().upper()

    if request_id == "":
        print("Request ID cannot be empty.")
        return

    if action == "APPROVED":
        action = "APPROVE"
    elif action == "REJECTED":
        action = "REJECT"

    if action not in ["APPROVE", "REJECT"]:
        print("Invalid action.")
        return

    request_lines = read_lines(REQUESTS_FILE)
    updated_requests = []
    request_found = False
    trainee_id = ""
    old_program_id = ""
    new_program_id = ""

    for line in request_lines:
        if skip_line(line):
            updated_requests.append(line)
            continue

        parts = line.split(SEP)

        if len(parts) >= 6 and parts[0] == request_id and parts[4] == "PENDING":
            request_found = True
            trainee_id = parts[1]
            old_program_id = parts[2]
            new_program_id = parts[3]

            if action == "APPROVE":
                parts[4] = "APPROVED"
            else:
                parts[4] = "REJECTED"

            updated_requests.append(SEP.join(parts))
        else:
            updated_requests.append(line)

    if not request_found:
        print("Pending request not found.")
        return

    write_lines(REQUESTS_FILE, updated_requests)

    if action == "APPROVE":
        enroll_lines = read_lines(ENROLL_FILE)
        updated_enrollments = []

        for line in enroll_lines:
            if skip_line(line):
                updated_enrollments.append(line)
                continue

            e = line.split(SEP)

            if len(e) >= 5 and e[1] == trainee_id and e[2] == old_program_id and e[3] == "ACTIVE":
                e[3] = "CHANGED"
                updated_enrollments.append(SEP.join(e))
            else:
                updated_enrollments.append(line)

        new_enroll_id = generate_next_enroll_id(enroll_lines)
        new_enroll_line = SEP.join([new_enroll_id, trainee_id, new_program_id, "ACTIVE", get_today_date()])
        updated_enrollments.append(new_enroll_line)

        write_lines(ENROLL_FILE, updated_enrollments)
        print("Request approved and enrollment updated successfully.")
    else:
        print("Request rejected successfully.")


def generate_next_enroll_id(lines):
    max_num = 0
    for line in lines:
        if skip_line(line):
            continue

        parts = line.split(SEP)
        if len(parts) > 0 and parts[0].startswith("E"):
            num_part = parts[0][1:]
            if num_part.isdigit():
                num = int(num_part)
                if num > max_num:
                    max_num = num

    return "E" + str(max_num + 1).zfill(3)


def get_today_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def admin_system_summary():
    print("\n=== ADMIN SYSTEM SUMMARY ===")

    users = read_lines(USERS_FILE)
    programs = read_lines(PROGRAMS_FILE)
    payments = read_lines(PAYMENTS_FILE)
    requests = read_lines(REQUESTS_FILE)

    total_admin = 0
    total_receptionist = 0
    total_coach = 0
    total_trainee = 0
    total_programs = 0
    total_requests = 0
    total_pending_requests = 0
    total_income = 0.0

    for line in users:
        if skip_line(line):
            continue

        parts = line.split(SEP)
        if len(parts) >= 4:
            role = parts[3]
            if role == "ADMIN":
                total_admin += 1
            elif role == "RECEPTIONIST":
                total_receptionist += 1
            elif role == "COACH":
                total_coach += 1
            elif role == "TRAINEE":
                total_trainee += 1

    for line in programs:
        if skip_line(line):
            continue
        total_programs += 1

    for line in requests:
        if skip_line(line):
            continue

        parts = line.split(SEP)
        if len(parts) >= 6:
            total_requests += 1
            if parts[4] == "PENDING":
                total_pending_requests += 1

    for line in payments:
        if skip_line(line):
            continue

        parts = line.split(SEP)
        if len(parts) >= 6:
            try:
                total_income += float(parts[3])
            except:
                pass

    print(f"Total Admins            : {total_admin}")
    print(f"Total Receptionists     : {total_receptionist}")
    print(f"Total Coaches           : {total_coach}")
    print(f"Total Trainees          : {total_trainee}")
    print(f"Total Programs          : {total_programs}")
    print(f"Total Requests          : {total_requests}")
    print(f"Pending Requests        : {total_pending_requests}")
    print(f"Total Income Collected  : RM{total_income:.2f}")