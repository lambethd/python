import present_value as pv
import interest_rate_service as ir

class IrsPricing:
    def __init__ (self):
        self.present_value_service = pv.PresentValue();
        self.interest_rate_service = ir.InterestRateService();

    def price_vanilla(self, notional, fixed_rate, time_to_maturity):
        fixed_cashflows = self.get_fixed_cashflows(notional, fixed_rate, time_to_maturity)
        floating_cashflows = self.get_floating_cashflows(notional, time_to_maturity)

        for i in range(len(fixed_cashflows)):
            fixed_cashflows[i] = round(self.present_value_service.get_present_value(fixed_cashflows[i], self.interest_rate_service.get_interest_rate(i + 1), i + 1), 2)
            floating_cashflows[i] = round(self.present_value_service.get_present_value(floating_cashflows[i], self.interest_rate_service.get_interest_rate(i + 1), i + 1), 2)

        total_fixed_pv = sum(fixed_cashflows)
        total_floating_pv = sum(floating_cashflows)

        return total_fixed_pv - total_floating_pv
        
    def price_fixed_fixed(self, notional, fixed_rate, fixed_rate1, time_to_maturity):
        fixed_cashflows = self.get_fixed_cashflows(notional, fixed_rate, time_to_maturity)
        fixed_cashflows_1 = self.get_fixed_cashflows(notional, fixed_rate1, time_to_maturity)

        for i in range(len(fixed_cashflows)):
            fixed_cashflows[i] = round(self.present_value_service.get_present_value(fixed_cashflows[i], self.interest_rate_service.get_interest_rate(i + 1), i + 1), 2)
            fixed_cashflows_1[i] = round(self.present_value_service.get_present_value(fixed_cashflows_1[i], self.interest_rate_service.get_interest_rate(i + 1), i + 1), 2)

        total_fixed_pv = sum(fixed_cashflows)
        total_fixed_pv_1 = sum(fixed_cashflows_1)

        return total_fixed_pv - total_fixed_pv_1
    
    def get_fixed_cashflows(self, notional, fixed_rate, time_to_maturity):
        cashflows = []
        for i in range (1, time_to_maturity + 1):
            cashflows.append(round(notional * fixed_rate / 100 / 12, 2))
        return cashflows
    
    def get_floating_cashflows(self, notional, time_to_maturity):
        cashflows = []
        for i in range(1, time_to_maturity + 1):
            cashflows.append(round(notional * self.interest_rate_service.get_interest_rate(i) / 100 / 12 , 2))
        return cashflows
    

irs_pricing_service = IrsPricing()
print(irs_pricing_service.price_vanilla(notional=1000000, fixed_rate=5.25, time_to_maturity=24))

print(irs_pricing_service.price_fixed_fixed(notional=1000000, fixed_rate=5.25, fixed_rate1=4.25, time_to_maturity=12))