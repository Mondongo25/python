def invertir (a) :
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r
    c = ["a","l","o","h"]   

# PD
b = input ("Introdueix una palabra:") 
c = invertir(b)
print ("La palabra",b,"si la girem es", c)    

