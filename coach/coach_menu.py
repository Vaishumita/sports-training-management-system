from coach.add_programs import add_program
from coach.program_details import update_program, delete_program
from coach.trainees_list import view_my_trainees
from coach.profile import update_profile_coach

def coach_menu(user_id):
    while True:
        print("\n--- COACH MENU ---")
        print(f"Logged in Coach ID: {user_id}")
        print("1. Add Training Program")
        print("2. Update Training Program")
        print("3. Delete Training Program")
        print("4. View Enrolled Trainees")
        print("5. Update My Profile")
        print("0. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_program(user_id)
        elif choice == "2":
            update_program(user_id)
        elif choice == "3":
            delete_program(user_id)
        elif choice == "4":
            view_my_trainees(user_id)
        elif choice == "5":
            update_profile_coach(user_id)
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")