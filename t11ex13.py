class animal:
    def __init__(self,especie,edat):
        self.especie=especie
        self.edat=edat

    def xerrar(self):
        pass

    def mourem(self):
        pass

    def quisoc(self):
        print(f"soc una espècie de {self.especie} i tinc una edat de {self.edat}")

class humà(animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom=nom

    def xerrar(self):
        print("Estic xerrat en català")

    def mourem(self):
        print("M'estic mourent amb els dos peus")

class fiet(humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares=pares

    def nompares(self):
        print(f"Els pares de {self.nom} són {self.pares[0]} i {self.pares[1]}")

    def mourem(self):
        print("Estic gatetjant")

    def xerrar(self):
        print("Gugugaga") 


class cavall(animal):
    def __init__(self, especie, edat):
        super().__init__(especie, edat)

    def xerrar(self):
        print("*relincho*")
    
    def mourem(self):
        print("Estic galopant")

class dofí(animal):
    def __init__(self, especie, edat):
        super().__init__(especie, edat)

    def xerrar(self):
        print("*silbidos*")

    def mourem(self):
        print("Estinc nadant")

class centaure(humà,cavall):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat, nom)

    def xerrar(self):
        print("Estic xerrant")

    def mourem(self):
        print("Estic galopant")

class abella(animal):
    def __init__(self, especie, edat):
        super().__init__(especie, edat)

    def xerrar(self):
        print("Bzzzzzz")

    def mourem(self):
        print("Estic volant")

    def picar(self):
        print("PII")

animales=[
    humà("humà",25,"David"),
    fiet("humà",8,"Pepito",["david","Maria"]),
    cavall("cavall",13),
    dofí("dofí",4),
    centaure("centaure",41,"Franco"),
    abella("abella",1)
]

for animal in animales:
    animal.xerrar()
    animal.mourem()
    animal.quisoc()
