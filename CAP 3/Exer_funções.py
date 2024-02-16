#Apresentando conceitos de funções com "def"

import math

def right_justify(s):
    print((" " * 64) + s)
    
right_justify("monty")
################################################################################
def print_lirics(): #definindo uma função chamada print_lirics
    print("hellooo")
    print("abestado")
def repeat_lirics(): #definindo uma nova função chamada repeat que vai repetir
    print_lirics() # 2 vezes a "print_lirics"
    print_lirics()
repeat_lirics() #executa ou chama a função repeat_lirics sem a necessidade do print
################################################################################

def print_twice(bruce): #neste exemplo determinamos que precisaremos passar um
    print(bruce) #argumento dentro da função
    print(bruce)
print_twice('Spam') #argumentos exemplo
print_twice(42) #argumentos exemplo
print_twice(math.pi) #argumentos exemplo

def cat_twice(part1, part2): #nesse exemplo atribumos uma nova variavel chamada 
    cat = part1 + part2 #cat_twice e dentro dela passamos que cat = part1 e part2
    print_twice(cat) #com isso definimos que print_twice vai receber o argumento cat 

line1 = 'Bing tiddle ' 
line2 = 'tiddle bang.'
cat_twice(line1, line2) # o resultado aki sera a junção de line1 e line2 conforme definido em cat.


