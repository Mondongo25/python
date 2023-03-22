def anho(a): 
    if a%4==0 and (a%400>0 or a%100==0):
        print("Es anho de transpaso")
    else:
        print("No es anho de transpaso")
#PP 
b=input("Introduce un anho: ")
anho(int(b))

