from utils import ENROLL_FILE, PROGRAMS_FILE, PAYMENTS_FILE, SEP, read_lines, skip_line


def view_payment_status(trainee_id):
    print("\n=== VIEW PAYMENT STATUS ===")

    total_charges = 0.0
    total_paid = 0.0
    active_programs = []

    for line in read_lines(ENROLL_FILE):
        if skip_line(line):
            continue

        e = line.split(SEP)
        if len(e) >= 5 and e[1] == trainee_id and e[3] == "ACTIVE":
            active_programs.append(e[2])

    if not active_programs:
        print("No active enrollments found.")
        return

    for line in read_lines(PROGRAMS_FILE):
        if skip_line(line):
            continue

        p = line.split(SEP)
        if len(p) >= 5 and p[0] in active_programs:
            total_charges += float(p[2])

    for line in read_lines(PAYMENTS_FILE):
        if skip_line(line):
            continue

        pay = line.split(SEP)
        if len(pay) >= 6 and pay[1] == trainee_id:
            total_paid += float(pay[3])

    balance = total_charges - total_paid

    print(f"Total Charges : RM{total_charges:.2f}")
    print(f"Total Paid    : RM{total_paid:.2f}")
    print(f"Balance       : RM{balance:.2f}")

    if balance <= 0:
        print("Payment Status: FULLY PAID")
    else:
        print("Payment Status: PENDING BALANCE")