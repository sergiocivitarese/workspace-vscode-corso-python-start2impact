# simula una calcolatrice

print("CALCOLATRICE..\n")
n1 = int(input("Inserisci n1:"))
operazione = input("Inserisci operazione:")
n2 = int(input("Inserisci n2:"))

def calcolatrice(n1, operazione, n2):
    res = 0
    if(operazione == '+'):
        res = n1 + n2
    elif (operazione == '-'):
        res = n1 - n2
    elif (operazione == '/'):
        res = n1 / n2
    elif (operazione == '*'):
        res = n1 * n2
    return print("Risultato = ", res)

calcolatrice(n1, operazione, n2)