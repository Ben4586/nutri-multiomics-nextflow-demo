import random
import pandas as pd

class Microbe:
    def __init__(self):
        self.energy = 10

    def step(self):
        self.energy += random.random()
        self.energy -= 0.5

population = [Microbe() for _ in range(50)]

history = []

for t in range(20):
    avg_energy = sum(m.energy for m in population) / len(population)
    history.append(avg_energy)
    
    for m in population:
        m.step()

df = pd.DataFrame({"time": range(20), "avg_energy": history})
df.to_csv("abm_simulation.csv", index=False)