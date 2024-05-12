class Etapa:

    def __init__(self, codigo, Nom, Porc):
        self.Codigo=int(codigo)
        self.Nombre = Nom
        self.Porcentaje=float(Porc)

    def get_Codigo(self):
        return int(self.Codigo)
    def set_Codigo(self,Cod):
        self.Codigo=int(Cod)

    def get_Nombre(self):
        return self.Nombre
    def set_Nombre(self,NomO):
        self.Nombre=NomO

    def get_Porcentaje(self):
        return float(self.Porcentaje)
    def set_Porcentaje(self,Porc):
        self.Porcentaje=float(Porc)