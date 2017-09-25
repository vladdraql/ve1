from NEWcoffee.coffee import Coffee


class CafeLatte(Coffee):

    def __init__(self, coffee_spoons, sugar_spoons, water, milk):
        super().__init__(coffee_spoons=coffee_spoons, sugar_spoons=sugar_spoons, water=water)
        self.milk = milk

    def prepare_coffee(self):
        cantitate_totala_cafelate = super().prepare_coffee() + self.milk
        return cantitate_totala_cafelate

    def prepare_coffee_time(self):
        time_to_prepare = 4 * self.coffee_spoons + 2 * self.sugar_spoons + self.milk/100
        print(f'dureaza {int(time_to_prepare)} secunde sa va preparam cafeaua, b0$$')
