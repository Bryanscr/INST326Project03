from schedule_code import generate_schedule, display_schedule_as_html
from Caregiver import Caregiver

def test_generate_schedule():
    # Create caregivers
    caregiver1 = Caregiver("Annie", "123-456-7890", "annie@example.com", 20)
    caregiver2 = Caregiver("Chris", "987-654-3210", "chris@example.com", 20)

    # Set caregiver availability
    for day in ["Monday", "Wednesday", "Friday"]:
        caregiver1.set_available(day, "7:00AM - 1:00PM", "preferred")
        caregiver1.set_available(day, "1:00PM - 7:00PM", "available")

    for day in ["Tuesday", "Thursday", "Saturday"]:
        caregiver2.set_available(day, "7:00AM - 1:00PM", "preferred")
        caregiver2.set_available(day, "1:00PM - 7:00PM", "available")

    # Add caregivers to the list
    caregivers = [caregiver1, caregiver2]

    # Generate the schedule for November 2024
    schedule = generate_schedule(caregivers, 2024, 11)

    # Print the generated schedule
    print("Generated Schedule:")
    for day, shifts in schedule.items():
        print(f"Day {day}:")
        for shift, caregiver in shifts.items():
            print(f"  {shift}: {caregiver}")

    # Generate the HTML schedule
    display_schedule_as_html(schedule, 2024, 11)
    print("\nHTML schedule generated successfully!")

# Run the test
if __name__ == "__main__":
    test_generate_schedule()