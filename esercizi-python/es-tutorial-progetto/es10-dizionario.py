# Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante 
# la "frequenza di comparsa" di ciascun carattere componente la stringa.
str_input = input(" --> inserisci una tringa:")
def genera_dict(str_input):
    mappa = {}
    for carattere in str_input:
        if carattere in mappa:
            mappa[carattere] +=1
        else:
            mappa[carattere] = 1
    return mappa


print(genera_dict(str_input))