class AvanceObra:
    
    def __init__(self, NObra, FechaAvan, NEtapa, PorcAvan):
        self.NombreObra = NObra
        self.Etapa=NEtapa
        self.FechaAvance=FechaAvan
        self.PorcentajeAvance=PorcAvan

    def get_NombreObra(self):
        return self.NombreObra
    def set_NombreObra(self,NomO):
        self.NombreObra=NomO

    def get_NombreEtapa(self):
        return self.Etapa
    def set_NombreObra(self,Etp):
        self.Etapa=Etp

    def get_PorcentajeAvance(self):
        return self.PorcentajeAvance
    def set_PorcentajeAvance(self,Pobra):
        self.PorcentajeAvance=Pobra

    def __str__(self):
        return f"{self.NombreObra} - {self.FechaAvance} - {self.Etapa} - {self.PorcentajeAvance}"
    
    def __repr__(self) -> str:
        return f"{self.NombreObra} - {self.FechaAvance} - {self.Etapa} - {self.PorcentajeAvance}"

