from treasury_client import TreasuryClient 
class InterestRateService:
    def __init__(self):
        self.treasury_client = TreasuryClient()
    mock_interest_rates = [
        {"Date": "2025-01", "Rate": 5.50}
    ]
    interest_rate_cache = []

    def get_interest_rate(self, number_of_months_in_future):
        # return self.mock_interest_rates[number_of_months_in_future]["Rate"]
        return self.get_zero_coupon_based_rate(number_of_months_in_future)
    
    def get_zero_coupon_based_rate(self, number_of_months_in_future):
        if len(self.interest_rate_cache) == 0:
            self.interest_rate_cache = self.treasury_client.get_zero_coupon_bond_prices()
        matching_rate = next(
            (val for val in self.interest_rate_cache if val["Months"] == number_of_months_in_future),
            None
        )
        if matching_rate:
            return float(matching_rate["Value"])
        else:
            (lower_months, lower_rate), (upper_months, upper_rate) = self.find_closest_rates(number_of_months_in_future)
            return self.interpolate_between_rates(
                lower_months, upper_months, lower_rate, upper_rate, number_of_months_in_future
            )
        
    def find_closest_rates(self, target_months):
        lower_rate = None
        lower_months = None
        upper_rate = None
        upper_months = None

        for rate in self.interest_rate_cache:
            if rate["Months"] < target_months:
                if lower_months is None or rate["Months"] > lower_months:
                    lower_rate = rate["Value"]
                    lower_months = rate["Months"]
            elif rate["Months"] > target_months:
                if upper_months is None or rate["Months"] < upper_months:
                    upper_rate = rate["Value"]
                    upper_months = rate["Months"]

        return (lower_months, lower_rate), (upper_months, upper_rate)
    
    def interpolate_between_rates(self, months1, months2, rate1, rate2, target_months):
        if months1 == months2:
            return float(rate1)
        return float(rate1) + (float(rate2) - float(rate1)) * (target_months - months1) / (months2 - months1)
        
if __name__ == "__main__":
    interest_rate_service = InterestRateService()
    print(interest_rate_service.get_zero_coupon_based_rate(1))
    print(interest_rate_service.get_zero_coupon_based_rate(6))
    print(interest_rate_service.get_zero_coupon_based_rate(7))
    print(interest_rate_service.get_zero_coupon_based_rate(90))