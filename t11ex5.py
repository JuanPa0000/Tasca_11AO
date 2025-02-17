def diccionari(lista):
    resultat = {}
    for index, valor in enumerate(lista):
        resultat[valor] = index
    return resultat


print(diccionari(['casa', 'cotxe', 'cadira', 'taula']))
