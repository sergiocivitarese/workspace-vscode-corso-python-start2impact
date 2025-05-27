parola =input("inserisci una parola: ")
def is_palindroma(parola):
    parola.lower()
    return parola == parola[::-1]

if(is_palindroma(parola)):
    print("La parola è palindroma")
else:
    print("La parola non è palindroma")