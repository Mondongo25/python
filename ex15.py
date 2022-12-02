# Funcion de sumar elementos 
def sumarlista (a):
    sumatori=0 
    for x in a:
        sumatori += x
    return sumatori 

# Funcion de multiplicar elementos
def multiplicarlista (lista):
    multiplicado=1
    for x in lista: 
        multiplicado *= x
    return multiplicado 

# Programa principal
x = [1,3,4,5,9]
print("El Sumatori es: ",sumarlista(x))
print("La multiplicació dels elements de la llista és: ", multiplicarlista(x))
