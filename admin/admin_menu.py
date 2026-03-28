from admin.coaches import register_coach, delete_coach, assign_coach_to_program
from admin.receptionist import register_receptionist, delete_receptionist
from admin.monthly_income import monthly_income_report
from admin.profile import update_profile_admin
from admin.request_management import view_all_requests, approve_reject_request, admin_system_summary

def admin_menu(admin_id):
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Register Coach")
        print("2. Delete Coach")
        print("3. Assign Coach to Program")
        print("4. Register Receptionist")
        print("5. Delete Receptionist")
        print("6. Monthly Income Report (by Program)")
        print("7. Update My Profile")
        print("8. View All Program Change Requests")
        print("9. Approve / Reject Request")
        print("10. View System Summary")
        print("0. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            register_coach()
        elif choice == "2":
            delete_coach()
        elif choice == "3":
            assign_coach_to_program()
        elif choice == "4":
            register_receptionist()
        elif choice == "5":
            delete_receptionist()
        elif choice == "6":
            monthly_income_report()
        elif choice == "7":
            update_profile_admin(admin_id)
        elif choice == "8":
            view_all_requests()
        elif choice == "9":
            approve_reject_request()
        elif choice == "10":
            admin_system_summary()
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")