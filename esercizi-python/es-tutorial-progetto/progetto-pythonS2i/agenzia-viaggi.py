#da fare dopo aver completato le parti teoriche
#obiettivo: Scrivi un codice in Python che permetta agli utenti di creare, 
# organizzare e gestire una collezione di elementi con caratteristiche specifiche.

# nome = nome identificativo del viaggio
# paese = luogo di destinazione del viaggio 
# attrazioni_turistiche = attività che si possono svolgere in quel luogo
# durata = numero di giorni del viaggio
# tipo = indentifica il tipo di viaggio come ad esempio viaggi di gruppo, viaggio di nozze, ecc...

#STRUTTURA DATI
from struct import pack
from matplotlib.pylab import f
from numpy import integer
from regex import F
from sqlalchemy import null
from zmq import NULL

risultato = []
filtri = {}
continua = True
lista_viaggi = [
    {
        "nome": "Scoperta del Rajasthan",
        "paese": "India",
        "attrazioni_turistiche": ["Jaipur", "Jodhpur", "Safari nel deserto del Thar"],
        "durata": 12,
        "tipo": "Viaggio di gruppo"
    },
    {
        "nome": "Avventura in Patagonia",
        "paese": "Argentina",
        "attrazioni_turistiche": ["El Calafate", "Ghiacciaio Perito Moreno", "Trekking nel Fitz Roy"],
        "durata": 14,
        "tipo": "Viaggio d'avventura"
    },
    {
        "nome": "Viaggio zen a Kyoto",
        "paese": "Giappone",
        "attrazioni_turistiche": ["Templi zen", "Foresta di bambù", "Cerimonia del tè"],
        "durata": 10,
        "tipo": "Viaggio culturale"
    },
    {
        "nome": "Relax tra le isole Gili",
        "paese": "Indonesia",
        "attrazioni_turistiche": ["Snorkeling", "Spiagge", "Corsi di yoga"],
        "durata": 7,
        "tipo": "Viaggio di nozze"
    },
    {
        "nome": "Meraviglie del Perù",
        "paese": "Perù",
        "attrazioni_turistiche": ["Machu Picchu", "Cusco", "Lago Titicaca"],
        "durata": 13,
        "tipo": "Viaggio di gruppo"
    },
    {
        "nome": "Esperienza andina in Bolivia",
        "paese": "Bolivia",
        "attrazioni_turistiche": ["Salar de Uyuni", "La Paz", "Lagune altiplaniche"],
        "durata": 11,
        "tipo": "Viaggio d'avventura"
    },
    {
        "nome": "Tesori della Cambogia",
        "paese": "Cambogia",
        "attrazioni_turistiche": ["Angkor Wat", "Tonlé Sap", "Phnom Penh"],
        "durata": 9,
        "tipo": "Viaggio culturale"
    },
    {
        "nome": "Viaggio romantico a Santorini",
        "paese": "Grecia",
        "attrazioni_turistiche": ["Oia", "Tramonti sul mare", "Crociera alle caldere"],
        "durata": 6,
        "tipo": "Viaggio di nozze"
    },
    {
        "nome": "Safari in Kenya",
        "paese": "Kenya",
        "attrazioni_turistiche": ["Masai Mara", "Lago Nakuru", "Villaggi locali"],
        "durata": 8,
        "tipo": "Viaggio d'avventura"
    },
    {
        "nome": "Tour delle città imperiali",
        "paese": "Marocco",
        "attrazioni_turistiche": ["Fès", "Marrakech", "Rabat"],
        "durata": 10,
        "tipo": "Viaggio culturale"
    },
    {
        "nome": "Famiglia in Thailandia",
        "paese": "Thailandia",
        "attrazioni_turistiche": ["Bangkok", "Ayutthaya", "Chiang Mai"],
        "durata": 10,
        "tipo": "Viaggio in famiglia"
    },
    {
        "nome": "Natura e cultura in Vietnam",
        "paese": "Vietnam",
        "attrazioni_turistiche": ["Baia di Ha Long", "Hanoi", "Hue"],
        "durata": 12,
        "tipo": "Viaggio di gruppo"
    },
    {
        "nome": "Scoperte gastronomiche in Messico",
        "paese": "Messico",
        "attrazioni_turistiche": ["Città del Messico", "Oaxaca", "Tulum"],
        "durata": 11,
        "tipo": "Viaggio culturale"
    },
    {
        "nome": "Avventura sulle Ande ecuadoriane",
        "paese": "Ecuador",
        "attrazioni_turistiche": ["Quito", "Cotopaxi", "Mercato di Otavalo"],
        "durata": 9,
        "tipo": "Viaggio d'avventura"
    },
    {
        "nome": "Viaggio rigenerante in Bali",
        "paese": "Indonesia",
        "attrazioni_turistiche": ["Ubud", "Templi indù", "Terapie ayurvediche"],
        "durata": 10,
        "tipo": "Viaggio rigenerativo"
    },
    {
        "nome": "Esplorazione del Nepal mistico",
        "paese": "Nepal",
        "attrazioni_turistiche": ["Kathmandu", "Pokhara", "Stupa di Swayambhunath"],
        "durata": 12,
        "tipo": "Viaggio spirituale"
    },
    {
        "nome": "Crociera tra le Galápagos",
        "paese": "Ecuador",
        "attrazioni_turistiche": ["Tartarughe giganti", "Isole vulcaniche", "Snorkeling"],
        "durata": 8,
        "tipo": "Viaggio naturalistico"
    },
    {
        "nome": "India spirituale e sostenibile",
        "paese": "India",
        "attrazioni_turistiche": ["Rishikesh", "Ashram", "Cerimonie sul Gange"],
        "durata": 15,
        "tipo": "Viaggio rigenerativo"
    },
    {
        "nome": "Tour familiare in Colombia",
        "paese": "Colombia",
        "attrazioni_turistiche": ["Cartagena", "Valle del Cocora", "Bogotá"],
        "durata": 10,
        "tipo": "Viaggio in famiglia"
    },
    {
        "nome": "Luna di miele in Costa Rica",
        "paese": "Costa Rica",
        "attrazioni_turistiche": ["Parco Manuel Antonio", "Foresta pluviale", "Relax sul Pacifico"],
        "durata": 9,
        "tipo": "Viaggio di nozze"
    }
]

#-------------------------------------------------------------------------------------------------

#stampa l'elenco dei viaggi disponibili
def mostraViaggi(lista_viaggi):
    print("VIAGGI:")
    for viaggio in lista_viaggi:
        print(f"nome: {viaggio['nome']}")
        print(f"paese: {viaggio['paese']}")
        attrazioni = ", ".join(viaggio['attrazioni_turistiche'])
        print(f"attrazioni_turistiche: {attrazioni}")
        print(f"durata: {viaggio['durata']} giorni")
        print(f"tipo: {viaggio['tipo']}")
        print("-"*30)
        

#aggiunta di un nuovo viaggio
def aggiungiViaggio():
    print(">> aggiunta di un nuovo viaggio >> ")
    nome_v = input("inserisci il nome: ")
    paese_v = input("inserisci il paese: ")
    attrazioni_input = input("inserisci le attrazioni_turistiche (separate da virgola): ")
    attrazioni_v = [attr.strip() for attr in attrazioni_input.split(',')]
    durata_v = int(input("inserisci durata(gg): "))
    tipo_v = input("inserisci il tipo: ")
    
    nuovo_viaggio = {
        "nome" : nome_v,
        "paese" : paese_v,
        "attrazioni_turistiche": attrazioni_v,
        "durata": durata_v,
        "tipo" : tipo_v
    }
    
    if nuovo_viaggio not in lista_viaggi:
        lista_viaggi.append(nuovo_viaggio)
        

#ricerca di un viaggio
def cercaViaggi(lista_viaggi):
    print("\n >> ricerca del viaggio: ")
    nome = input("ricerca per [nome] oppure (vuoto) per skippare il filtro: ") 
    paese = input("ricerca per [paese] oppure (vuoto) per skippare il filtro: ") 
    attrazioni = input("ricerca per [attrazzioni] separate da ',' oppure (vuoto) per skippare il filtro: ")
    attrazioni = [attrazioni.strip() for attr in attrazioni.split(',')] 
    durata = input("ricerca per [durata] oppure (vuoto) per skippare il filtro: ")
    if(durata != "" or durata != NULL):
        durata = int(durata)
    else:
        durata = "" 
        
    tipo = input("ricerca per [tipo] oppure (vuoto) per skippare il filtro: ")
    
    if paese:
        filtri["paese"] = paese
    if tipo:
        filtri["tipo"] = tipo
    if (durata!= "" or durata !=NULL):
        filtri["durata"] = durata
    
    
    risultato = viaggiFiltrati(**filtri)
    print(">> processo di ricerca terminato!")
    print("Viaggi che rientrano nelle tue richieste:\n\n")
    mostraViaggi(risultato)
    print("\n\n")
    



def viaggiFiltrati(**filtri):
    for viaggio in lista_viaggi:
        for chiave, valore in filtri.items():
            if (viaggio[chiave] == valore):
                risultato.append(viaggio)
    return risultato
                
        
#---------main------------------------------------------------------------
#CREO UN MENU PER GESTIRE LE OPERAZIONI DELL'UTENTE
while(continua):
    operazione = ""
    print("-"*30)
    print("### MENU PRINCIPALE ###")
    print("-"*30)
    print("## Scegli quale operazione eseguire ## ")
    print("[a] - mostra l'elenco dei viaggi disponibili")
    print("[b] - aggiungi un viaggio")
    print("[c] - cerca un viaggio inserendo dei filtri")
    print("[fine] - per terminare")
    operazione = input("inserisci scelta:")
    print("-"*30)
    if(operazione == "a"):
        mostraViaggi(lista_viaggi)
    elif(operazione == "b"):
        aggiungiViaggio()
    elif(operazione == "c"):
        cercaViaggi(lista_viaggi)
    elif(operazione == "fine"):
        continua = False
    else:
        break




