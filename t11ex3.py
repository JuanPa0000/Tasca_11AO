def comencen_per(lista, letra):
    return list(filter(lambda x: x[0]==letra, lista))

print(comencen_per(["maria","manta","peu","mà"],"p"))