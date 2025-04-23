class PresentValue:
    def get_present_value(self, cash_flow, rate, time_period):
        monthly_rate = rate / 12 / 100
        return cash_flow / ((1 + monthly_rate) ** time_period)