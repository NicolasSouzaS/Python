#Definindo funções em Python
#Para criar funções você deve usar o comando def(definition)
#Seguido do nome da função e o paratenses que pode ter ou não
#argumentos.
#Em Python, não é necessário definir o tipo de retorno
def soma(valores):
    x = 0
    for i in valores:
        x = x + i
    return x
def media(valores):
    x = 0
    for i in valores:
        x = x + i
    return x / len(valores)

def maior(valores):
    x = valores[0]
    for i in range(1,len(valores)):
        if(i > x):
            x = i
    return x

