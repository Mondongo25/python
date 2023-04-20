import random
def calculem_n_aleatoris():
    b=[]
    for i in range(4):
        b.append(random.randint(0,9))
    
def llegir_n_usuari():   
    b=[]
    for i in range(4):
        b.append(int(input("Introduce un numero: ")))
    return b

def comparar(a,b):
    totoigual=0
    existeixen=0
    for i in range(4):
        if a[i]==b[i]:
            totoigual+=1
        elif b[i] in a:
            return totoigual,existeixen

a=calculem_n_aleatoris()
sortir = 0
while sortir!=1:
    b=llegir_n_usuari()
    x,y=comparar(a,b)
    if x == 4:
        print("Has acertat tots el numeros {} ".format(b))
    elif x<4 and y>0:
        print("Has encertat {} numeros i n'hi ha {} que son pero no son al seu lloc".format(x,y))
    elif x<y and y==0:
        print("")
    elif x==0 and y>0:
        print("")
    else:
        


a=calculem_n_aleatoris()
sortir = 0
while sortir!=1:
    b=llegir_n_usuari()
    if comparar(a,b)!=1:
            escriure_resultat(a,b)
    else:
        sortir = 1
    escriure_despedida()
