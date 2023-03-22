def leer():
    L = [] 
    a = 'a'
    while a != ".":
        a = input("Pon el nombre: ")
        if a !='.':
            L.append(a)
    return L

def ncp(L,c):
    p = []
    x = 0
    for e in L:
        if e[0]==c:
            x += 1
            p.append(e)
    print("El numero de palabras que comienza {} son {} y son {} ".format(c,x,p))

#PP
o = leer()
x = input("introduce el caracter que deseas buscar: ")
ncp(x, o)