import numpy as np
import simulation_graph as sg
import pandas as pd
class MonteCarlo:
    def __init__(self, num_samples):
        self.num_samples = num_samples
    def generate_samples(self, mean, std_dev):
        data = {
            'Date': pd.date_range(start='2024-01-01', periods=self.num_samples, freq='D'),
            'Value': [i + (i * 0.1) + np.random.normal(mean, std_dev) for i in range(self.num_samples)]  # Example values with noise
        }
        return data

if __name__ == "__main__":
    mc = MonteCarlo(num_samples=1000)
    scenario1 = mc.generate_samples(mean=0, std_dev=1)
    scenario2 = mc.generate_samples(mean=3, std_dev=1)
    simulation_graph = sg.SimulationGraph([scenario1, scenario2])
    simulation_graph.display_dropdown()
