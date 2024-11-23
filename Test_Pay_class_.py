from Caregiver import Caregiver
from Pay_class import Pay

def test_pay_module():
    # Create caregiver instances
    caregiver1 = Caregiver("Annie", "123-456-7890", "annie@example.com", 20)
    caregiver2 = Caregiver("Chris", "987-654-3210", "chris@example.com", 25)

    # Assign hours worked
    caregiver1.hours_worked = 30
    caregiver2.hours_worked = 40

    # Generate and display pay report
    caregivers = [caregiver1, caregiver2]
    report = Pay.pay_report(caregivers)
    print(report)

    # Save the report to a file
    Pay.save_report_to_file(report)

# Run the test
if __name__ == "__main__":
    test_pay_module()