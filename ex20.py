# Definir crear puntos
def crear_repetits(a,b):
    c = b*int(a)
    return c

def crear_punts(a):
    for e in a:
        c=crear_repetits(int(e),'.')
        print(c)

a = input("Escribe in lista numerica de elementos: ")
crear_punts(a)        