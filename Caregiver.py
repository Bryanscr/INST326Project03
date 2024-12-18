# Solution - enter your code solution below

class Caregiver:
    def __init__(self, name, phone, email, pay_rate):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.availability = {}
        self.hours_worked = 0

    def set_available(self, day, shift, status = "available"):
        if day not in self.availability:
            self.availability[day] = {}
        self.availability[day][shift] = status

    def set_unavailable(self, day, shift):
        if day not in self.availability:
            self.availability[day] = {}
        self.availability[day][shift] = False

    def get_availability(self):
        return self.availability


class CaregiverManager:
    def __init__(self):
        self.caregivers = []

    def add_caregiver(self, caregiver):
        if not any(c.email == caregiver.email for c in self.caregivers):
            self.caregivers.append(caregiver)
        else:
            print(f"Caregiver with email {caregiver.email} already exists.")

    def list_caregivers(self):
        print("\nList of Caregivers:")
        if not self.caregivers:
            print("No caregivers added yet.")
            return
        for caregiver in self.caregivers:
            print(
                f"Name: {caregiver.name}, Phone: {caregiver.phone}, "
                f"Email: {caregiver.email}, Pay Rate: ${caregiver.pay_rate}/hr"
            )

    def display_availability(self):
        print("\nCaregiver Availability:")
        if not self.caregivers:
            print("No caregivers added yet.")
            return
        for caregiver in self.caregivers:
            print(f"\nAvailability for {caregiver.name}:")
            for day, shifts in caregiver.get_availability().items():
                formatted_shifts = ", ".join(
                    [f"{shift}: {'Available' if available else 'Unavailable'}" for shift, available in shifts.items()]
                )
                print(f"Day {day}: {formatted_shifts}")
