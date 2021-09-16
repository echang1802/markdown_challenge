
import numpy as np

def simulate(model, engine):
    execution = {"prices": [], "sales" : []}
    for week in range(engine.total_weeks):
        down_price_prob = np.random.random()
        if down_price_prob > 0.99:
            engine.down_price(3)
        elif down_price_prob > 0.95:
            engine.down_price(2)
        elif down_price_prob > 0.8:
            engine.down_price(1)
        units_sold = model.predict(engine)
        execution["prices"].append(engine.price())
        execution["sales"].append(min(units_sold, engine.inventory()))
        engine.end_week(units_sold)
    execution["revenue"] = engine.revenue()
    return execution
