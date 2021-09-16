
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
        
