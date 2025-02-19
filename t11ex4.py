def concatenar_listes(lista1, lista2, connector):
   return [a + connector + b for a, b in zip(lista1, lista2)]


print(concatenar_listes(['sub', 'supra'], ['campió', 'campiona'], '-'))