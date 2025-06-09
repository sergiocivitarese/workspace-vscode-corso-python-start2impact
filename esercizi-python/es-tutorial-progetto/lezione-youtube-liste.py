#codice lezione da 6 ore Youtube corso Python

#OPERAZIONI DI INSERT E APPEND SU LISTE ---------------------------------------------------------
x = ["milano", "roma", "napoli", "venezia", "brescia"]
print(x)
x.append("bergamo")
print(x)
x.insert(1, "lugano")
print(x)

#extend è un append con una lista che già esiste
x2 = ["torino", "firenze"]
print(x2)
x.extend(x2)
print(x)



#ELIMINAZIONE VALORE DALLA LISTA -----------------------------------------------------------------
#remove, pop, del clear
x.remove("milano")
print("rimosso milano --> ", x)
x.pop()
print("operazione di POP ultimo elemento cancellato\n -->  ", x)

# del(lista) cancella tutta la lista dalla memoria
# clear(lista) rimuove tutti gli elementi dalla lista, ottenendo una lista vuota
# del(lista[1]) rimuove l'elemento in posizione 1
print("cancellazione elementi.. da x2")
x2.clear()
print(x2)
x2.append("nuovo")
print(x2)
#--------------------------------------------------------------------------------------------------

#ciclo for con l'utilizzo di range
citta = ['ancona', 'acitrezza', 'acicastello']
print("test ciclo for con range:")
for i in range(len(citta)):
    print( citta[i])


#ordinamento di una lista
print("ordinamento numerico..")
numeri = [4,6,8,2,1,4,3,5]
numeri.sort() #ordina  
print( numeri )

#RIFERIMENTI (puntatori in altri linguaggi)

#questo esempio mostra come modificando y vado a modificare anche x perchè sono legato al riferimento di x e non al valore
x = ["udine", "bari", "napoli"]
y = x    #y copia il riferimento di x
print (x)
y[0] = "montecatini"
print("stampo nuovamente e verifico che y è legata a x")
print (x)

#se voglio effettuare una copia distinta devo usare copy()
y = x.copy()
y[0] = 'udine'
print(y)
