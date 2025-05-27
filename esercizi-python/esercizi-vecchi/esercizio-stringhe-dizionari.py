stringa = input("Inserisci una stringa: ")
def conta_caratteri_string(stringa):
    dizionario =  {}
    contatore = 0
    for c in stringa:
        if c in dizionario:
            dizionario[c] += 1
        else:
            dizionario[c] = 1
    return dizionario


print("Risultato ES 4: ", conta_caratteri_string(stringa).items())