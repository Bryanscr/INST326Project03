from Caregiver import Caregiver, CaregiverManager
from schedule_code import generate_schedule
from Pay_class import Pay

def test_full_program():
    # Step 1: Create caregivers and add their availability
    caregiver_manager = CaregiverManager()
    caregiver1 = Caregiver("Annie", "123-456-7890", "annie@example.com", 20)
    caregiver2 = Caregiver("Chris", "987-654-3210", "chris@example.com", 25)
    caregiver3 = Caregiver("Emma", "234-567-8901", "emma@example.com", 20)
    caregiver4 = Caregiver("David", "345-678-9012", "david@example.com", 19)
    caregiver5 = Caregiver("Ella", "456-789-0123", "ella@example.com", 20)
    caregiver6 = Caregiver("Frank", "567-890-1234", "frank@example.com", 21)
    caregiver7 = Caregiver("Grace", "678-901-2345", "grace@example.com", 18)
    caregiver8 = Caregiver("Hannah", "789-012-3456", "hannah@example.com", 22)

    caregivers = [caregiver1, caregiver2, caregiver3, caregiver4, caregiver5, caregiver6, caregiver7, caregiver8]
    for caregiver in caregivers:
        caregiver_manager.add_caregiver(caregiver)

    caregiver1.set_available("Monday", "7:00AM - 1:00PM", "preferred")
    caregiver2.set_available("Monday", "1:00PM - 7:00PM", "available")
    caregiver3.set_available("Tuesday", "7:00AM - 1:00PM", "preferred")
    caregiver4.set_available("Tuesday", "1:00PM - 7:00PM", "available")
    caregiver5.set_available("Wednesday", "7:00AM - 1:00PM", "preferred")
    caregiver6.set_available("Wednesday", "1:00PM - 7:00PM", "available")
    caregiver7.set_available("Thursday", "7:00AM - 1:00PM", "preferred")
    caregiver8.set_available("Thursday", "1:00PM - 7:00PM", "available")

    # Step 2: Generate the schedule
    schedule = generate_schedule(caregivers, 2024, 11)

    print("\nGenerated Schedule:")
    for day, shifts in schedule.items():
        print(f"Day {day}:")
        for shift, caregiver in shifts.items():
            print(f"  {shift}: {caregiver}")

    # Step 3: Calculate pay and generate the report
    report = Pay.pay_report(caregivers)
    print("\n" + report)

    # Step 4: Save the report to a file
    Pay.save_report_to_file(report, "full_program_pay_report.txt")
    print("\nReport saved to full_program_pay_report.txt!")

# Run the test
if __name__ == "__main__":
    test_full_program()