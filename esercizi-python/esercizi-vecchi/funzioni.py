#FUNZIONI IN PYTHON
def addizione(a, b):
    risultato = a + b
    print("Questa è la funzione di addizione")
    print("Fornisce la somma di due numeri passati come parametri")
    print("Il risultato è: ", str(risultato))
    
addizione(5, 3)


#funzioni con parametri OPZIONALI

def laptop_nuovo(ram, cpu, antivirus=False):
    print("Il laptop ha", ram, "GB di RAM")
    print("Il laptop ha un processore", cpu)
    if (antivirus == True):
        print("Il laptop ha un antivirus installato")
    else:
        print("Il laptop non ha un antivirus installato")
        
        
print("\n------\n")        
    
laptop_nuovo("16GB", "i7")
print("\n------\n")
laptop_nuovo("8GB", "i5", True)