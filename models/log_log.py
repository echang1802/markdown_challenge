
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from tools.engine import base_engine
from tools.simulator import simulate

class log_log_model:

    def __init__(self):
        data = pd.read_csv("data/formated_data.csv")
        data.drop(columns = ["item"], inplace = True)
        data = data.apply(np.log)
        self.model = LinearRegression().fit(data.drop(columns = "Sales"), data.Sales)

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
        aux = pd.DataFrame({
            "Week" : engine.total_weeks - engine.remaining_weeks,
            "Qty" : engine.inventory(),
            "Price" : engine.price()
        }, index = {0})
        return np.power(self.model.predict(aux),2)
