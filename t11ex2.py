from functools import reduce

def Passar_a_Numero(lista):
    return reduce(lambda n1, n2: str(n1)+str(n2), lista)

print(Passar_a_Numero([3, 4, 1, 5]))