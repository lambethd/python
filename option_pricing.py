import present_value as pv
import interest_rate_service as ir
from nominal_tree import NominalTree
import numpy as np
#from scipy.stats import norm
import scipy

class OptionPricing:
    def __init__(self):
        self.pv = pv.PresentValue()
        self.ir = ir.InterestRateService()
        self.tree = NominalTree()
    
    def get_black_scholes_price(self, notional, strike_price, time_to_maturity, volatility, risk_free_rate):
        d1 = (np.log(notional / strike_price) + (risk_free_rate + 0.5 * volatility ** 2) * time_to_maturity) / (volatility * np.sqrt(time_to_maturity))
        d2 = d1 - volatility * np.sqrt(time_to_maturity)

        call_price = (notional * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2))

        return round(call_price, 2)
    
    def get_binomial_price(self, notional, strike_price, time_to_maturity, volatility):
        steps = int(time_to_maturity * 12)
        binomial_tree = self.tree.build_binomial_tree(steps)

        binomial_tree.value = strike_price
        binomial_tree.traverse_tree(lambda node: self.calc_node_values(node, volatility))
        self.tree.print_tree(binomial_tree)

    def calc_node_values(self, node, volatility):
        if node is not None and (node.value == 0 or node.value is None):
            parents = node.parents
            print("Working on " + str(node.id))
            up_parents = list(filter(lambda x: x.get_up_child() == node, parents))
            down_parents = list(filter(lambda x: x.get_down_child() == node, parents))
            up_value = 0
            down_value = 0
            if len(up_parents) == 1:
                up_parent = up_parents[0]
                up_value = up_parent.value * (1 + volatility)
            if len(down_parents) == 1:
                down_parent = down_parents[0]
                down_value = down_parent.value * (1 - volatility)

            if len(up_parents) == 1 and len(down_parents) == 1:
                node.value = (up_value + down_value ) / 2
            else:
                node.value = up_value + down_value

OptionPricing().get_binomial_price(100, 100, 1, 0.02)        