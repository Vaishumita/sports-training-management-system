from receptionist.registeration import register_trainee
from receptionist.update_program import enroll_trainee_to_program
from receptionist.payment import accept_payment
from receptionist.delete_trainees import delete_trainee
from receptionist.profile import update_profile_receptionist

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
            print("Invalid choice.")