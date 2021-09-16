
from tools.base import base_engine

class engine(base_engine):

    def __init__(self, model = "naive", base_inventory = 2000, total_weeks = 16, price_list = [100, 90, 80, 60]):
        self.__base_init__(base_inventory = 2000, total_weeks = 16, price_list = [100, 90, 80, 60])

        if model == "naive":
            from models.naive import naive_model
            self.__model__ = naive_model()
        if model == "log_log":
            from models.log_log import log_log_model
            self.__model__ = log_log_model()

    def predict(self):
        return self.__model__.execute(self._inventory, self.remaining_weeks, self._price.get_list())

    def stats(self):
        print("Price:", self.price())
        print("Unit sold:", self.last_period_unit_sold)
        print("Inventory:", self.inventory())
        print("Revenue:", self.revenue())
