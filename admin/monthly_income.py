from utils import SEP, PAYMENTS_FILE, PROGRAMS_FILE, read_lines, skip_line

def list_programs():
    lines = read_lines(PROGRAMS_FILE)
    print("\n=== PROGRAM LIST ===")

    found = False
    print("-" * 78)
    print(f"{'Program ID':<12}{'Training Name':<24}{'Charges':<12}{'Schedule':<18}{'Coach ID':<10}")
    print("-" * 78)

    for line in lines:
        if skip_line(line):
            continue

        p = line.split(SEP)
        if len(p) < 5:
            continue

        found = True
        print(f"{p[0]:<12}{p[1]:<24}RM{p[2]:<10}{p[3]:<18}{p[4]:<10}")

    if not found:
        print("No programs found.")

    print("-" * 78)

def monthly_income_report():
    print("\n=== MONTHLY INCOME REPORT ===")
    list_programs()
    program_id = input("Enter Program ID (e.g., P001): ").strip()
    month = input("Enter Month (01-12): ").strip()
    year = input("Enter Year (e.g., 2026): ").strip()

    # payments format: R001|trainee_id|program_id|amount|YYYY-MM-DD HH:MM|received_by
    payments = read_lines(PAYMENTS_FILE)
    total = 0.0
    count = 0

    for line in payments:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) < 6:
            continue

        pid = parts[2]
        amt_str = parts[3]
        dt = parts[4]  # "2026-01-21 10:30"

        if pid != program_id:
            continue

        if len(dt) >= 7:
            pay_year = dt[0:4]
            pay_month = dt[5:7]
        else:
            continue

        if pay_year == year and pay_month == month:
            try:
                total += float(amt_str)
                count += 1
            except:
                pass

    print("\n--- REPORT RESULT ---")
    print(f"Program: {program_id}")
    print(f"Month/Year: {month}/{year}")
    print(f"No. of payments: {count}")
    print(f"Total Income: RM {total:.2f}")
