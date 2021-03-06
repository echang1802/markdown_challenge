
import pandas as pd
import numpy as np

from tools.engine import base_engine
from tools.simulator import simulate

class naive_model:

    def __init__(self):
        data = pd.read_csv("data/formated_data.csv")
        data = data.groupby("Price").Sales.mean()
        self.data = np.round(data,0)

    def execute(self, inventory, weeks, prices):
        best_execution = {"revenue": 0}
        engine = base_engine(inventory, weeks, prices)
        for sim in range(1000):
            execution = simulate(self, engine)
            if execution["revenue"] > best_execution["revenue"]:
                best_execution = execution
            engine.restart()
        return best_execution

    def predict(self, engine):
        return self.data[engine.price()]
