from trainee.view_schedule import view_schedule
from trainee.request import send_request
from trainee.update_request import update_pending_request, delete_pending_request
from trainee.view_payments import view_payment_status
from trainee.profile import update_profile_trainee


def trainee_menu(user_id):
    while True:
        print("\n--- TRAINEE MENU ---")
        print("1. View Training Schedule")
        print("2. Send Request to Change Program")
        print("3. Update Pending Request")
        print("4. Delete Pending Request")
        print("5. View Payment Status and Balance")
        print("6. Update My Profile")
        print("0. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            view_schedule(user_id)
        elif choice == "2":
            send_request(user_id)
        elif choice == "3":
            update_pending_request(user_id)
        elif choice == "4":
            delete_pending_request(user_id)
        elif choice == "5":
            view_payment_status(user_id)
        elif choice == "6":
            update_profile_trainee(user_id)
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")