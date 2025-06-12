# python non ha un suo tipo di DATA
# per lavorare con le date va importato il modulo apposito "datetime"

import datetime

x = datetime.datetime.now()
print(x)

# vediamo ora come creare una data partendo da una data predefinita

x = datetime.datetime(2012, 6, 13)
print(x)

#FORMATTAZIONE DELLA DATA con stringFormatTime ---> strftime()

x = datetime.datetime.now()
print(x.strftime("%B"))                 # %B = Month name, full version --> restituisce il nome intero del mese corrente


# se volessi la data gg/mm/yyyy con questo formato posso fare cosi
#print("gg/mm/yyyy")
print(x.strftime("%d/%m/%Y"))     #11/06/2025

#oppure
print(x.strftime("%A %d-%B %Y"))     #Mercoledì 11-Giugno 2025