#creo un listino vuoto di dict di prodotti per il negozio
from numpy import integer
from zmq import NULL


listino_prodotti  = {
    "pane": 1.50,
    "latte": 0.99,
    "pasta": 1.20,
    "uova": 2.30,
    "formaggio": 3.75
}


def aggiungiProdotto():
    nome = input("inserisci nome prodotto: ")
    prezzo = float(input("inserisci prezzo: "))
    listino_prodotti[nome] = prezzo

def stampaListinoProdotti():
    print("------------------------------")
    print("LISTINO PRODOTTI:")
    for nome, prezzo in listino_prodotti.items():
        print(nome + " " + str(prezzo))
    print("------------------------------")


def aggiornaProdotto():
    nome_p = input("inserisci il nome del prodotto che desideri aggiornare: ")
    prezzo_p = float(input("inserisci il prezzo del nuovo prodotto: "))
    if(listino_prodotti.get(nome_p) == NULL):
        print("errore nessun prodotto presente con quel nome")
    else:
        listino_prodotti[nome_p] = prezzo_p
        input("prodotto aggiornato")

def calcolaCosto():
    prezzo_tot = 0.0
    lista_prod_acuistati = []
    input_string = input("inserisci i prodotti che vuoi acquistare:")
    nomi_prod_input = input_string.split()

    for n in nomi_prod_input:
        if(listino_prodotti.keys().__contains__(n)):
            lista_prod_acuistati.append(n)
            prezzo_tot += listino_prodotti[n]
                
    print("lista prodotti acquistati:")
    print(lista_prod_acuistati)
    print("prezzo totale = ", prezzo_tot)
    

def gestisciProdotti():
    operazione = "999"
    
    while(operazione != 0):
        print("Operazioni disponibili:")
        print("------------------------------------------------------------")
        print("digita [1] per aggiungere un nuovo prodotto")
        print("digita [2] per aggiornare un prodotto esistente")
        print("digita [3] per stampare il listino dei prodotti")
        print("digita [4] per calcolare il prezzo dei prodotti acquistati:")
        print("digita [0] per terminare:")
        print("------------------------------------------------------------")
        operazione = input("scegli operazione:")
        operazione = int(operazione)
        if(operazione == 1):
            aggiungiProdotto()
        elif(operazione == 2):
            aggiornaProdotto()
        elif(operazione == 3):
            stampaListinoProdotti()
        elif(operazione == 4):
            calcolaCosto()
        
stampaListinoProdotti()        
gestisciProdotti()