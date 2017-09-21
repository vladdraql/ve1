from coffee.latte import concatenate_list as c_l
from fifi.fufu import greater_than as g_t

def main():
    l1 = [1, 7, 5]
    l2 = ['nu', 'dada', '666']
    print(c_l(l1, l2))
    if g_t(l1[1], l1[2]):
        print('Dap')
    else:
        print('Nop')

if __name__ == '__main__':
    main()