class InterestRateService:
    mock_interest_rates = [
        {"Date": "2025-01", "Rate": 5.50}
    ]

    def get_interest_rate(self, number_of_months_in_future):
        return self.mock_interest_rates[number_of_months_in_future]["Rate"]