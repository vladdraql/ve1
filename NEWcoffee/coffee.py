class Coffee:

    def __init__(self, coffee_spoons, sugar_spoons, water):
        self.coffee_spoons = coffee_spoons
        self.sugar_spoons = sugar_spoons
        self.water = water

    def prepare_coffee(self):
        cantitate_totala_cafea = self.coffee_spoons + self.sugar_spoons + self.water
        return cantitate_totala_cafea

    def prepare_coffee_time(self):
        time_to_prepare = 4*self.coffee_spoons + 2*self.sugar_spoons
        print(f'dureaza {time_to_prepare} secunde sa va preparam cafeaua, b0$$')