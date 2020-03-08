#se si cambia file, cambiare nome qui
nome_file = "1_victoria_lake.txt"

token = []
lista_uffici = []
riga = []

def unisci(mappa_terreno, lista_uffici):
    for element in lista_uffici:
        x = element[0] - 1
        y = element[1] - 1
        reward_point = element[2]
        mappa_terreno[x][y][1] = 1
        mappa_terreno[x][y][2] = reward_point


with open(nome_file) as mappa:
    linea = mappa.readline().strip()
    token = linea.split()
    larghezza = int(token[0])
    altezza = int(token[1])
    num_uffici_clienti = token[2]
    uffici_reply = token[3]
    mappa_terreno = []
    token = []
    linea = mappa.readline().strip()
    #lettura uffici
    while not("T" in linea or "H" in linea or "#" in linea or "~" in linea or "*" in linea or "+" in linea or "X" in linea or "_" in linea):
        token = linea.split()
        x = int(token[0])
        y = int(token[1])
        reward_point = int(token[2])
        token = []
        lista_uffici.append([x, y, reward_point])
        linea = mappa.readline().strip()
    #lettura terreno
    while linea != "":
        riga = []
        token = list(linea)
        for element in token:
            riga.append([element, 0, 0])
        mappa_terreno.append(riga)
        linea = mappa.readline().strip()
        token = []

unisci(mappa_terreno, lista_uffici)