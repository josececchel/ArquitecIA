
from PlanificacionObra import PlanificacionObra
from AvanceObra import AvanceObra
from Etapa import Etapa
from os import system
import qrcode
from PIL import Image

ListOfPlanificacion=[]
ListOfAvance=[]
ListOfEtapas=[]

# Validaciones de input
def validarEntrada(mensaje="", esNumerico=False):
    entradaValida = 0
    entrada = ""
    while entradaValida == 0:
        try:
            entrada = input(mensaje)
            if esNumerico and entrada.isnumeric():
                # Un float sigue siendo un numero (Engloba al int)
                entrada = float(entrada)
                entradaValida = 1
            elif esNumerico and not entrada.isnumeric():
                print("La entrada es incorrecta")
            elif not esNumerico:
                entradaValida = 1
        except:
            print("Ocurrio algo")
    return entrada

# Carga en memoria lista de Etapas
def CargarArchivo_Etapas():
    try:
        with open("Etapa.txt","r")as file:
            for linea in file.readlines():
                infoetapa=linea.strip().split(",")
                codigo,nombre,porcentaje=infoetapa #formato de como va a estar eln el archivo
                #creo el objeto
                mi_etapa = Etapa(int(codigo),nombre,porcentaje)
                ListOfEtapas.append(mi_etapa)        
    except:
        print("Error al cargar las etapas")
    
# Carga en memoria lista de Planifacacion de Obra
def CargarArchivo_PlanificacionObra():    
    try:
        with open("PlanificacionObra.txt","r")as file:
            for linea in file.readlines():
                infoplanificacion=linea.strip().split(",")
                nombre,etapa,porcentaje=infoplanificacion #formato de como va a estar eln el archivo
                mi_etapa= Recuperar_Etapa_porNombre(etapa)
                #creo el objeto
                mi_planificacion = PlanificacionObra(nombre,mi_etapa,porcentaje)
                ListOfPlanificacion.append(mi_planificacion)
    except:
        print("Error al cargar las planificaciones")

# Actualiza archivo con  lista de Planifacacion de Obra
def ActualizarArchivo_PlanificacionObra():
    try:
        with open("PlanificacionObra.txt","w") as file:
            for obra in ListOfPlanificacion:
                infoplanificacion=f"{obra.NombreObra},{obra.Etapa.get_Nombre()},{obra.PorcentajeObra}\n"
                file.write(infoplanificacion)
        # UNA VEZ ACTUALIZO EL ARCHIVO VUELVE A CARGA EN MEMORA LA LISTA DE OBRAS    
        CargarArchivo_PlanificacionObra()
    except:
        print("Error al actualizar las planificaciones de obra")

# Actualiza archivo con  lista de Avances de Obra
def ActualizarArchivo_AvancesObra():
    try:
        with open("AvanceObra.txt","w") as file:
            for obra in ListOfAvance:
                infoavance=f"{obra.NombreObra},{obra.FechaAvance},{obra.Etapa},{obra.PorcentajeAvance}\n"            
                file.write(infoavance)

        # UNA VEZ ACTUALIZO EL ARCHIVO VUELVE A CARGA EN MEMORA LA LISTA DE AVANCES
        CargarArchivo_AvanceObra()
    except:
        print("Error al registrar el avance de la obra.")

# Carga en memoria Avances de Obras
def CargarArchivo_AvanceObra():
    try:
        ListOfAvance.clear()
        with open("AvanceObra.txt","r")as file:
            for linea in file.readlines():
                infoavance=linea.strip().split(",")
                nombre,fecha,etapa,porcentaje=infoavance #formato de como va a estar eln el archivo
                #creo el objeto
                mi_avance = AvanceObra(nombre,fecha,etapa,porcentaje)

                ListOfAvance.append(mi_avance)
    except:
        print("Error al cargar los avances de obra.")


def Imprimir_TituloPantalla():
    system("cls") # LIMPIA PANTALLA
    print(">>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<< ARQUITECT IA >>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<")
    print("  ")

def Existe_Obra(unaObra):
    for obra in ListOfPlanificacion:
        if obra.NombreObra==unaObra:            
            return True
        
    return False

def Cargar_NuevaObra():
    Imprimir_TituloPantalla()    
    
    print("SUBMENU << NUEVA OBRA >>")
    NombreObra=validarEntrada("Ingrese el Nombre de Obra: ")
    if Existe_Obra(NombreObra)==False:
        # GENERA UNA NUEVA OBRA SI NO EXISTE
        newObra = PlanificacionObra
        ListNuevaObra=[]
        ListNuevaObra = newObra.Generar_Obra(NombreObra,ListOfEtapas)
        # CARGA EN LISTA DE OBRAS, LA NUEVA OBRA CREADA
        for item in ListNuevaObra:
            ListOfPlanificacion.append(item)

        ActualizarArchivo_PlanificacionObra()
    else:
        print("<< YA EXISTE UNA OBRA CON EL NOMBRE INGRESADO >>")

    print("  ")
    seguir=validarEntrada("PRESION (V) PARA VOLVER AL MENU PRINCIPAL.")


# RECUPERA UNA ETAPA SEGUN UN CODIGO INGRESADO DE ETAPA
def Recuperar_Etapa(CodigoEtapa):
    NombreEtapa=""
    for obj in ListOfEtapas:
        if int(obj.Codigo)==int(CodigoEtapa):
            NombreEtapa= obj.Nombre

    return NombreEtapa

def Recuperar_Etapa_porNombre(unaEtapa):
    objEtapa:Etapa=None
    
    for obj in ListOfEtapas:
        if obj.Nombre==unaEtapa:
            objEtapa= obj
            break

    return objEtapa

def Cargar_AvanceObra():
    Imprimir_TituloPantalla()    
    
    print("SUBMENU << REGISTRO AVANCE OBRA >>")
    NombreObra=validarEntrada("Ingrese el Nombre de Obra: ")
    if Existe_Obra(NombreObra)==True:
        # SI LA NUEVA OBRA EXISTE, SOLICITA LOS DATOS DEL AVANCE
        FechaAvance=validarEntrada("Ingrese la fecha de avance (AAAA-MM-DD)")
        print("Ingrese la Etapa en la cual realizo avances: ")
        for obj in ListOfEtapas:
            print(f"({obj.Codigo}) {obj.Nombre}")        
        opcionEtapa=validarEntrada("Ingrese una opcion: ", True)
        NombreEtapa=Recuperar_Etapa(opcionEtapa)
        porcentaje=validarEntrada("Ingrese el Porcentaje de Avance: ", True)

        mi_avance=AvanceObra(NombreObra,FechaAvance,NombreEtapa,porcentaje)
        ListOfAvance.append(mi_avance)

        ActualizarArchivo_AvancesObra()
    else:
        print("LA OBRA INGRESADA NO EXISTE")

    print("  ")
    seguir=validarEntrada("PRESION (V) PARA VOLVER AL MENU PRINCIPAL.")

def Generar_QrAvanceObra():
    try:
        Imprimir_TituloPantalla()
        print("SUBMENU << GENERACION QR AVANCE OBRA >>")
        NombreObra=validarEntrada("Ingrese el Nombre de Obra: ")
        if Existe_Obra(NombreObra)==True:

            for obra in ListOfAvance:
                if obra.NombreObra==NombreObra:
                    img = qrcode.make(obra)
                    f = open(f"{obra.NombreObra}.png", "wb")
                    img.save(f)
                    f.close()

            print("Qr GENERADO CON EXITO!!!!")                

        else:
            print("LA OBRA INGRESADA NO EXISTE")

        print("  ")
        seguir=validarEntrada("PRESION (V) PARA VOLVER AL MENU PRINCIPAL.")    
    except:
        print("Error al generar el codigo QR")

def Consultar_QrAvanceObra():

    Imprimir_TituloPantalla()
    print("SUBMENU << VISUALIZADOR AVANCE OBRA >>")
    NombreObra=validarEntrada("Ingrese el Nombre de Obra: ")
    if Existe_Obra(NombreObra)==True:
        img = Image.open(f'{NombreObra}.png')
        img.show()                

    else:
        print("LA OBRA INGRESADA NO EXISTE")

    print("  ")
    seguir=validarEntrada("PRESION (V) PARA VOLVER AL MENU PRINCIPAL.")

def Consultar_QrObras():
    Imprimir_TituloPantalla()

    print("SUBMENU << CONSULTA OBRA >>")
    for obj in ListOfPlanificacion:
        print(f"{obj}")        

    print("  ")
    seguir=validarEntrada("PRESION (V) PARA VOLVER AL MENU PRINCIPAL.")

def main():    
    CargarArchivo_AvanceObra()
    CargarArchivo_Etapas()
    CargarArchivo_PlanificacionObra()

    FinalizaApp=0
    
    while FinalizaApp!=99:
        Imprimir_TituloPantalla()

        print(":: MENU PRINCIPAL ::")
        print("(1) CARGA NUEVA OBRA")
        print("(2) CARGA AVANCE DE OBRA")
        print("(3) GENERAR QR AVANCE DE OBRA")
        print("(4) CONSULTAR QR AVANCE OBRA")
        print("(5) CONSULTAR OBRAS")
        print("(99) FINALIZAR APP")
        FinalizaApp=validarEntrada("INGRESE LA OPCION :", True)

        if FinalizaApp==1:
            Cargar_NuevaObra()

        elif FinalizaApp==2:
            Cargar_AvanceObra()

        elif FinalizaApp==3:
            Generar_QrAvanceObra()

        elif FinalizaApp==4:
            Consultar_QrAvanceObra()

        elif FinalizaApp==5:
            Consultar_QrObras()

        elif FinalizaApp < 0 and FinalizaApp > 5:
            print("Opcion invalida.")


if __name__ == '__main__':

    main()