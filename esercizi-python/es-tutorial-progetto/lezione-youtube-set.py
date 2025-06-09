# SET sono collezioni non ordinate di elementi unici, non permettono duplicati
# sono mutabili, ma non indicizzate
# accederemo agli elementi tramite un ciclo for o con l'operatore in
# possiamo unire due set con l'operatore |
# unisco le due tuple in una nuova tupla
#rimuovo elementi con remover pop(), clear(), aggiungo con add(), update()


# creazione di un set
x = {"milano", "roma", "napoli"}
print(type(x))
print(x)

#un set può contenere tipi diversi
#y = {"milano", 34, True}  

#stampa il set
for i in x:
    print(i)

#aggiungo un elemento
x.add("venezia")
print("dopo l'aggiunta di venezia")
print(x)

#update
y = {"udine", "torino","imola"}
x.update(y)
print(x)

#remove()  per utilizzarlo dobbiamo essere sicuri della rimozione perchè altrimenti si blocca e restituisce errore
#discard() rimuove l'elemento se c'è oppure passa avanti senza alcun tipo di problema
 
x.discard("udine")
# x.remove("udine")
print(x)

x.pop()
print(x)
x.pop()
print(x)

#union() crea un nuovo set a cui dobbiamo assegnare una variabile, in questo caso z
z = x.union(y)
print(z)

#se vogliamo lavorare con elementi dobbiamo usare intersection() che crea un set solo di elementi in comune
#se vogliamo far ritornare un nuovo set come z possiamo fare intersection_update() la differenza sta nell'update finale
#update() e union() sono simili perchè escludono elementi duplicati
#intersection() tiene conto dei duplicati

print("elementi in comune:")
#se voglio gli elementi in comune tra x e y ad esempio userò intersection_update()
print(x)
print(y)
h = x.intersection_update(y)
print(x)
print(y)