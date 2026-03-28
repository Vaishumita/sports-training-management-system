import os

from receptionist.registeration import register_trainee
from receptionist.update_program import enroll_trainee_to_program
from receptionist.payment import accept_payment
from receptionist.delete_trainees import delete_trainee
from receptionist.profile import update_profile_receptionist

from admin.admin_menu import admin_menu

from coach.coach_menu import coach_menu
from trainee.trainee_menu import trainee_menu


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

USERS_FILE = os.path.join(DATA_DIR, "users.txt")

MAX_LOGIN = 3
SEP = "|"


def read_lines(path):
    if not os.path.exists(path):
        return []
    f = open(path, "r", encoding="utf-8")
    lines = f.read().splitlines()
    f.close()
    return lines


def login():
    attempts = 0
    while attempts < MAX_LOGIN:
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        lines = read_lines(USERS_FILE)
        for line in lines:
            # SKIP header or empty lines
            if line.startswith("#") or line.strip() == "":
                continue

            parts = line.split(SEP)

            if len(parts) < 5:
                continue

            # U001|admin|123|ADMIN|Admin User
            user_id = parts[0].strip()
            u = parts[1].strip()
            p = parts[2].strip()
            role = parts[3].strip()
            name = parts[4].strip()

            if username == u and password == p:
                print(f"\nWelcome {name} ({role})")
                return user_id, role, name

        attempts += 1
        print(f"Invalid login. Attempts left: {MAX_LOGIN - attempts}")

    print("\nToo many attempts. Exiting...")
    return None, None, None


def receptionist_menu(user_id):
    while True:
        print("\n--- RECEPTIONIST MENU ---")
        print("1. Register Trainee")
        print("2. Enroll Trainee to Program")
        print("3. Accept Payment + Receipt")
        print("4. Delete Trainee")
        print("5. Update My Profile")
        print("0. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            register_trainee()
        elif choice == "2":
            enroll_trainee_to_program()
        elif choice == "3":
            accept_payment(user_id)
        elif choice == "4":
            delete_trainee()
        elif choice == "5":
            update_profile_receptionist(user_id)
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        user_id, role, name = login()

        if role is None:
            break

        # menu routing
        if role == "ADMIN":
            admin_menu(user_id)
        elif role == "RECEPTIONIST":
            receptionist_menu(user_id)
        elif role == "COACH":
            coach_menu(user_id)
        elif role == "TRAINEE":
            trainee_menu(user_id)
        else:
            print("Unknown role!")


if __name__ == "__main__":
    main()