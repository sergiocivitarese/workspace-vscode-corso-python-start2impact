############    TUPLE  ########################

x = ('milano', 'roma', 'napoli')
print(x)
y = ('milano' , True, 1)
print(y)

#vediamo ora come creare una tupla con un solo elemento
x = ('milano')  #non è una tupla ma una stringa di un solo elemento
print(type(x))  #stampa <class 'str'>

#la tupla con un solo elemento deve essere creata con una virgola alla fine
x = ('milano',)  #ora è una tupla
print(type(x))  #stampa <class 'tuple'>

print('-------------------')
#vediamo ora come creare una tupla con il costruttore tuple()
x = tuple(('milano', 'roma', 'napoli'))   #attenzione alla doppia parentesi è importante
print(x)  
#la tupla è immutabile, non possiamo modificare i suoi elementi
#x[0] = 'torino'  #questo darebbe errore perché le tuple sono immutabili

#esiste tuttavia un metodo che permette di modificare una tupla, ma non è consigliato
#trasformo la tupla in una lista, modifico la lista e poi riconverto in tupla
print(x[0])  #stampa 'milano'
lista_x = list(x) #trasformo la tupla in una lista
print(lista_x)  #stampa ['milano', 'roma', 'napoli']
lista_x[0] = 'torino'  #modifico la lista
print(lista_x)  #stampa ['torino', 'roma', 'napoli']
x = tuple(lista_x)  #riconverto in tupla
print(x)  

#------------------------------------------------------------------------------------
print('-------------------')
#manipolazione delle tuple, spacchettamento in più variabili

citta = ('milano', 'roma', 'napoli')
print(citta) 
(x, y, z) = citta  #spacchetto la tupla in tre variabili
print(x)  #stampa 'milano'
print(y)  #stampa 'roma'
print(z)  #stampa 'napoli'

print('-------------------')

#se la tupla ha più elementi delle variabili disponibili posso fare in questo modo:
# metto asterisco su *z che è l'ultima variabile in questo modo prendo tutti gli elementi rimanenti
# z diventa quindi una lista
citta = ('milano', 'roma', 'napoli', 'torino', 'bologna')
print(citta)
(x, y, *z) = citta  #spacchetto la tupla in due variabili e una lista
print(x)  #stampa 'milano'
print(y)  #stampa 'roma'
print(z)  #stampa ['napoli', 'torino', 'bologna']     

#UNIRE le tuple
print('-------------------')
lista_citta = ('milano', 'roma', 'napoli')  #creo una tupla con tre città
lista_citta2 = ('venezia', 'londra')        #creo una seconda tupla con due città

print("unione di due tuple")
y = lista_citta + lista_citta2  #unisco le due tuple creando una nuova lista che le contiene
print(y)  #stampa 