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
        if (y>z): # y>x and y 