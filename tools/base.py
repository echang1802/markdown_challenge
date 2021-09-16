
from tools.price_man import price_man

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
