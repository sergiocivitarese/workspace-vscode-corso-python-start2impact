#Verifica la presenza di vocali nella stringa di input
vocali = "aeiou"
carattere = input("Inserisci un carattere:").lower()
if(carattere in vocali):
    print("C'è una vocale!")
