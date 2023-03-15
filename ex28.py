def leer():
	lista=[]
	a = 'a'
	while a!='.':
		a = input("Introduce un mumero: ")
		if a != '.':
			lista.append (int(a))
		return tuple(lista)
def mostrar_mayores_que(a,num):
	for e in a:
		if e > num:
			print(e)
#PP
x = leer()
i = input("Introduce el numero que quieres comparar: ")
mostrar_mayores_que(x,int(i))
