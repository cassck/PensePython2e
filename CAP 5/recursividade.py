"""neste codigo apresentamos a função de recursividade, nele informamos o valor 
3 para "n", sendo assim como n não é == 0 inciamos o loop até que seja no primeiro
round s=3, 2 round s=2, 3 round s=1. não inicia o 4 round pq n == 0, esse loop
não aceita numeros negativos pois temos no else um n-1 oque ocasionaria se fosse
n = -1 e s = 0, n=-1 + -1 = -2, nunca chegariamos a 0 entrando em um loop eterno
    """

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)


recurse(3, 0)