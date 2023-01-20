#Calcular la diferencia simétrica entre 3 conjuntos:
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {0, 2, 7}
conjunto_3 = {2, 8, 10, 15}
a = conjunto_1 & conjunto_2 & conjunto_3
for i in a:
    print(i)
conjunto_1.discard(i)
conjunto_2.discard(i)
conjunto_3.discard(i)

print("La diferencia simétrica de los 3 conjuntos es:",(conjunto_1 | conjunto_2 | conjunto_3))