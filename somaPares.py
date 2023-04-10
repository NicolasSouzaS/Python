lista1 = [2,11,3,6,4,17,10]

lista2 = [1,3,6,12,20,8]

#Exibir os numeros pares de cada lista criada e somar
#os números mostrados que são pares
resultadoSomaX = 0
resultadoSomaY = 0
resultadoFinal = 0

for x in lista1:
    if(x % 2 == 0):
        print("Números pares da lista 1:"+ str(x))
        resultadoSomaX = x + resultadoSomaX
for y in lista2:
    if(y % 2 == 0):
        print("Numeros pares da lista 2:"+ str(y))
        resultadoSomaY = y + resultadoSomaY

resultadoFinal = resultadoSomaX + resultadoSomaY

print("Resultado final da soma das duas listas, utilizando numeros pares: "+ str(resultadoFinal))
