
class price_man:

    def __init__(self, price_list):
        self.prices = price_list

        self.actual = price_list[0]
        self.level = 0
        self.max_level = len(price_list) - 1

    def down(self, levels):
        if self.level + levels > self.max_level:
            return
        self.level += levels
        self.actual = self.prices[self.level]
        
    def get(self):
        return self.actual

    def restart(self):
        self.level = 0
        self.actual = self.prices[self.level]

    def get_list(self):
        return self.prices[self.level:]

class base_engine:

    def __init__(self, base_inventory = 2000, total_weeks = 16, price_list = [100, 90, 80, 60]):
        self.base_inventory = base_inventory
        self.total_weeks = total_weeks

        self._inventory = base_inventory
        self.remaining_weeks = total_weeks
        self._revenue = 0
        self._price = price_man(price_list)

    def end_week(self, units_sold):
        units_sold = min(units_sold, self._inventory)
        self.last_period_unit_sold = units_sold
        self._inventory -= units_sold
        self.remaining_weeks -= 1
        self._revenue += units_sold * self.price()

    def down_price(self, levels):
        self._price.down(levels)

    def restart(self):
        self._inventory = self.base_inventory
        self.remaining_weeks = self.total_weeks
        self._revenue = 0
        self._price.restart()

    def price(self):
        return self._price.get()

    def revenue(self):
        return self._revenue

    def inventory(self):
        return self._inventory

    __base_init__ = __init__

class engine(base_engine):

    def __init__(self, model = "naive", base_inventory = 2000, total_weeks = 16, price_list = [100, 90, 80, 60]):
        self.__base_init__(base_inventory = 2000, total_weeks = 16, price_list = [100, 90, 80, 60])

        if model == "naive":
            from models.naive import naive_model
            self.__model__ = naive_model()

    def predict(self):
        return self.__model__.execute(self._inventory, self.remaining_weeks, self._price.get_list())

    def stats(self):
        print("Price:", self.price())
        print("Unit sold:", self.last_period_unit_sold)
        print("Inventory:", self.inventory())
        print("Revenue:", self.revenue())
