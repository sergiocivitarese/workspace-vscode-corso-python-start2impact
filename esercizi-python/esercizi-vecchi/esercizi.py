#ESERCIZIO 1

def indice_elemento(lista):
    risultato = []
    for i in range(len(lista)):
        risultato.append((lista[i], i))
    return risultato
print("Risultato ES 1: ")
print(indice_elemento([1, 10, 100, 1000]))

#------------------------------------------------------------
#ESERCIZIO 2

def conta_parole(parole):
    risultato = {}
    for parola in parole:
        if parola in risultato:
            risultato[parola] += 1
        else:
            risultato[parola] = 1
    return risultato

print("Risultato ES 2: ")
print(conta_parole(['anna', 'mario', 'luca', 'edo', 'luca', 'anna']))

#------------------------------------------------------------
#ESERCIZIO 3

def conta_num_pari(lista):
    num_pari = 0
    for num in lista:
        if(num % 2 == 0 ):
            num_pari += 1
    return num_pari

print("Risultato ES 3: ")
print("Numeri pari trovati = ",conta_num_pari([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#------------------------------------------------------------
#ESERCIZIO 4
def conta_carattere(stringa, carattere):
    contatore = 0
    for c in stringa:
        if c == carattere:
            contatore += 1
    return contatore

print("Risultato ES 4: ")
print(conta_carattere('sternocleidomastoideo', 'o'))

#------------------------------------------------------------
#ESERCIZIO 4

def multipli_di_tre(lista):
    risultato = []
    for num in lista:
        if(num % 3 == 0):
            risultato.append(num)
    return risultato 

print("Risultato ES 5: ")
print(multipli_di_tre([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))    
    