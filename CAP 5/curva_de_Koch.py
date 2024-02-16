import turtle

def koch(t, n):
    if n < 10: #definir que o tamanho n, não pode ser inferior a 10
        t.fd(n)
        return
    m = n/3 #ecomizar ter que colocar n/3 ao inves de m
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    for i in range(3): #definir que vai rodar o koch 3 vezes
        koch(t, n)
        t.rt(120) #definir que no final de cada loop ele vai parar virado a 120° a direita


bob = turtle.Turtle()

bob.pu() #definir onde a linha vai começar
bob.goto(-150, 90) #definir o position da tela
bob.pd() #definir onde a linha vai terminar

snowflake(bob, 30)#input do tamanho

turtle.mainloop()
