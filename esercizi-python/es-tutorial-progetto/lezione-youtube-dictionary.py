#collezzioni di dati ordinate, modificabili che non permettono duplicati

#creazione dict
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

#stampo dict
print(persona)

#stampo chiavi
x = persona.keys()
print(x)

#stampo i valori 
y = persona.values()
print(y)

#genera delle tuple(chiave, valore)
z = persona.items()
print(z)

#oltre alle funzioni sopra citate se voglio verificare l'esistenza di una chiave in un dict posso fare così
print("nome" in persona)  # restituisce TRUE

#update e modifica di un valore
#versione1:    persona["nome"] = "marco"

persona.update({"nome": "anna"})
print("persona update: ",persona)

#AGGIUNGERE ELEMENTI 
#aggiunge una chiave "colore" e gli assegna il valore "blu"
persona["colore"] = "blu"
print(persona)



#RIMUOVERE ELEMENTI
persona.pop("nome")  #elimina la chiave nome e il contenuto del suo valore
persona.popitem()    #va a rimuovere l'ultimo item
persona.clear       #ritorna un dict vuoto


#del persona                 #cancella il dict
#del persona["nome"]         #cancella la chiave all'interno



#seconda opzione per ciclare è quella di usare persona.values() e 
#persona.keys() che restituisce l'insieme chiavi o valori e si puo stampare usando solo x senza parentesi

#ciclare le chiavi del dict
print(" ------- stampo chiavi del dict -----------")
for x in persona:
    print(x)  #prende la chiave e la stampa
    
    
#ciclare i valori del dict
print(" ------- stampo le valori del dict ------")
for x in persona:
    print(persona[x])  #prende il valore e lo stampa
 