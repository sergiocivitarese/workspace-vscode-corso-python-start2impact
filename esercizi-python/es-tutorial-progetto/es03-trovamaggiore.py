#trova il max valore nella lista
lista_numeri = [2,10,22,28,36,5,3]

max = 0
for x in lista_numeri:
    if(x > max):
        max = x;
        
print(f"MAX = {max}")