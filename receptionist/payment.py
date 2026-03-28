from utils import SEP, PAYMENTS_FILE, USERS_FILE, PROGRAMS_FILE, ENROLL_FILE, generate_new_id, read_lines, write_lines, now_str, skip_line

def accept_payment(receptionist_id):
    print("\n=== ACCEPT PAYMENT ===")
    trainee_id = input("Trainee ID (e.g., U004): ").strip()
    program_id = input("Program ID (e.g., P001): ").strip()
    amt_str = input("Amount Paid (e.g., 50): ").strip()

    # validate trainee
    trainee_found = False
    for line in read_lines(USERS_FILE):
        if skip_line(line):
            continue
        p = line.split(SEP)
        if len(p) >= 4 and p[0] == trainee_id and p[3] == "TRAINEE":
            trainee_found = True
            break

    if not trainee_found:
        print("Invalid trainee ID.")
        return

    # validate program
    program_found = False
    for line in read_lines(PROGRAMS_FILE):
        if skip_line(line):
            continue
        p = line.split(SEP)
        if len(p) >= 1 and p[0] == program_id:
            program_found = True
            break

    if not program_found:
        print("Invalid program ID.")
        return

    # check enrollment
    enrolled = False
    for line in read_lines(ENROLL_FILE):
        if skip_line(line):
            continue
        e = line.split(SEP)
        if len(e) >= 5 and e[1] == trainee_id and e[2] == program_id and e[3] == "ACTIVE":
            enrolled = True
            break

    if not enrolled:
        print("Trainee is not enrolled in this program.")
        return

    try:
        amt = float(amt_str)
        if amt <= 0:
            print("Amount must be greater than 0.")
            return
    except:
        print("Invalid amount.")
        return

    rid = generate_new_id("R", PAYMENTS_FILE)
    dt = now_str()
    line = SEP.join([rid, trainee_id, program_id, f"{amt:.2f}", dt, receptionist_id])

    lines = read_lines(PAYMENTS_FILE)
    lines.append(line)
    write_lines(PAYMENTS_FILE, lines)

    print("\nPayment accepted successfully!")
    print(f"Receipt ID : {rid}")
    print(f"Trainee ID : {trainee_id}")
    print(f"Program ID : {program_id}")
    print(f"Amount Paid: RM{amt:.2f}")
    print(f"Date/Time  : {dt}")