def mdc(a, b):
    # Caso-base: se b for zero, o MDC é a
    if b == 0:
        return a
    # Chamada recursiva com os argumentos trocados (b, a % b)
    else:
        return mdc(b, a % b)

# Exemplos de uso:
print(mdc(48, 18))  # Saída: 6, pois 6 é o maior divisor comum de 48 e 18
print(mdc(35, 14))  # Saída: 7, pois 7 é o maior divisor comum de 35 e 14
print(mdc(1071, 462))  # Saída: 21, pois 21 é o maior divisor comum de 1071 e 462
