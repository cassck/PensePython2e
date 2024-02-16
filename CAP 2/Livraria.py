import math

print(2+1) ; print(15-8) 
#o ; serve para finalizar o código anterior e se vc quiser por tudo em uma linha
# só é isso
r = 5
volume = (4/3*math.pi*r**3) #aki atribuimos math.pi para ter o valor de pi
print(round(volume, 1)) #utilizamos round para puxar somente uma casa decimal

################################################################################

capa_livro = 24.95 #preço do livro
desconto = 40/100 # desconto de 40%
desconto_da_livraria = capa_livro*desconto
preço_final = capa_livro - desconto_da_livraria
transporte_primeiro_exemplar = 3 #custo de envio do primeiro livro
transporte_add = 0.75 #custo de cada livro add
quantidade_de_copias = 60 #60 pois é o numero de copias solicitadas no exercicio
custo_de_transporte_add = 0.75 * (quantidade_de_copias - 1)
print(round((preço_final*quantidade_de_copias) + (transporte_primeiro_exemplar + custo_de_transporte_add),2))

