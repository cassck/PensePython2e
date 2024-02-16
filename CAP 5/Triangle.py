def is_triangle(a, b, c):
    if a + b == c:
        print("yes,it is a triagle")
    else:
        print("No,is't not triagle")

number_one = int(input("Digite um numero de 0 a 10:"))
number_two = int(input("Digite um numero de 0 a 10:"))
number_three = int(input("Digite um numero de 0 a 10:"))

is_triangle(number_one, number_two, number_three)