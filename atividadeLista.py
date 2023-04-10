lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for x in range(1,10):

    print("Primeira proposta: " + str(lista[x]))
print("##########################################")

for x in range(8,13):
    print("Segunda proposta: " + str(lista[x])) 
print("##########################################")


for x in lista:
    if(x % 2 == 0):
        print("Terceira proposta: "+ str(x))
print("##########################################")

for x in lista:
    if(x % 2 != 0):
        print("Quarta proposta:" +str(x))
print("##########################################")

for x in lista:
    if( x % 2 == 0  ):
        print("Proposta do mutiplos de 2: "+ str(x))
print("##########################################")

for x in lista:
    if( x % 3 == 0):
        print("Proposta do mutiplos de 3: "+ str(x))
print("##########################################")

for x in lista:
    if(x % 4 == 0):
        print("Proposta dos mutiplos 4: "+ str(x))
print("##########################################")

for x in range(15,-1,-1):
        print(lista[x])

    

        
        
        
    