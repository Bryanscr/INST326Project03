import calendar

def generate_schedule(caregivers, year, month):
    # Define shifts
    shifts = ["7:00AM - 1:00PM", "1:00PM - 7:00PM"]

    # Get the number of days in the specified month
    num_days = calendar.monthrange(year, month)[1]

    # Initialize the schedule dictionary
    schedule = {day: {shift: None for shift in shifts} for day in range(1, num_days + 1)}

    # Helper function to find the best caregiver for a shift
    def find_best_caregiver(day, shift):
        best_caregiver = None
        # Convert numeric day to day name 
        weekday = calendar.weekday(year, month, day)  # 0=Monday, 6=Sunday
        day_name = calendar.day_name[weekday]  # "Monday", "Tuesday", etc.

        for caregiver in caregivers:
            # Check if caregiver is available for this day and shift
            if day_name in caregiver.availability and shift in caregiver.availability[day_name]:
                status = caregiver.availability[day_name][shift]
                if status == "preferred":  # Prioritize "preferred" caregivers
                    if best_caregiver is None or caregiver.hours_worked < best_caregiver.hours_worked:
                        best_caregiver = caregiver
                elif status == "available":  # Consider "available" if no "preferred"
                    if best_caregiver is None or (
                        best_caregiver.availability[day_name][shift] != "preferred"
                        and caregiver.hours_worked < best_caregiver.hours_worked
                    ):
                        best_caregiver = caregiver
        return best_caregiver

    # Assign caregivers to each shift
    for day in range(1, num_days + 1):
        for shift in shifts:
            caregiver = find_best_caregiver(day, shift)
            if caregiver:
                schedule[day][shift] = caregiver.name
                caregiver.hours_worked += 6  # Each shift is 6 hours
                print(f"Assigned {caregiver.name} to Day {day}, Shift {shift}")
            else:
                print(f"No caregiver available for Day {day}, Shift {shift}")

    return schedule


def display_schedule_as_html(schedule, year, month):
    # Create the HTML structure
    html_schedule = f"""
    <html>
    <head>
        <title>Care Schedule for {calendar.month_name[month]} {year}</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            td {{
                height: 100px;
                vertical-align: top;
            }}
        </style>
    </head>
    <body>
        <h1>Care Schedule for {calendar.month_name[month]} {year}</h1>
        <table>
            <tr>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
                <th>Sun</th>
            </tr>
    """
    
    # Get the first weekday of the month and the total days
    first_weekday, num_days = calendar.monthrange(year, month)

    # Fill in the days of the month
    current_day = 1
    for week in range((num_days + first_weekday) // 7 + 1):
        html_schedule += "<tr>"
        for day in range(7):
            if (week == 0 and day < first_weekday) or current_day > num_days:
                html_schedule += "<td></td>"  # Empty cell for days outside the month
            else:
                # Add the day and the assigned shifts
                shifts_for_day = schedule.get(current_day, {})
                morning_shift = shifts_for_day.get("7:00AM - 1:00PM", "N/A")
                afternoon_shift = shifts_for_day.get("1:00PM - 7:00PM", "N/A")

                html_schedule += f"<td>{current_day}<br><b>AM:</b> {morning_shift}<br><b>PM:</b> {afternoon_shift}</td>"
                current_day += 1
        html_schedule += "</tr>"

    # Close the table and HTML
    html_schedule += """
        </table>
    </body>
    </html>
    """
    
    # Write the HTML content to a file
    with open(f"care_schedule_{year}_{month}.html", "w") as file:
        file.write(html_schedule)

    print(f"HTML care schedule for {calendar.month_name[month]} {year} generated successfully!")
