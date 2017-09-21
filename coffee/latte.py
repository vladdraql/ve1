def concatenate_list(a, b):
    a.extend(b)
    return a


def main():
    l1 = [1, 2, 3]
    l2 = ['cucu', 76, 'i']

    nl = concatenate_list(l1, l2)
    print('latte: {}'.format(nl))


if __name__ == '__main__':
    main()
