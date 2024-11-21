class Pay:
    @staticmethod
    def calculate_weekly_pay(caregiver):
        return caregiver.hours_worked * caregiver.pay_rate

    @staticmethod
    def pay_report(caregiver):
        total_weekly_pay = 0
        report_lines = []
        report_lines.append("Weekly Pay Report")

        for caregiver in caregivers:
            weekly_pay = Pay.calculate_weekly_pay(caregiver)
            total_weekly_pay += weekly_pay 
            report_lines.append(
                f"Name: {caregiver.name}, Hours Worked: {caregiver.hours_worked}, "
                f"Pay Rate: ${caregiver.pay_rate:.2f}/hr, Weekly Pay: ${weekly_pay:.2f}")

        report_lines.append(f"Total Weekly Pay for All Caregivers: ${total_weekly_pay:.2f}")
        return "\n".join(report_lines)

    @staticmethod
    def save_report_to_file(report, filename = "pay_report.txt"):
        with open(filename, "w") as file:
            file.write(report)

        