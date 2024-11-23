class Pay:
    @staticmethod
    def calculate_weekly_pay(caregiver):
        # Calculate weekly pay for a caregiver
        return caregiver.hours_worked * caregiver.pay_rate

    @staticmethod
    def calculate_monthly_pay(caregiver):
        # Calculate monthly in a month
        return Pay.calculate_weekly_pay(caregiver) * 4

    @staticmethod
    def pay_report(caregivers):
        # Generate a weekly pay report for all caregivers
        total_weekly_pay = 0
        report_lines = []
        report_lines.append("Weekly Pay Report")

        for caregiver in caregivers:
            weekly_pay = Pay.calculate_weekly_pay(caregiver)
            total_weekly_pay += weekly_pay
            report_lines.append(
                f"Name: {caregiver.name}, Hours Worked: {caregiver.hours_worked}, "
                f"Pay Rate: ${caregiver.pay_rate:.2f}/hr, Weekly Pay: ${weekly_pay:.2f}"
            )

        report_lines.append(f"Total Weekly Pay for All Caregivers: ${total_weekly_pay:.2f}")
        return "\n".join(report_lines)

    @staticmethod
    def save_report_to_file(report, filename="pay_report.txt"):
        # Save the generated report to a file
        with open(filename, "w") as file:
            file.write(report)
        print(f"Report saved to {filename}")

        