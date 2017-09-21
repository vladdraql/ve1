# def suma(a=1, b=2): #default values, daca nu se trimite niciun param, se iau val astea
#     return a + b

#comparam doua numere de la tst: daca nr1>=nr2, return true, daca nu, false
#cu acest output, daca este true, atunci cerem de la tst altul, daca e false il vom inlocui cu cel mai mare nr impar mai mic decat el

def citire(mesaj='Nr = '):
    a = int(input(mesaj))
    return a

# nu este clar ca functia citire returneaza un int
# era mai intuitiv daca scriai return int(a)

def compare(a, b):
    if a >= b:
        return True
    else:
        return False

def primul_impar(a):
    if a % 2 == 0:
        return a - 1
    else:
        return a - 2


if __name__ == '__main__':
    a = citire('a = ')
    b = citire('b = ')

    if compare(a, b):
        a = citire('inlocuim a cu: ')
    else:
        a = primul_impar(a)

    print(a, b)