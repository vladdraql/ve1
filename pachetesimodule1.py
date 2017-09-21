from coffee.latte import concatenate_list
from fifi.fufu import greater_than


def main():
    gt = greater_than(4, 6)
    print('pachetesimodule1: {}'.format(gt))

    l1 = [5]
    l2 = [6, 7]

    print('pachetesimodule1: {}'.format(concatenate_list(l1, l2)))


if __name__ == '__main__':
    main()
