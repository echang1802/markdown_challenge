
import pandas as pd
import numpy as np

from tools.engine import base_engine

class naive_model:

    def __init__(self):
        data = pd.read_csv("data/formated_data.csv")
        data = data.groupby("Price").Sales.mean()
        self.data = np.round(data,0)

    def execute(self, inventory, weeks, prices):
        best_execution = {"revenue": 0}
        engine = base_engine(inventory, weeks, prices)
        for sim in range(1000):
            execution = self.__simulate__(engine)
            if execution["revenue"] > best_execution["revenue"]:
                best_execution = execution
            engine.restart()
        return best_execution

    def __simulate__(self, engine):
        execution = {"prices": [], "sales" : []}
        for week in range(engine.total_weeks):
            down_price_prob = np.random.random()
            if down_price_prob > 0.99:
                engine.down_price(3)
            elif down_price_prob > 0.95:
                engine.down_price(2)
            elif down_price_prob > 0.8:
                engine.down_price(1)
            units_sold = self.data[engine.price()]
            execution["prices"].append(engine.price())
            execution["sales"].append(min(units_sold, engine.inventory()))
            engine.end_week(units_sold)
        execution["revenue"] = engine.revenue()
        return execution
