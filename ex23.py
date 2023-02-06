def paraula_mes_llarga(a):
    b=list()
    i=0
    for e in a:
        b[i]=len(e)
        i+=1
    b.sort()
    return b[::-1]

x = ["Hola", "Adios", "Si", "Matematicas"]
e = list(paraula_mes_llarga(x))
print("La paraula mes llarga es: ", e[0]) 

        
