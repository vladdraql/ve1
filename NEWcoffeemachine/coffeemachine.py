from NEWcoffee.coffee import Coffee
from NEWcafelatte.cafelatte import CafeLatte


if __name__ == '__main__':
    cafea1 = Coffee(2, 2, 200)
    cafea1.prepare_coffee_time()
    print(f'aceasta cafea are cantitatea: {cafea1.prepare_coffee()}')

    cafea2 = CafeLatte(coffee_spoons=2, sugar_spoons=2, water=200, milk=200)
    cafea2.prepare_coffee_time()
    print(f'aceasta cafea are cantitatea: {cafea2.prepare_coffee()}')
