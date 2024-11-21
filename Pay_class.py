class Pay:
    @staticmethod
    def calculate_weekly_pay(caregiver):
        return caregiver.hours_worked * caregiver.pay_rate