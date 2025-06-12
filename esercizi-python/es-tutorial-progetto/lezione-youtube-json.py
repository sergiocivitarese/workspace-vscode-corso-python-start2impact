# vediamo come leggere del json che arriva da frontend in python
# vediamo anche come convertire da python in json
# vediamo come formattare e ordinare il json

# attenzione : il json arriva come stringa{} quindi noi dobbiamo ricreare quella situazione come prima cosa

import json

#ESEMPIO 1    passaggio da PYTHON ---> JSON

x = '{"nome": "Luca", "cognome": "Rossi", "eta": 25 }'
y = json.loads(x)

print(y)

print(type(y))   #verifichiamo che abbiamo trasformato la stringa in un dict che come struttura è molto simile al json

print(y["nome"])