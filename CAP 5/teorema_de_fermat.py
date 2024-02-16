def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")



a = int(input("Informe 1 numero de 1 a 10: "))
b = int(input("Informe 1 numero de 1 a 10: "))
c = int(input("Informe 1 numero de 1 a 10: "))
n = int(input("Informe 1 numero de 1 a 10: "))

check_fermat(a, b, c, n)
