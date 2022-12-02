# Dado un caracter que no regrese true si es vocal y si es falso si no es
def vocal(a):
    if a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U':
        return True
    else:
        return False

# Programa principal

a = input("Escribir un caracter: ")
print("La funcion nos indica si es vocal o caonsante",vocal(a))