#Funcion que regresa la longituda
def longitud (a):
    count=0
    for i in a:
        count+=1
    return count

#Programa principal
b=[1,"a", [3,4],5,6]
print(longitud(b))