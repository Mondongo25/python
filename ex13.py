def longitud(a):
    l = 0
    for i in a:
        l +=1
        return l

a = input ("introduiex una cadena")
b = longitud(a)
print("La longitud", a,"es", b)
c = list()
for a in range(10):
    x = input("Introdueix el seguent element de la llista")
    c.append(x)
d = longitud(c)
print("La longitud", c,"es", d)