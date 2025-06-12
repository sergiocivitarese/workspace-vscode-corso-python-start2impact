# Sintassi classi e oggetti
# istanza, costruttore e metodi
# proprietà degli oggetti
# il parametro self

#creazione dell'oggetto Persona
#def_init è il costruttore dell'oggetto e self è come il this di java
#in python il SELF va messo come PRIMO parametro in ogni funzione OBBLIGATORIAMENTE
class Persona:
    def __init__(self, nome, cognome):            
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("ciao sono " + self.nome)

#creo l'istanza di persona1 e persona2
persona1 = Persona("Luca", "Rossi")
persona2 = Persona("Marco", "Verdi")

#stampo i nomi
print(persona1.nome)
print(persona2.nome)

#chiamo una funzione dell'oggetto persona
persona1.saluta()
persona2.saluta()

#cambio il valore del nome 
persona2.nome = "Maria"
print("ho cambiato il nome:")
persona2.saluta()

#ELIMINAZIONE OGGETTO
del persona2
# persona2.saluta() genera eccezzione


#--------------------------------------------------------------