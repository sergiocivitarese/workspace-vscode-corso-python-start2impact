import miomodulo as em

import platform                                 #è un modulo standard molto comune 
import math

#mormalmente per i nomi dei moduli si usano massimo un paio di lettere in questo caso possiamo modificare il nome
#inseriento un alias (parola chiave "as" )


#recupero il dict dal modulo e stampo il valore del nome
x = em.persona1["nome"]
em.saluta(x)

y = platform.system()      #restituisce il nome del sistema operativo che si sta utilizzando
print(y) 


z = math.floor(2.9)   #arrotonda per difetto portando il risultato da 2.9 --> 2
print(z)

#la funzione DIR permette di mandare a schermo tutte le funzioni di math
print(dir(math))


#se volessi importare solo una parte del modulo come faccio ?
#   [ from miomodulo import persona1 ]--> importa solo quella variabile 