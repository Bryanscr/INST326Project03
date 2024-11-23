from Caregiver import Caregiver, CaregiverManager

# Test Caregiver class
def test_caregiver():
    caregiver1 = Caregiver("Annie", "123-456-7890", "annie@example.com", 22)
    caregiver2 = Caregiver("Chris", "987-654-3210", "chris@example.com", 24)

    caregiver1.set_available("Monday", "AM")
    caregiver1.set_available("Tuesday", "PM")
    caregiver2.set_available("Monday", "PM")
    caregiver2.set_unavailable("Tuesday", "AM")

    print(f"Caregiver: {caregiver1.name}, Phone: {caregiver1.phone}, Email: {caregiver1.email}, Pay Rate: ${caregiver1.pay_rate}/hr")
    print(f"Availability: {caregiver1.get_availability()}")

    print(f"Caregiver: {caregiver2.name}, Phone: {caregiver2.phone}, Email: {caregiver2.email}, Pay Rate: ${caregiver2.pay_rate}/hr")
    print(f"Availability: {caregiver2.get_availability()}")

# Test CaregiverManager class
def test_caregiver_manager():
    manager = CaregiverManager()
    caregiver1 = Caregiver("Annie", "123-456-7890", "alice@example.com", 22)
    caregiver2 = Caregiver("Chris", "987-654-3210", "bob@example.com", 24)
    manager.add_caregiver(caregiver1)
    manager.add_caregiver(caregiver2)

    manager.list_caregivers()

# Run tests
if __name__ == "__main__":
    print("Testing Caregiver Module:")
    test_caregiver()
    print("\nTesting Caregiver Manager:")
    test_caregiver_manager()