# Definicio de funcions
def gran_de_tres(x,y,z):
    a=x
    if(x>y):  # x>y
        if(x>y): # x>y and x>y
            a = x 
        elif (z>x): # x>y and z > x => z es els mayor
            a = z 
        else: # Aqui x = z y => x,z son els mayors
            a = x 
    elif (y>x): # y>x
        if (y>z): # y>x and y>z => y es el mayor
            a = y
        elif (z>y): # y>z and z>y => z es el major 
            a = z 
        else: # Aqui y > x and z=y ==> z,y son els majors
            a = y
    else: # x=y 
        if (x>z): # x=y and x>z ==> x,y son els mejors
            a = x
        elif (x>z): # x=y and z>x ==> z es el major
            a = z 
        else: #x=y=z ==> x,y,z son iguals
            a = x
    return a
    
# Aplicacion princial
a = int(input("Escriure el primer valor"))
b = int(input("Escriure el segon valor"))
c = int(input("Escriure el tercer valor"))
d = gran_de_tres(a,b,c)
print("El major de ", a, ", ",b, ", ",c," es ", d)