import requests

class TreasuryClient:
    date_conversions = [
        {"Tenor": "1 Mo", "Months": 1},
        {"Tenor": "1.5 Month", "Months": 1.5},
        {"Tenor": "2 Mo", "Months": 2},
        {"Tenor": "3 Mo", "Months": 3},
        {"Tenor": "4 Mo", "Months": 4},
        {"Tenor": "6 Mo", "Months": 6},
        {"Tenor": "1 Yr", "Months": 12},
        {"Tenor": "2 Yr", "Months": 24},
        {"Tenor": "3 Yr", "Months": 36},
        {"Tenor": "5 Yr", "Months": 60},
        {"Tenor": "7 Yr", "Months": 84},
        {"Tenor": "10 Yr", "Months": 120},
        {"Tenor": "20 Yr", "Months": 240},
        {"Tenor": "30 Yr", "Months": 360}
    ]

    def get_zero_coupon_bond_prices(self):
        url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202505?type=daily_treasury_yield_curve&field_tdr_date_value_month=202505&page&_format=csv"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content.decode('utf-8')
            lines = data.split('\n')
            headers = lines[0].split(',')
            prices = []
            most_recent_date = lines[2].split(',')
            for i in range(0, len(headers)):
                tenor = headers[i].strip().replace('"', '')
                conversion = next((item for item in self.date_conversions if item["Tenor"] == tenor), None)
                if conversion:
                    prices.append({"Months": conversion["Months"], "Value": most_recent_date[i]})
            return prices
        else:
            raise Exception("Failed to fetch data from Treasury API")

if __name__ == "__main__":
    print(TreasuryClient().get_zero_coupon_bond_prices())