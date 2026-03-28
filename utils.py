import os
from datetime import datetime

SEP = "|"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.txt")
PROGRAMS_FILE = os.path.join(DATA_DIR, "programs.txt")
ENROLL_FILE = os.path.join(DATA_DIR, "enrollment.txt")  
PAYMENTS_FILE = os.path.join(DATA_DIR, "payments.txt")
REQUESTS_FILE = os.path.join(DATA_DIR, "requests.txt")

MAX_LOGIN = 3

def read_lines(path):
    if not os.path.exists(path):
        return []
    f = open(path, "r", encoding="utf-8")
    lines = f.read().splitlines()
    f.close()
    return lines

def write_lines(path, lines):
    f = open(path, "w", encoding="utf-8")
    for line in lines:
        f.write(line + "\n")
    f.close()

def skip_line(line):
    return line.strip() == "" or line.startswith("#")

def generate_new_id(prefix, filename):
    lines = read_lines(filename)
    max_num = 0
    for line in lines:
        if skip_line(line):
            continue
        parts = line.split(SEP)
        if len(parts) == 0:
            continue
        if parts[0].startswith(prefix):
            num = parts[0].replace(prefix, "")
            if num.isdigit():
                n = int(num)
                if n > max_num:
                    max_num = n
    return prefix + str(max_num + 1).zfill(3)

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M")