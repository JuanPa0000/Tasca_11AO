try:
   with open("fitxer.txt","r") as f:
       f.seek(0)
       print(f.read())
except:
   print("Error el fitxer no existeix")