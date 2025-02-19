def dividir(n1,n2):
   try:
       return n1/n2
   except ZeroDivisionError:
       return "Error, no es pot dividir per zero"


print(dividir(10,0))