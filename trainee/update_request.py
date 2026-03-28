from datetime import datetime
from utils import REQUESTS_FILE, PROGRAMS_FILE, SEP, read_lines, write_lines, skip_line


def show_my_pending_requests(trainee_id):
    print("\n=== MY PENDING REQUESTS ===")
    found = False

    for line in read_lines(REQUESTS_FILE):
        if skip_line(line):
            continue

        parts = [x.strip() for x in line.split(SEP)]

        if len(parts) >= 6 and parts[1] == trainee_id and parts[4].upper() == "PENDING":
            print(f"Request ID   : {parts[0]}")
            print(f"Old Program  : {parts[2]}")
            print(f"New Program  : {parts[3]}")
            print(f"Status       : {parts[4]}")
            print(f"Request Date : {parts[5]}")
            print("-" * 30)
            found = True

    if not found:
        print("No pending requests found.")


def update_pending_request(trainee_id):
    print("\n=== UPDATE PENDING REQUEST ===")
    show_my_pending_requests(trainee_id)

    request_id = input("Enter Request ID to update: ").strip()
    lines = read_lines(REQUESTS_FILE)
    updated = False
    new_lines = []

    for line in lines:
        if skip_line(line):
            new_lines.append(line)
            continue

        parts = [x.strip() for x in line.split(SEP)]

        if len(parts) >= 6 and parts[0] == request_id and parts[1] == trainee_id and parts[4].upper() == "PENDING":
            new_program_id = input("Enter New Program ID: ").strip()

            if new_program_id == "":
                new_lines.append(line)
                continue

            exists = False
            for p_line in read_lines(PROGRAMS_FILE):
                if skip_line(p_line):
                    continue
                p = [x.strip() for x in p_line.split(SEP)]
                if len(p) >= 5 and p[0] == new_program_id:
                    exists = True
                    break

            if not exists:
                print("Program ID not found.")
                new_lines.append(line)
                continue

            new_date = datetime.now().strftime("%Y-%m-%d")
            new_lines.append(SEP.join([parts[0], parts[1], parts[2], new_program_id, "PENDING", new_date]))
            updated = True
        else:
            new_lines.append(line)

    if updated:
        write_lines(REQUESTS_FILE, new_lines)
        print("Request updated successfully.")
    else:
        print("Pending request not found.")


def delete_pending_request(trainee_id):
    print("\n=== DELETE PENDING REQUEST ===")
    show_my_pending_requests(trainee_id)

    request_id = input("Enter Request ID to delete: ").strip()
    lines = read_lines(REQUESTS_FILE)
    new_lines = []
    deleted = False

    for line in lines:
        if skip_line(line):
            new_lines.append(line)
            continue

        parts = [x.strip() for x in line.split(SEP)]

        if len(parts) >= 6 and parts[0] == request_id and parts[1] == trainee_id and parts[4].upper() == "PENDING":
            deleted = True
        else:
            new_lines.append(line)

    if deleted:
        write_lines(REQUESTS_FILE, new_lines)
        print("Pending request deleted successfully.")
    else:
        print("Pending request not found.")




        