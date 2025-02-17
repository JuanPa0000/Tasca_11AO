def coincideixen(lista):
    resultat=0
    for index,num in enumerate(lista):
        if index==num:
            resultat+=1
    return resultat

print(coincideixen([0,2,3,3,4]))