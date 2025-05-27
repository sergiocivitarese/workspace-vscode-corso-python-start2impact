#dictionary 
# collezzioni di dati ordinate, modificabili che non permettono duplicati
# un dizionario è una collezione di dati che contiene coppie chiave-valore
# i dizionari sono indicizzati tramite le chiavi
# le chiavi sono uniche
# i valori possono essere di qualsiasi tipo
#operazioni sui dizionari
#accedere agli elementi con [chiave], get(chiave), keys(), values(), items(),
#aggiungere elementi con [chiave] = valore, update({chiave: valore}), update({chiave: valore})
#rimuovere elementi con pop(chiave), popitem(), del dizionario, clear()
#copiare dizionario con copy(), dict(dizionario)


persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "anni": 25,
}

# prove di stampa
print(type(persona))
print(persona)

x = persona.keys()
y = persona.values()
print( "keys->", x)
print( "values->",y)

print("nome" in persona)