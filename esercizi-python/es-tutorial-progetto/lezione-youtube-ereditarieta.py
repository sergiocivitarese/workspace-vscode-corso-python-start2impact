#ereditarietà
from typing import Self
from colorama import init


class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("ciao sono " + self.nome)
        
# la classe Insegnante ESTENDE persona, ovvero deriva da persona e aggiunge delle funzionalità 
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)     #super è il costruttore della classe padre Persona()
        self.materia = materia
    
    #override del metodo saluta()
    def saluta(self):
        print("buongiorno sono " + self.nome + " " + self.cognome)
    
    def daiVoto(self):
        print("bravo un bel 8")


persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri", "Matematica")

#concetto di ereditarietà
persona1.saluta()
insegnante1.saluta()
insegnante1.daiVoto()

