class Fruit:
    def __init__(self, name, color): #contructorul
        self.name = name
        self.color = color

    def _priv(self):
        print('this is private')

    def show(self):
        print(f'This fruit is {self.color} and is named {self.name}')
        self._priv()

    @staticmethod #eticheta
    def apb(a, b):
        return a + b


if __name__ == '__main__':
    plum = Fruit('plum', 'purple')
    apple = Fruit('apple', 'red')

    plum.show()
    apple.show()

    print(Fruit.apb(2, 4))

    print(plum.__dict__) #printuie constructorul lui plum in format de dictionar