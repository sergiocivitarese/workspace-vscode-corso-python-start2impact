# vediamo come leggere del json che arriva da frontend in python
# vediamo anche come convertire da python in json
# vediamo come formattare e ordinare il json

# attenzione : il json arriva come stringa{} quindi noi dobbiamo ricreare quella situazione come prima cosa

import json

from zmq import proxy

#ESEMPIO 1    passaggio da PYTHON ---> JSON    trasformo da stringa json a dict 

x = '{"nome": "Luca", "cognome": "Rossi", "eta": 25 }'
y = json.loads(x)

print(y)

print(type(y))   #verifichiamo che abbiamo trasformato la stringa in un dict che come struttura è molto simile al json

print(y["nome"])

val = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

y = json.dumps(val)
print(y)
print(type(y))

#ESEMPIO 2     passaggio da JSON ---->  PYHON  trasformo da dict a stringa json

