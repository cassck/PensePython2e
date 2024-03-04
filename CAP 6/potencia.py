def is_power(a, b):
    if a == b:
        return True
    elif a < b:
        return False
    elif a % b == 0 and is_power(a // b, b):
        return True
    else:
        return False

# Exemplos de uso:
print(is_power(8, 2))  # True, pois 8 é 2^3
print(is_power(27, 3))  # True, pois 27 é 3^3
print(is_power(5, 2))  # False, pois 5 não é uma potência de 2
