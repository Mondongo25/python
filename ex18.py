# Definir funcion dos listas
def superposicio(a,b):
    n = 0 # Indica cuantos elementos hay en comun
    for e in a:
        n += b.count(e)
    if n>0:
        return [n, True]
    else:
        return [0, False]

# Programa principal
a = input("Introduce la primera lista de elementos de string, sin espacios: ")
b = input("Introduce la segunda lista de elementos de un string, sin espacios: ")
c,d = superposicio(a,b)
if (c==0):
    print("Las dos listas no tiene nada en comun")
else:
    print("Las listas tiene ", c, "elementos en comun")