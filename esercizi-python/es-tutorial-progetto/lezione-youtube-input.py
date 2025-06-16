#utilizzo in input dei valori da assegnare a un dict da linea di comando

persona = {
    "nome" : "Luca",
    "cognome": "Rossi",
    "eta" : 25
}

operazioni = ("aggiungere", "modificare", "eliminare")
def start():
    operazione = input("cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Aggiungi chiave:valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass
   
   
   
def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    #aggiungo una nuova persona
    persona[chiave] = valore
    print(persona)
    
        
while True:
    start()
    
    