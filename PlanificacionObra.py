from Etapa import Etapa

ListOfEtapas=[]
ListOfPlanificacion=[]

class PlanificacionObra:
    
    def __init__(self, NObra="", NEtapa:Etapa=None, PorcObra=0):
        self.NombreObra = NObra
        self.Etapa=NEtapa
        self.PorcentajeObra=PorcObra
    

    def get_NombreObra(self):
        return self.NombreObra
    def set_NombreObra(self,NomO):
        self.NombreObra=NomO

    def get_NombreEtapa(self):
        return self.Etapa
    def set_NombreObra(self,Etp):
        self.Etapa=Etp

    def get_PorcentajeObra(self):
        return self.PorcentajeObra
    def set_PorcentajeObra(self,Pobra):
        self.PorcentajeObra=Pobra

    def __str__(self) -> str:
        return f"{self.NombreObra},{self.Etapa.get_Nombre()},{self.PorcentajeObra}"
    
    def Generar_Obra(NomO,ListEtapas=[]):
        
        ListPlanificacion=[]

        for etapa in ListEtapas:
            newObra=PlanificacionObra(NomO,etapa,0)
            ListPlanificacion.append(newObra)        

        return ListPlanificacion
        
        

