class BondPricing:
    #face_value is the par value of the bond
    #rate is the annual coupon rate, e.g. 4.25
    #coupon_frequency is how regular the payments are in months, e.g. 6 is semi-annual
    #time_to_maturity is the number of months to maturity
    #yield_to_maturity is the ytm of the bond

    #This assumes the bond's time to maturity is a whole number of months
    def price(self, face_value, rate, coupon_frequency, time_to_maturity, yield_to_maturity):
        period_multiplier = coupon_frequency / 12
        coupon_rate_per_period = period_multiplier * rate / 100
        number_of_coupon_payments = time_to_maturity / coupon_frequency
        interest_per_period = coupon_rate_per_period * face_value
        discount_rate_per_period = yield_to_maturity * period_multiplier / 100

        present_value_of_face = face_value / (1 + discount_rate_per_period) ** number_of_coupon_payments
        present_value_of_interest = 0
        for i in range(int(number_of_coupon_payments)):
            present_value_of_interest += interest_per_period / (1 + discount_rate_per_period) ** (i + 1)
        
        return round(present_value_of_face + present_value_of_interest, 2)
    
    def calc_ytm(self, face_value, discount_price, rate, coupon_frequency, time_to_maturity):
        previous_result = face_value * 1000 #Setting a large value so that its always replaced #TODO: Replace this with int.MAX or something
        current_ytm = 0
        for interval in range(0, 8):
            interval_amount = 10 ** -interval
            for step in range(0, 100):
                ytm_to_test = current_ytm + (interval_amount * step)
                result = self.price(face_value, rate, coupon_frequency, time_to_maturity, ytm_to_test)
                if result == discount_price:
                    return ytm_to_test
                if result < discount_price and discount_price < previous_result:
                    current_ytm = ytm_to_test - interval_amount
                    break
                previous_result = result
        if discount_price - result < previous_result - discount_price:
            return ytm_to_test
        else:
            return current_ytm
        
if __name__ == "__main__":
    # Example usage     
    bond_pricing = BondPricing()
    #print(bond_pricing.price(face_value= 100, rate = 5, coupon_frequency= 6, time_to_maturity= 36, yield_to_maturity = 6))
    print(bond_pricing.calc_ytm(face_value=100, discount_price=95.92, rate = 5,coupon_frequency=6, time_to_maturity=36))
