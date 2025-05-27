# Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente.
# Il programma deve poi chiedere all'utente di inserire una lettera e mostrare 
# in output solo i colori nella lista che iniziano con quella lettera.

lista_colori = []
def inserisci_colori():
    colori = []
    i = 0
    while(i<10):
        colore  = input("inserisci un colore: ")
        if colore not in colori:
            colori.append(colore)
        i+=1
    return colori
        
lista_colori = inserisci_colori()
carattere = input("Inserisci una lettera:")

def cercaColori(carattere):
    print(f"ricerca colori che iniziano con {carattere}:\n")
    for colore in lista_colori:
        if colore.startswith(carattere):
            print(f" - {colore}\n")
            
cercaColori(carattere)