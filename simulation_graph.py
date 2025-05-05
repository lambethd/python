import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

class SimulationGraph:
    def __init__(self, simulations):
        self.simulations = simulations

    def plot_simulation(self, simulation_number='Average'):
        plt.figure(figsize=(10, 6))
        if simulation_number == 'Average':
            avg_values = np.mean([sim['Value'] for sim in self.simulations], axis=0)
            plt.plot(self.simulations[0]['Date'], avg_values, label='Average Simulation', color='green')
        else:
            sim = self.simulations[simulation_number]
            plt.plot(sim['Date'], sim['Value'], label=f'Simulation {simulation_number + 1}', color='blue')
        
        plt.title('Simulation Results')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid()
        plt.show()

    def display_dropdown(self):
        root = tk.Tk()
        root.title("Simulation Selector")

        options = ['Average'] + [f'Simulation {i + 1}' for i in range(len(self.simulations))]
        selected_option = tk.StringVar(value='Average')

        def on_select(event):
            value = selected_option.get()
            if value == 'Average':
                self.plot_simulation('Average')
            else:
                sim_number = int(value.split()[-1]) - 1
                self.plot_simulation(sim_number)

        dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
        dropdown.bind("<<ComboboxSelected>>", on_select)
        dropdown.pack(pady=20)

        root.mainloop()

if __name__ == "__main__":
    # Example data for multiple simulations
    num_simulations = 5
    simulations = []
    for i in range(num_simulations):
        data = {
            'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
            'Value': [i + (i * 0.1) + np.random.normal(0, 5) for i in range(100)]  # Example values with noise
        }
        simulations.append(pd.DataFrame(data))

    simulation_graph = SimulationGraph(simulations)
    simulation_graph.display_dropdown()