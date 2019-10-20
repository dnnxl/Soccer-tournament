#----------------------------------------
#Autor Danny Xie Li
#Tarea Programada 4
#Instituto Tecnologico de Costa Rica
#Profesor William Mata
#Versión 0.0.1
#Fecha de entrega 27/11/16
#----------------------------------------

#-----------------
#Librerías Usadas
#-----------------

from os import startfile 
import random
import time
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

#-------------------
#Variables globales
#-------------------

PosicionesEquipos = []
EquipoProceso = []
EquiposAgregar = []
Jugadores = []
ConfiguracionLista = []
CodigoPaisConsultar = ""
ListaDeEquipos = []
Combinaciones = []
CombinacionesTodos = []
Fechas = []
ResultadosLista = []
JugadoresAnotadores = []
ResultadosDePartidos = []

#----------
#Funciones
#----------

#----------------------------------------------------------------------------------
#Descricpción: La siguiente función abre el manual de usuario de torneos de futbol.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def ManualTorneo():
    startfile("manual_de_usuario_torneos_de_futbol.pdf")

#----------------------------------------------------------------------------------------
#Descricpción: La siguiente función abre el video manual de usuario de torneos de futbol.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

def ManualVideoTorneo():
    startfile("manual_video_de_usuario_torneos_de_futbol.mp4")

#---------------------------------------------------------------------
#Descripción: La siguiente función despliega 2 botones en la pantalla.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def OpcionesAcercaDe():
       Button(ventanaDTorneosFutbol,command=ManualTorneo,bg="black",image=manu,relief=FLAT).place(x=510,y=270) #Boton de salida
       Button(ventanaDTorneosFutbol,command=ManualVideoTorneo,image=vide,bg="black",relief=FLAT).place(x=510,y=390)#Boton de salida

#-------------------------------------------------------------------------------------
#Descripción: La siguiente función asigna todos los valores de los equipos a la lista.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
#Se usó iteración debido a que ocupaba modificar la variable global, de otra manera ocuparía usar más código, menos eficiencia.

def ListaEquipos():
    global ListaDeEquipos,ConfiguracionLista
    l=ConfiguracionLista[5]
    for i in l:
        ListaDeEquipos = ListaDeEquipos + [i[1]]
        
#-----------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista de número según el parametro que se le da.
#Entradas: Un entero positivo.
#Salidas: Una lista de números.
#Restricciones: Sólo enteros positivos.

def imprimir(num,cont=1,lista=[]):
    if num+1 == cont:
        return lista
    else:
        return imprimir(num,cont+1,lista=lista+[cont])

#---------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un número según la cantidad de caracteres que hay en el string.
#Entradas: Un string.
#Salidas: Una número entero.
#Restricciones: Sólo strings.

def Contar(string):
    if string == "":
        return 0
    else:
        return 1+Contar(string[1:])

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función carga la configuración almacenada a la variable global.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CargarConfiguración():
    global ConfiguracionLista
    contenido = leerTodo("configuracion_torneos_de_futbol.txt")
    if contenido == "" :
        ConfiguracionLista  = []
        return contenido
    else:
        ConfiguracionLista  = eval(contenido)
        return eval(contenido)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna el contenido leído en un archivo en formato string, cuando se le digite la entrada que es el nombre del archivo en formato string.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo en formato string.

def leerTodo (nombreArchivo):
    archivo = open (nombreArchivo, "r+")  #Abre el archivo y la operación es sólo escritura.
    contenido = archivo.read ()  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.
    return contenido

#-----------------------------------------------------------------------------------        
#Descripción: La siguiente funcion sobrescribe el archivo y guarda la configuración.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
        
def SobreescribeConfi():
    global ConfiguracionLista
    archivo = open ("configuracion_torneos_de_futbol.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(ConfiguracionLista))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#--------------------------------------------------------------------------------------        
#Descripción: La siguiente funcion retorna una lista de solo los codigos de los equipos.
#Entradas: Una lista y un entero.
#Salidas: Una lista.
#Restricciones: Sólo listas y enteros positivos.

def ListaCodigos(listaequipo,pos):
    if listaequipo == []:
        return []
    else:
        return [listaequipo[0][pos]] + ListaCodigos(listaequipo[1:],pos)

#--------------------------------------------------------------------------------------        
#Descripción: La siguiente funcion retorna la cantidad de elementos que tiene una lista.
#Entradas: Una lista.
#Salidas: Un entero positivo.
#Restricciones: Sólo listas.
       
def ContarElementosDeLista(lista):
    if lista == []:
        return 0
    else:
        return 1 + ContarElementosDeLista(lista[1:])

#--------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función es para aceptar las modificaciones hechas en la planilla de jugadores.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def AceptarModificaciones():
    global ConfiguracionLista,CodigoPaisConsultar
    CodigoPaisConsultar = ""
    SobreescribeConfi2(ConfiguracionLista)
    return messagebox.showinfo("Info","Modificaciones guardados con exito")

#-------------------------------------------------------
#Descripción: La siguiente función sobrescribe una lista
#Entradas: Una lista.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def SobreescribeConfi2(lista):
    archivo = open ("configuracion_torneos_de_futbol.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(lista))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#----------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna la lista de jugadores según el equipo que estaba buscando.
#Entradas: Un string.
#Salidas: Una lista.
#Restricciones: Sólo strings.
    
def JugadoresConsultar(equipo):
    global ConfiguracionLista #Usa iteración debido a que se ocupa los datos de la variable global pero sin modificarlos, si usará recursividad tendría que modificar la variable global y eso es lo que no ocupo.
    for i in ConfiguracionLista[5]:
        if i[0] == equipo:
            return i[3]

#------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista nueva con los datos del jugador que desea agregar.
#Entradas: Dos strings, un entero y una lista.
#Salidas: Una lista.
#Restricciones: Sólo strings, enteros y listas.
        
def AgregarJugador(jugador,posicion,chema,lista):
    lista = lista + [[jugador,posicion,chema]]
    return lista

#-----------------------------------------------------------------------------------------------
#Descripción: La siguiente fucnión retorna una lista, si encuentra el jugador que esta buscando.
#Entradas: Un string y una lista.
#Salidas: Una lista.
#Restricciones: Sólo strings y listas.

def BuscarJugador(jugador,lista):
    if lista == []:
        return []
    if lista[0][0] == jugador:
        return lista[0]
    else:
        return BuscarJugador(jugador,lista[1:])

#--------------------------------------------------------------------------------------------------
#Descripción: La siguiente función modifica un jugador, si se desea modificar la posicion o numero.
#Entradas: Dos strings, un entero y una lista.
#Salidas: Una lista.
#Restricciones: Sólo lista, strings y enteros.
    
def ModificarJugador(jugador,posicion,chema,lista):
    if posicion != "" and chema !="0":
        nuevo = EliminarJugadores(jugador,lista)
        return [[jugador,posicion,chema]]+nuevo
    if posicion != "":
        nuevo = EliminarJugadores(jugador,lista)
        return [[jugador,posicion,lista[2]]]+nuevo
    if chema != "0":
        nuevo = EliminarJugadores(jugador,lista)
        return [[jugador,lista[1],chema]]+nuevo

#-----------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con los jugadores según el codigo del país.
#Entradas: Una lista y un string.
#Salidas: Una lista.
#Restricciones: Sólo lista y strings.
    
def PaisJugadores(lista,pais):
    if lista == []:
        return
    if lista[0][0] == pais:
        return lista[0][3]
    else:
        return PaisJugadores(lista[1:],pais)

#--------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con los datos del equipo según el codigo del equipo.
#Entradas: Una lista y un string.
#Salidas: Una lista.
#Restricciones: Sólo lista y strings.
    
def PaisEquipo(lista,pais):
    if lista == []:
        return []
    if lista[0][0] == pais:
        return lista[0]
    else:
        return PaisEquipo(lista[1:],pais)

#-----------------------------------------------------------------
#Descripción: La siguiente función elimina jugadores en un equipo.
#Entradas: Un string y una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas y strings.
    
def EliminarJugadores(jugador,lista,nuevo=[]):
    if lista == []:
        return nuevo
    if lista[0][0] == jugador:
        return EliminarJugadores(jugador,lista[1:],nuevo=nuevo)
    else:
        return EliminarJugadores(jugador,lista[1:],nuevo=nuevo+[lista[0]])

#-------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano si el jugador se encuentra en la lista de equipo.
#Entradas: Un string y una lista.
#Salidas: Un valor booleano.
#Restricciones: Sólo string y lista.
    
def Esta125(jugador,lista,valor=True):
    if lista == []:
        return valor
    if lista[0][0] == jugador:
        return True
    else:
        return Esta125(jugador,lista[1:],valor=False)

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con números hasta n lo que uno desea.
#Entradas: Un número entero.
#Salidas: Una lista.
#Restricciones: Sólo números enteros.
    
def imprimir(num,cont=1,lista=[]):
    if num+1 == cont:
        return lista
    else:
        return imprimir(num,cont+1,lista=lista+[cont])


#-----------------------------------------------------------------------------------------
#Descripción: La siguiente función cuenta la cantidad de elementos que posee en una lista.
#Entradas: Una lista.
#Salidas: Un entero positivo.
#Restricciones: Sólo listas.

def ContarElementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + ContarElementos(lista[1:])

#-----------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con 2 números aleatorios.
#Entradas: Un entero positivo.
#Salidas: Una lista.
#Restricciones: Sólo enteros positivos.
    
def PosiblesNumeros(n2):
    lista = CrearLista(n2)
    l = Diferentes(random.sample(lista,2),n2)
    return l

#-----------------------------------------------------------------------------
#Descripción: La siguiente función crea una lista de n-1 a n.
#Entradas: Un entero positivo.
#Salidas: Una lista.
#Restricciones: Sólo enteros positivos.

def CrearLista(n,cont=0,lista=[]):
    if cont==n:
        return lista
    else:
        return CrearLista(n,cont=cont+1,lista=lista+[cont])

#-------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con dos números diferentes.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
    
def Diferentes(lista,n2):
    l=lista
    while l[0] == l[1]: #Se usa iteración para poder usar asignación y ahorrar código es decir hacerlo más eficiente.
        l=random.sample(CrearLista(n2),2)
        continue
    return l       

#--------------------------------------------------------------------------------------
#Descripción: La siguiente función saca una lista con una combinacion de dos elementos.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def P(lis):
    o=PosiblesNumeros(ContarElementos(lis))
    n=o[0]
    n1=o[1]
    l=lis
    lista=[l[n],l[n1]]
    return lista

#-------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano, si el elemnto esta o no esta en una lista.
#Entradas: Un string y una lista.
#Salidas: Un valor booleano.
#Restricciones: Sólo strings y listas.

def Esta(ele,lista): #Eficiencia en el código.
    for i in lista:
        if i == ele:
            return True
    return False

#--------------------------------------------------------------------
#Descripción: La siguiente función retorna el factorial de un número.
#Entradas: Un entero.
#Salidas: Un entero.
#Restricciones: Sólo números positivos.
    
def Factorial(num,resul=1):
    if num == 0:
        return resul
    else:
        return Factorial(num-1,resul*num)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano si una lista con dos elementos es correcto o no según las indicaciones del proyecto.
#Entradas: Una lista.
#Salidas: Un valor booleano.
#Restricciones: Sólo listas.

#TodosLosCombinaciones(["aaa","eee","ccc","jjj","ooo","ttt"])

def Correcto2(lista): #Formato ["mm","ff"]
    global Fechas,Combinaciones
    if lista==[]:
        return False
    if Esta(lista,Combinaciones):
        return False
    if lista[0] == lista[1]:
        return False
    else:
        return True

#------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función crea una lista que es correcta según las indicaciones que pidió en el enunciado.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
    
def FormarCorrecto2(lista):
    global Fechas,Combinaciones
    formado=[]
    while Correcto2(formado)==False: #Para asignación,debido a que en la recursividad era menos eficiente y daba errores de maxima recursividad. 
        formado=P(lista)
        continue
    return formado

#--------------------------------------------------------------------------------------
#Descripción: L siguiente función crea todos las combinaciones posibles de n elementos.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def TodosLosCombinaciones(lista):
    global Combinaciones
    Can=int((Factorial(ContarElementos(lista))/(Factorial(ContarElementos(lista)-2))))
    for i in range(Can):#Para asignación,debido a que en la recursividad era menos eficiente y daba errores de maxima recursividad. 
        Combinaciones=Combinaciones+[FormarCorrecto2(lista)]
    return Combinaciones

#--------------------------------------------------------------------
#Descripción: La siguiente función eliina dos elementos de una lista.
#Entradas: Dos lista..
#Salidas: Una lista. 
#Restricciones: Sólo listas.

def EliminarDosElemento(l,l1):
    n=[]
    for i in l1: 
        if i == l[0] or i == l[1]:
            continue
        else:
            n=n+[i]
    return n

#---------------------------------------------------------------
#Descripción: La siguiente función elimina un elementoe una lista.
#Entradas: Un elemento y una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas y strings o enteros.

def EliminarElemento(ele,lista):
    n=[]
    for i in lista:
        if i == ele or i == ele:
            continue
        else:
            n=n+[i]
    return n

#-----------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función crea todos los combinaciones posibles y se lo asigna a la varible global.
#Entradas: Una lista.
#Salidas: Ninguna.
#Restricciones: Sólo listas.

def CrearCombinaciones(lista):
    global CombinacionesTodos
    CombinacionesTodos=TodosLosCombinaciones(lista)
    print(CombinacionesTodos)

#-----------------------------------------------------------------------
#Descripción: La siguiente función crea todas las fechas del calendario.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def TodosLasFechas():
    global ListaDeEquipos,CombinacionesTodos
    cont=1
    while CombinacionesTodos != []:
        FormarFechas(ListaDeEquipos,cont)
        cont=cont+1
    
#----------------------------------------------------------------
#Descripción: La siguiente función crea una fecha del calendario.
#Entradas: Una lista y un entero.
#Salidas: Una lista.
#Restricciones: Sólo listas y enteros positivos.

def FormarFechas(lista,cual):#Usar con variable global
    global CombinacionesTodos,Fechas
    l=lista
    n=[]
    cont=0
    while l != []: #Se usa iteración debido a que habría una máxima capacidad de recursividad.
        if CombinacionesTodos[0][0] in l and CombinacionesTodos[0][1] in l:
            n=n+[CombinacionesTodos[0]]#cont
            l=EliminarDosElemento(CombinacionesTodos[0],l)#cont
            CombinacionesTodos=EliminarElemento(CombinacionesTodos[0],CombinacionesTodos)#cont
            random.shuffle(CombinacionesTodos)
            cont=cont+1
            continue
        if [l] not in CombinacionesTodos:
            CombinacionesTodos=CombinacionesTodos+n
            l=lista
            n=[]
        else:
            random.shuffle(CombinacionesTodos)
            cont=cont+1
            continue
    Fechas=Fechas+[["Fecha "+str(cual),n]]
    print(Fechas)
    return [["Fecha "+str(cual),n]]     

#-------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función usa retorna un valor booleano si un partido se encuentra en una lista.
#Entradas: Dos strings y una lista.
#Salidas: Un valor booleano.
#Restricciones: Sólo strings y listas.

def Esta2(Casa,visita,lista):
    for i in lista:
        if i[0] == Casa and i[2] == visita:
            return True
    return False

#-----------------------------------------------------------------------------------------------------
#Descripción: La siguiente función usa retorna una lista con los jugadores que anotaron en ese partido.
#Entradas: Dos strings.
#Salidas: Una lista.
#Restricciones: Sólo strings.

def Encontrar(Casa,visita):
    global ResultadosDePartidos
    for i in ResultadosDePartidos:
        if i[0] == Casa and i[2] == visita:
            return i[4]
    return 

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función carga la configuración almacenada a la variable global.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CargarResultados():
    global ResultadosDePartidos
    contenido = leerTodo("resultados_torneos_de_futbol.txt")
    if contenido == "" :
        ResultadosDePartidos  = []
        return contenido
    else:
        ResultadosDePartidos  = eval(contenido)
        return eval(contenido)

#-----------------------------------------------------------------------------------        
#Descripción: La siguiente funcion sobrescribe el archivo y guarda la configuración.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
        
def SobreescribeResul():
    global ResultadosDePartidos
    archivo = open ("resultados_torneos_de_futbol.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(ResultadosDePartidos))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#----------------------------------------------------------------------------------------------        
#Descripción: La siguiente funcion cuenta la cantidad de letras que tiene una cadena de string.
#Entradas: Un string.
#Salidas: Un entero positivo.
#Restricciones: Sólo strings.

def ContarString(string):
    if string == "":
        return 0
    else:
        return 1 + ContarString(string[1:])

#-------------------------------------------------------------------------------------------------------------------        
#Descripción: La siguiente funcion cuenta la cantidad de goles que se registraron en la pantalla de registrar datos.
#Entradas: Un string y una lista.
#Salidas: Un entero positivo.
#Restricciones: Sólo strings y listas.

def ContarGoles(equipo,lista):#[["Pedro","CRC"]]
    cont=0
    for i in lista:
        if i[1] == equipo:
            cont=cont+1
            continue
        else:
            continue
    return cont

#----------------------------------------------------------------------------------------------------------        
#Descripción: La siguiente funcion cuenta la cantidad de listas de jugadores que hay en la variable global.
#Entradas: Ninguna.
#Salidas: Un entero.
#Restricciones: Ninguno.

def CantidaDeJugadores():
    global JugadoresAnotadores
    cont=0
    for i in JugadoresAnotadores:
        cont=cont+1
    return cont

#-----------------------------------------------------------------------
#Descripción: La siguiente función ordena los equipos según los puntos.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.
    
def OrdenarListaEquipoPuntos(): 
    global ResultadosDePartidos,ConfiguracionLista
    ListaPuntos = ListasDePosiciones()
    L = OrdenarMaximo(SóloPuntos(ListaPuntos))
    n = []
    M = ListaPuntos
    for i in L: #Se usa para listas anidadas.
        for j in M:
            if i == j[8]:
                n=n+[j]
                M = eliminar3(j,M)
                break
    return n

#--------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con sólo el código de los equipos.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo lista.
        
def EquiposListaSolo(lista,nuevo=[]):
    if lista == []:
        return nuevo
    else:
        return EquiposListaSolo(lista[1:],nuevo=nuevo+[[lista[0][1],lista[0][0]]])

#-------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con las posiciones en el escalon de los equipos participantes.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.
    
def ListasDePosiciones():
    global ConfiguracionLista
    p = PosicionEscalon(ConfiguracionLista)
    Obj = p.Ordenado()
    new = EquiposListaSolo(Obj)
    n=[]
    for i in new:
        l=PuntosEquipos(i)
        n = n + [l.CrearListaTeam()]
    return n

#--------------------------------------------------------------------------------------------
#Descripción: Esta función retorna una lista con solo los puntos de los equipos participantes.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def SóloPuntos(lista,nuevo=[]):
    if lista == []:
        return nuevo
    else:
        return SóloPuntos(lista[1:],nuevo=nuevo+[lista[0][8]])

#-----------------------------------------------------------------------------------
#Descripción: La siguiente función ordena de mayor a menor los puntos de los equipos.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def OrdenarMaximo(lista,nuevo=[]): 
    if lista == []:
        return nuevo
    else:
        return OrdenarMaximo(eliminar3(max(lista),lista),nuevo=nuevo+[max(lista)])

#------------------------------------------------------------------------------
#Descripción: La siguiente función elimina la primera aparición de ese elemento.
#Entradas: Un string, lista o entero.
#Salidas: Una lista.
#Restricciones: Sólo enteros,lista o strings.

def eliminar3(ele,lista,nuevo=[],cont=0):
    if lista == []:
        return nuevo
    if lista[0] == ele and cont == 0:
        return eliminar3(ele,lista[1:],nuevo,cont=cont+1)
    else:
        return eliminar3(ele,lista[1:],nuevo+[lista[0]],cont)
    
#----------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena la lista de equipos según los puntos que tiene. 
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def OrdenarListaEquipoPuntos(): 
    global ResultadosDePartidos,ConfiguracionLista
    ListaPuntos = ListasDePosiciones()
    L = OrdenarMaximo(SóloPuntos(ListaPuntos))
    n = []
    M = ListaPuntos
    for i in L:
        for j in M:
            if i == j[8]:
                n=n+[j]
                M = eliminar3(j,M)
                break
    return n

#-----------------------------------------------------------------------------
#Descripción: La siguiente función elimina el elemento que se quiere eliminar.
#Entradas: Un string, lista o entero.
#Salidas: Una lista.
#Restricciones: Sólo listas, enteros o strings. 

def eliminar4(ele,lista,n=[]):
    if lista == []:
        return n
    if ele == lista[0]:
        return eliminar4(ele,lista[1:],n)
    else:
        return eliminar4(ele,lista[1:],n=n+[lista[0]])

#---------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con los elementos sin repetir.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
    
def SinRepetir(lista,n=[]):
    if lista == []:
        return n
    if lista[0] in lista[1:]:
        return SinRepetir(eliminar4(lista[0],lista[1:]),n=n+[lista[0]])
    else:
        return SinRepetir(lista[1:],n+[lista[0]])

#-------------------------------------------------------------------------------------------------
#Descripción: La siguiente función cuenta la cantidad de listas de equipos que tenga esos equipos.
#Entradas: Un entero y una lista.
#Salidas: Un entero.
#Restricciones: Sólo listas y enteros.

def Contar3(num,lista,n=0):
    if lista == []:
        return n
    if num == lista[0][8]:
        return Contar3(num,lista[1:],n+1)
    else:
        return Contar3(num,lista[1:],n)

#---------------------------------------------------------------------------------------
#Descripción: La sguiente función retorna una lista, es el euqipo que tenga esos puntos. 
#Entradas: Un entero y una lista. 
#Salidas: Una lista.
#Restricciones: Sólo enteros y listas.

def EsEseEquipo(pts,lista):
    for i in lista:
        if i[8] == pts:
            return i

#---------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista de los equipos que tenga el punto que le digite. 
#Entradas: Un entero y una lista.
#Salidas: Una lista.
#Restricciones: Sólo enteros y listas.
        
def SóloLosEquiposConEsePunto(punto,lista):
    n=[]
    for i in lista:
        if i[8] == punto:
            n=n+[i]
    return n

#------------------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena las listas de los equipos según la diferencia de goles.
#Entradas: Ninguna.
#Salidas: Una lista.
#Restricciones: Ninguna.

def OrdenarSegunPuntosyDiferencias():
    puntos = SinRepetir(SóloPuntos(OrdenarListaEquipoPuntos()))
    n=[]
    for i in puntos:
        if Contar3(i,OrdenarListaEquipoPuntos()) >1:
            l = SonIguales(SóloLosEquiposConEsePunto(i,OrdenarListaEquipoPuntos()))
            k = SinRepetir(l.OrdenadoPorPuntosDiferencias())
            n = n + k
            continue
        else:
            n = n + [EsEseEquipo(i,OrdenarListaEquipoPuntos())]
            continue
    return n
            
#----------------------------------------------------------------------------
#Descripción: La siguiente función retorna el equipo que pertenece el jugador.
#Entradas: Un string.
#Salidas: Un string.
#Restricciones: Sólo strings.

def OnlyPlayers(nombre):
    global ConfiguracionLista
    n = []
    for i in ConfiguracionLista[5]:
        for j in i[3]:
            if j[0] == nombre:
                return i[1]
    return 

#--------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con todos los jugadores que anotaron en los partidos.
#Entradas: Una lista
#Salidas: Una lista.
#Restricciones: Sólo listas.

def TodosLosPartidos(lista,nuevo=[]):
    if lista == []:
        return nuevo
    else:
        return TodosLosPartidos(lista[1:],nuevo=nuevo+lista[0][4])

#---------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con sólo los jugadores.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones:Sólo listas.

def SóloJugadores(lista,nuevo=[]):
    if lista == []:
        return nuevo
    else:
        return SóloJugadores(lista[1:],nuevo=nuevo+[lista[0][0]]) 

#------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna la cnatidad de goles que posee el jugador.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
    
def GolesJugador(lista):
    global ResultadosDePartidos
    nuevo=[]
    ListaJugador=TodosLosPartidos(ResultadosDePartidos)
    for i in lista:
        if CantidadDeGoles(i,ListaJugador) == 0:
            continue
        else:
            nuevo=nuevo+[[i,CantidadDeGoles(i,ListaJugador)]]
    return nuevo

#----------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna la cnatidad de autogoles que posee el jugador.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def AutoGolesJugador(lista,jugadores):
    nuevo=[]
    for i in lista:
        if AutoGoles(i,jugadores) == 0:
            continue
        else:
            nuevo=nuevo+[[i,AutoGoles(i,jugadores)]]
    return nuevo

#---------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un entero que indica la cantidad de goles que tiene un jugador.
#Entradas: Un string y una lista.
#Salidas: Un entero.
#Restricciones: Sólo strings y listas.

def CantidadDeGoles(Jugador,lista,cont=0):
    global ConfiguracionLista
    if lista == []:
        return cont
    if Jugador == lista[0][0] and BuscarTeam(Jugador,ConfiguracionLista[5]) == lista[0][1]:
        return CantidadDeGoles(Jugador,lista[1:],cont=cont+1)
    else:
        return CantidadDeGoles(Jugador,lista[1:],cont=cont+0)

#-------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un entero que indica la cantidad de autogoles que tiene un jugador.
#Entradas: Un string y una lista.
#Salidas: Un entero.
#Restricciones: Sólo strings y listas.
    
def AutoGoles(Jugador,lista,cont=0):
    global ConfiguracionLista
    if lista == []:
        return cont
    if Jugador == lista[0][0] and BuscarTeam(Jugador,ConfiguracionLista[5]) != lista[0][1]:
        return AutoGoles(Jugador,lista[1:],cont=cont+1)
    else:
        return AutoGoles(Jugador,lista[1:],cont=cont+0)
    
#------------------------------------------------------------------------
#Descripción: La siguiente función retorna el equipo que esta el jugador.
#Entradas: Un string y una lista.
#Salidas: Un string.
#Restricciones: Sólo listas y strings.
    
def BuscarTeam(jugador,lista): 
    for i in lista:
        for j in i[3]:
            if j[0] == jugador:
                return i[0]
    return 

#--------------------------------------------------------------------------------
#Descripción: La siguiente función ordena la lista de goleadores según los goles.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def OrdenarLalistaDeGoleadores(lista):
    n = MaximoGoles(SóloGoles(lista))
    lis = []
    for i in n:
        for j in lista:
            if i == j[1]:
                lis = lis + [j]
                break
    return lis

#-----------------------------------------------------------------------------------------------
#Descripción: La siguiente función cuenta los jugadores que hicieron la misma cantidad de goles.
#Entradas: Un entero y una lista.
#Salidas: Un entero.
#Restricciones: Sólo enteros y listas.

def ContarParteGoleador(gol,lista,cont=0):
    if lista == []:
        return cont
    if lista[0][1] == gol:
        return ContarParteGoleador(gol,lista[1:],cont+1)
    else:
        return ContarParteGoleador(gol,lista[1:],cont)

#--------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con los jugadores que anotaron el mismo cantidad de goles.
#Entradas: Un entero y una lista.
#Salidas: Una lista.
#Restricciones: Sólo enteros y listas.
    
def SoloEsosJugadoresConLosMismoGoles(gol,lista,nuevo=[]):
    if lista == []:
        return nuevo
    if lista[0][1] == gol:
        return SoloEsosJugadoresConLosMismoGoles(gol,lista[1:],nuevo+[lista[0]])
    else:
        return SoloEsosJugadoresConLosMismoGoles(gol,lista[1:],nuevo)

#-----------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena en orden alfabetico los nombre de los jugadores.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def OrdenAlfabetico(lista):
    l=lista
    n =[]
    while l != []:
        n = [max(l)]+n
        l.remove(max(l))
    return n

#------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con solo los nombres de los jugadores.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def SoloNombres(lista,n=[]):
    if lista==[]:
        return n
    else:
        return SoloNombres(lista[1:],n+[lista[0][0]])

#-----------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista con los nombres de los jugadores pero con su equipo correspondiente.
#Entradas: Dos listas.
#Salidas: Una lista.
#Restricciones: Sólo listas.

def Arreglado(listadenombre,lista):
    n=[]
    for i in listadenombre:
        for j in lista:
            if i == j[0]:
                n=n+[j]
    return n

#---------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena según la cantidad de goles, y en orden alfabetico los jugadores.
#Entradas: Ninguna.
#Salidas: Una lista.
#Restricciones: Ninguna.

def OrdenMaximo_aux():
    global ResultadosDePartidos
    Anotadores = GolesJugador(SóloJugadores(TodosLosPartidos(ResultadosDePartidos)))
    l = MaximoGoles(SinRepetir(SóloGoles(Anotadores)))
    new = []
    for i in l:
        print(l)
        if ContarParteGoleador(i,Anotadores)>1:
            nuevo = Arreglado(OrdenAlfabetico(SoloNombres(SoloEsosJugadoresConLosMismoGoles(i,Anotadores))),Anotadores)
            new=new+nuevo
        else:
            Este=SoloEsosJugadoresConLosMismoGoles(i,Anotadores)
            new=new+Este
    return SinRepetir(new)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función es complemento de la función OrdenMaximo_aux, ordena según la cantidad de goles, y en orden alfabetico los jugadores.
#Entradas: Ninguna.
#Salidas: Una lista.
#Restricciones: Ninguna.

def OrdenMaximo():
    l = OrdenMaximo_aux()
    nuevo=[]
    for i in l:
        nuevo=nuevo+[[i[0],OnlyPlayers(i[0]),i[1]]]
    return nuevo

#-------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función ordena según la cantidad de autogoles, y en orden alfabetico los jugadores.
#Entradas: Ninguna.
#Salidas: Una lista.
#Restricciones: Ninguna.

def OrdenMaximo_aux2():
    global ResultadosDePartidos
    Anotadores = AutoGolesJugador(SóloJugadores(TodosLosPartidos(ResultadosDePartidos)),TodosLosPartidos(ResultadosDePartidos))
    l = MaximoGoles(SinRepetir(SóloGoles(Anotadores)))
    new = []
    for i in l:
        if ContarParteGoleador(i,Anotadores)>1:
            nuevo = Arreglado(OrdenAlfabetico(SoloNombres(SoloEsosJugadoresConLosMismoGoles(i,Anotadores))),Anotadores)
            new=new+nuevo
        else:
            Este=SoloEsosJugadoresConLosMismoGoles(i,Anotadores)
            new=new+Este
    return SinRepetir(new)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función es complemento de la función OrdenMaximo_aux2, ordena según la cantidad de autogoles, y en orden alfabetico los jugadores.
#Entradas: Ninguna.
#Salidas: Una lista.
#Restricciones: Ninguna.

def OrdenMaximo2():
    l = OrdenMaximo_aux2()
    nuevo=[]
    for i in l:
        nuevo=nuevo+[[i[0],OnlyPlayers(i[0]),i[1]]]
    return nuevo

#--------------------------------------------------------------------------------
#Descripción: La siguiente retorna una lista con sólo los goles de los jugadores.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
        
def SóloGoles(lista,n=[]):
    if lista == []:
        return n
    else:
        return SóloGoles(lista[1:],n+[lista[0][1]])

#---------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna una lista de goles ordenado de mayor a menor.
#Entradas: Una lista.
#Salidas: Una lista.
#Restricciones: Sólo listas.
    
def MaximoGoles(listadegoles):
    l=listadegoles
    n=[]
    while l != []:
        n=n+[max(l)]
        l.remove(max(l))
    return n

#-------------------------------------------------------
#Descripción: La siguiente función sobrescribe una lista
#Entradas: Una lista.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def SobreescribeResultados(lista):
    archivo = open ("resultados_torneos_de_futbol.txt", "w")  #Abre el archivo y la operación es sólo escritura.
    archivo.write (str(lista))  #El contenido leído se lo asigna a la variable.
    archivo.close() #Se cierra el archivo.

#-------------------------------------------------------------------------------------------------------------
#Descripción: La siguiente función retorna un valor booleano si el jugador se encuentra en la lista de equipo.
#Entradas: Un string y una lista.
#Salidas: Un valor booleano.
#Restricciones: Sólo string y lista.
    
def Esta12(jugador,lista):
    if lista == []:
        return False
    if lista[0][0][0] == jugador:
        return True
    else:
        return Esta12(jugador,lista[1:])

#-------------------------------
#Ventana de Tabla de Goleadores 
#-------------------------------

def VentanaTablaDeGoleadores():

    #------------------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels de los goleadores al notebook.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarGoledoresAlNote():
        global ResultadosDePartidos
        Jugadores = OrdenMaximo()
        fila=0
        for i in Jugadores:
            Label(frameDeCanvas1,fg="white",text=str(i[0]),bg="#2FA4A4",width=10,font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas1,fg="white",text=str(i[1]),bg="#2FA4A4",width=12,font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas1,fg="white",text=str(i[2]),bg="#2FA4A4",width=9,font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
            fila=fila+1
        
    #----------------------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels de los autogoleadores al notebook.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarAutoGoledoresAlNote():
        Jugadores = OrdenMaximo2()
        print(Jugadores)
        fila=0
        for i in Jugadores:
            Label(frameDeCanvas2,fg="white",text=str(i[0]),bg="#2FA4A4",width=10,font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas2,fg="white",text=str(i[1]),bg="#2FA4A4",width=12,font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas2,fg="white",text=str(i[2]),bg="#2FA4A4",width=9,font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
            fila=fila+1

    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
            
    def Eventos1(eventos):
        canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)

    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas3.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos2(eventos):
        canvas3.configure(scrollregion=canvas3.bbox("all"),width=250,height=280)

    #-------------------------------------------------------
    #Descripción: Cierra la pantalla de tabla de goleadores.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def CerrarVentanaGoledores():
        ventanaGoleadores.destroy()

    #-----------------------------------------------------------------------------------
    #Descripción: Cierra la pantalla de tabla de goleadores y abre la pantalla principal.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def Volver():
        ventanaGoleadores.destroy()
        ventanaDTorneosFutbol.deiconify()

    CargarResultados()
    CargarConfiguración()
    ventanaDTorneosFutbol.iconify()
    ventanaGoleadores = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaGoleadores.title("DTorneo de Fútbol") #Titulo de la ventana.
    ventanaGoleadores.geometry("797x436") #Tamano de la ventana.
    ventanaGoleadores.maxsize(797,436) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaGoleadores.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    icono = ventanaGoleadores.iconbitmap("futbol.ico") #Icono de la ventana.
    canvas = Canvas(ventanaGoleadores,width=300, height=200, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    AcercaDe = Image.open("TablaGoleadores.png") #Imagen.
    AcercaDe1 = ImageTk.PhotoImage(AcercaDe) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = AcercaDe1 #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor=NW, image=AcercaDe1) #Se crea el fondo de pantalla.
    nbook = ttk.Notebook(ventanaGoleadores,height=220,width=260) #Sea un nootebook dentro de la ventana.
    nbook.place(x=50,y=135) #Lo ubica en ese eje.
    nbook2 = ttk.Notebook(ventanaGoleadores,height=220,width=260) #Sea un nootebook dentro de la ventana.
    nbook2.place(x=415,y=135) #Lo ubica en ese eje.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas2 = Canvas(frame1,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas2) #Se crea ua miniventana.
    frameDeCanvas1 = Frame(canvas2) #Se crea ua miniventana.
    Barra1 = Scrollbar(frame1,orient = "vertical",command = canvas2.yview) #Se crea un scrollbar.
    canvas2.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
    Barra1.pack(side="right",fill="y") #Se empaca el scrollbar.
    canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas2.create_window((0,0),window=frameDeCanvas1,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
    AgregarGoledoresAlNote() #Función para agregar los goleadores del torneo.
    frame2=Frame(nbook2,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame2.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas3 = Canvas(frame2,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas3) #Se crea ua miniventana.
    frameDeCanvas2 = Frame(canvas3) #Se crea ua miniventana.
    Barra2 = Scrollbar(frame2,orient = "vertical",command = canvas3.yview) #Se crea un scrollbar.
    canvas3.configure(yscrollcommand = Barra2.set) #Configura el scrollbar.
    Barra2.pack(side="right",fill="y") #Se empaca el scrollbar.
    canvas3.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas3.create_window((0,0),window=frameDeCanvas2,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas2.bind("<Configure>",Eventos2) #Espera a un evento del scrollbar.
    AgregarAutoGoledoresAlNote() #Función para agregar los autogoleadores del torneo.
    tab1=nbook.add(frame1,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab2=nbook2.add(frame2,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    prin = Image.open("Principal.png") #Imagen de volver.
    Principal = ImageTk.PhotoImage(prin) #Imagen de la ventana principal.
    Button(ventanaGoleadores,image=Principal,command=Volver,relief=FLAT,bg="#134E84").place(x=725,y=350)#Boton para regresar a la ventana principal.
    no = Image.open("error.png") #Imagen.
    error = ImageTk.PhotoImage(no) #Imagen de no. 
    Button(ventanaGoleadores,image=error,command=CerrarVentanaGoledores,relief=FLAT,bg="#134E84").place(x=725,y=170) #Botón de no.
    si = Image.open("exito.png") #Imagen.
    exito = ImageTk.PhotoImage(si) #Imagen de aceptar.
    Button(ventanaGoleadores,image=exito,command=CerrarVentanaGoledores,relief=FLAT,bg="#134E84").place(x=725,y=250) #Botón de aceptar operación.
    ventanaGoleadores.mainloop()#La ventana se mantiene hasta que haya una interación con el usuario.

            
#--------------------
#Ventana Calendario
#--------------------

def VentanaDeCalendario():

    #----------------------------------------------------------------------------
    #Descripción: Cierra la pantalla de calendarios y abre la pantalla principal.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def Regresar():
        ventanaCalendario.destroy()
        ventanaDTorneosFutbol.deiconify()
        
    #-----------------------------------------------
    #Descripción: Cierra la pantalla de calendarios.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def CerrarVentanaCalendario():
        ventanaCalendario.destroy()
        
    #-------------------------------------------------------------------------------
    #Descripción la siguiente función inserta labels en la pantalla de calendarios.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def h():
        def Eventos1(eventos):
            canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)
        global Fechas
        cont=1
        p = Fechas
        Ran = ContarElementos(Fechas)
        for i in range(Ran):
            frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
            frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
            canvas2 = Canvas(frame1,bg="deep sky blue", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
            frameDeCanvas1 = Frame(canvas2) #Se crea ua miniventana.
            canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
            tab1=nbook.add(frame1,text="Fecha "+str(cont),padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
            Barra1 = Scrollbar(frame1,orient = "vertical",command = canvas2.yview) #Se crea un scrollbar.
            canvas2.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
            Barra1.pack(side="right",fill="y") 
            cont=cont+1
            frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
            fila=2
            Label(canvas2,text="Casa",bg="deep sky blue",fg="white",font=("ms sans Serif",15,"bold")).grid(row=1,column=0)
            Label(canvas2,text="Visita",bg="deep sky blue",fg="white",font=("ms sans Serif",15,"bold")).grid(row=1,column=2)
            for j in p[0][1]:
                print(p)
                Label(canvas2,text=j[0],bg="deep sky blue",font=("ms sans Serif",10,"bold")).grid(row=fila,column=0)
                Label(canvas2,text="-",bg="deep sky blue",font=("ms sans Serif",10,"bold")).grid(row=fila,column=1)
                Label(canvas2,text=j[1],bg="deep sky blue",font=("ms sans Serif",10,"bold")).grid(row=fila,column=2)
                fila=fila+1
            p=p[1:]
            
    global ListaDeEquipos,ConfiguracionLista
    ventanaDTorneosFutbol.iconify()
    CargarConfiguración()
    if ConfiguracionLista != []:
        ListaEquipos()
        CrearCombinaciones(ListaDeEquipos)
        TodosLasFechas()
    ventanaCalendario = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaCalendario.title("DTorneo de Fútbol") #Titulo de la ventana.
    ventanaCalendario.geometry("798x400") #Tamaño de la ventana.
    ventanaCalendario.maxsize(798,400) #El tamaño máximo que se puede agrandar la pantalla.
    ventanaCalendario.minsize(798,400) #El tamaño máximo que se puede minimizar la pantalla.
    ventanaCalendario.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    icono = ventanaCalendario.iconbitmap("futbol.ico") #Icono de la ventana.
    canvas = Canvas(ventanaCalendario,width=300, height=200, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    AcercaDe = Image.open("CalendarioJuego.png") #Imagen.
    AcercaDe1 = ImageTk.PhotoImage(AcercaDe) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = AcercaDe1 #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor=NW, image=AcercaDe1) #Se crea el fondo de pantalla.
    nbook = ttk.Notebook(ventanaCalendario,height=220,width=610) #Sea un nootebook dentro de la ventana.
    nbook.place(x=60,y=110) #Coloca el notebook en ese eje.
    if ListaDeEquipos != []:
        h()
    prin = Image.open("Principal.png") #Imagen.
    Principal = ImageTk.PhotoImage(prin) #Imagen de la ventana principal.
    Button(ventanaCalendario,image=Principal,command=Regresar,relief=FLAT,bg="#89D1E2").place(x=725,y=320)#Boton para regresar a la ventana principal.
    no = Image.open("error.png") #Imagen.
    error = ImageTk.PhotoImage(no) #Imagen de error o no.
    Button(ventanaCalendario,command=CerrarVentanaCalendario,image=error,relief=FLAT,bg="#89D1E2").place(x=725,y=170) #Botón de no o cancelar operación.
    si = Image.open("exito.png") #Imagen.
    exito = ImageTk.PhotoImage(si) #Imagen de si o aceptar.
    Button(ventanaCalendario,command=CerrarVentanaCalendario,image=exito,relief=FLAT,bg="#89D1E2").place(x=725,y=250) #Boton de aceptar.
    ventanaCalendario.mainloop()#La ventana espera hasta que el usuario intyeractue en el.

#-------
#Clases
#-------

#---------------------------------------------------------------------------------------------------------------------------------
#Descripción: Se define clase jugador en donde tendrá todas las caracteristicas que se definió en el proyecto para validar datos.
#Entradas: Dos strings y un entero.
#Salidas: Depende del método.
#Restricciones: Sólo strings y enteros.

class Jugador:
    
    def __init__(self,name,pos,num):
        self.nombre = name
        self.posicion = pos
        self.numero = num

    #------------------------------------------------------------------------------
    #Descripción: Se define método ValidoNombre para validar el nombre del jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def VálidoNombre(self):
        name = self.nombre
        if 1<Contar(name)<51:
            return True
        else:
            return False

    #----------------------------------------------------------------------------------
    #Descripción: Se define método VálidoPosicion para validar la posición del jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def VálidoPosicion(self):
        pos = self.posicion
        if 4<Contar(pos)<21:
            return True
        else:
            return False

    #------------------------------------------------------------------------------
    #Descripción: Se define método VálidoNumero para validar el número del jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def VálidoNumero(self):
        num = self.numero
        if 0<num<100:
            return True
        else:
            return False
        
    #----------------------------------------------------------------------------------------------------
    #Descripción: Se define método CrearListaJugador para crear una lista con los tres datos del jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def CrearListaJugador(self):
        return [self.nombre,self.posicion,self.numero]

#---------------------------------------------------------------------------------------------------------------------------------
#Descripción: Se define clase equipo en donde tendrá todas las caracteristicas que se definió en el proyecto para validar datos.
#Entradas: Dos strings y un entero.
#Salidas: Depende del método.
#Restricciones: Sólo strings y enteros.

class Equipo:
    
    def __init__(self,code,name,position):
        self.Codigo = code
        self.Nombre = name
        self.Posicion = position

    #----------------------------------------------------------------------------------------------------
    #Descripción: Se define método CrearListaJugador para crear una lista con los tres datos del equipo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def CrearLista(self):
        return [self.Codigo,self.Nombre,self.Posicion]

    #-----------------------------------------------------------------------------
    #Descripción: Se define método VálidoCodigo para validar el código del equipo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def VálidoCodigo(self):
        code = self.Codigo
        if Contar(code) == 3:
            return True
        else:
            return False

    #-----------------------------------------------------------------------------
    #Descripción: Se define método VálidoNombre para validar el nombre del equipo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def VálidoNombre(self):
        name = self.Nombre
        if 1<Contar(name)<51:
            return True
        else:
            return False

    #----------------------------------------------------------------------------------
    #Descripción: Se define método VálidoPosición para validar la posición del jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def VálidoPosición(self):
        position = self.Posicion
        if 0<position<271:
            return True
        else:
            return False

#---------------------------------------------------------------------------------------------------------------------------------
#Descripción: Se define clase torneo en donde tendrá todas las caracteristicas que se definió en el proyecto para validar datos.
#Entradas: Dos strings y un entero.
#Salidas: Depende del método.
#Restricciones: Sólo strings y enteros.

class torneo:
    
    def __init__(self,nombre,cantidad,clasifican,puntosG,puntosE):
        self.name=nombre
        self.mount=cantidad
        self.clasify=clasifican
        self.pointW=puntosG
        self.pointE=puntosE

    #------------------------------------------------------------------------------------------
    #Descripción: Se define método VálidoPosición para crear una lista con los datos del torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def CrearLista(self):
        return [self.name,self.mount,self.clasify,self.pointW,self.pointE]

    #-------------------------------------------------------------------------------
    #Descripción: Se define método ValidoNombre para validar el nombre del torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def ValidoNombre(self):
        name = self.name
        if 1<Contar(name)<51 and isinstance(name,str):
            return True
        else:
            return False
        
    #---------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método CantidadDeEquipos para validar la cantidad de equipos participantes en un torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def CantidadDeEquipos(self):
        cantidad=self.mount
        if 2<=cantidad and cantidad%2==0:
            return True
        else:
            return False

    #----------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método Clasifican para validar la cantidad de equipos participantes que clasifican en un torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def Clasifican(self):
        clasifican=self.clasify
        participantes =self.mount
        if 1<=clasifican< participantes:
            return True
        else:
            return False

    #-----------------------------------------------------------------------------------------------------------
    #Descripción: Se define método PuntosGanados para validar los puntos ganados por patidos ganados del torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def PuntosGanados(self):
        ganado=self.pointW
        if ganado>=1:
            return True
        else:
            return False

    #----------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método PuntosEmpatados para validar los puntos ganados por partidos empatados del torneo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def PuntosEmpatados(self):
        empatado=self.pointE
        ganado=self.pointW
        if empatado>=1 and ganado>empatado:
            return True
        else:
            return False

#---------------------------------------------------------------------------------------------------------------------------------
#Descripción: Se define clase Jugador Anotador en donde tendrá todas las caracteristicas que se definió en el proyecto para validar datos.
#Entradas: Dos strings y un entero.
#Salidas: Depende del método.
#Restricciones: Sólo strings y enteros.

class JugadorAnotador:
    
    def __init__(self,nom,equi):
        self.nombre = nom
        self.Equipo = equi

    #-------------------------------------------------------------------------------
    #Descripción: Se define método SetNombre para asignarle a la variable el nombre.
    #Entradas: String.
    #Salidas: Ninguno.
    #Restricciones: Sólo strings.
        
    def SetNombre(self,nom):
        self.nombre = nom

    #-------------------------------------------------------------------------------
    #Descripción: Se define método SetEquipo para asignarle a la variable el equipo.
    #Entradas: String.
    #Salidas: Ninguno.
    #Restricciones: Sólo strings.
        
    def SetEquipo(self,equi):
        self.Equipo = equi

    #----------------------------------------------------------------------------
    #Descripción: Se define método GetNombre para retornar la variable el nombre.
    #Entradas: Ninguno.
    #Salidas: Un string.
    #Restricciones: Ninguno.
        
    def GetNombre(self):
        return self.nombre

    #-------------------------------------------------------------------------
    #Descripción: Se define método GetEquipo para retornar la variable equipo.
    #Entradas: Ninguno.
    #Salidas: Un string.
    #Restricciones: Ninguno.
    
    def GetEquipo(self):
        return self.Equipo

    #----------------------------------------------------------------------------
    #Descripción: Se define método VálidoEquipo para validare la variable equipo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def VálidoEquipo(self):
        equipo = self.Equipo
        if ContarString(equipo) ==3:
            return True
        else:
            return False

    #----------------------------------------------------------------------------
    #Descripción: Se define método VálidoNombre para validare la variable equipo.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def VálidoNombre(self):
        name = self.nombre
        if 2 < ContarString(name) < 50:
            return True
        else:
            return False

    #------------------------------------------------------------------------------
    #Descripción: Se define método cuenta la cantidad de letras que tiene un string.
    #Entradas: String.
    #Salidas: Ninguno.
    #Restricciones: Sólo strings.
        
    def ContarString(string):
        if string == "":
            return 0
        else:
            return 1 + ContarString(string[1:])

#----------------------------------------------------------------------------------------------
#Descripción: Se define clase Lista en donde tendrá metodos de busqueda de elementos en listas.
#Entradas: Dos strings y un entero.
#Salidas: Depende del método.
#Restricciones: Sólo strings y enteros.

class ListaEsta:
    
    def __init__(self,lista1):
        self.lista=lista1


    #-------------------------------------------------------------------------------------------------------
    #Descripción: Se define método EstaListaEnCom para saber si una lista esta en la variable global fechas.
    #Entradas: Ninguno.
    #Salidas: Un valor booleano.
    #Restricciones: Ninguno.
        
    def EstaListaEnCom(self):
        l=self.lista
        global Fechas
        for i in Fechas:
            for j in i[1]:
                if j == l :
                    return True
        return False

    #--------------------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método EstaEnResultadosDePartidos para saber si una lista esta en la variable global ResultadosDePartidos.
    #Entradas: Ninguno.
    #Salidas: Un valor booleano.
    #Restricciones: Ninguno.
    
    def EstaEnResultadosDePartidos(self):
        global ResultadosDePartidos
        casa=self.lista[0]
        visita=self.lista[1]
        for i in ResultadosDePartidos:
            if i[0] == casa and i[2] == visita:
                return True
        return False

#------------------------------------------------------------------------------
#Descripción: La siguiente clase es sobre la posición en escala de los equipos.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.

class PosicionEscalon:
    
    def __init__(self,lista): #recibe la lista de la configuracion de [5] 
        self.configuracion = lista

    #-------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método SoloPosicion y retorna una lista con solo las posiciones de los equipos en la escala.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno.

    def SoloPosicion(self):
        l = self.configuracion[5]
        n = []
        for i in l:
            n = n + [i[2]]
        return n

    #------------------------------------------------------------------------------------------
    #Descripción: Se define método OrdenadoMayor y retorna una lista ordenado de mayor a menor.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno.

    def OrdenadoMayor(self):
        num = self.SoloPosicion()
        n = []
        while num != []:
            n = [max(num)] + n
            num.remove(max(num))
        return n

    #------------------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método Ordenado y retorna una lista ordenado de mayor a menor, es complemento del metodo anterior.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno.

    def Ordenado(self):
        numeros = self.OrdenadoMayor()
        lista = self.configuracion[5]
        n = []
        for i in numeros:
            for j in lista:
                if i == j[2]:
                    n=n+[j]
        return n

#----------------------------------------------------------------------------------------------------------------------------
#Descrpción: La siguiente clase es para definir si dos lista de equipos con los puntos tiene las mismas diferencias de goles.
#Entradas: Ninguno.
#Salidas: Ninguna
#Restricciones: Ninguno.
    
class SonIguales:#[[puntos diferencia,puntos],[puntos diferencia,puntos]]
    
    def __init__(self,lis):
        self.lista = lis

    #-----------------------------------------------------------------------------------------------------------
    #Descripción: Se define método SoloPuntosDiferencias y retorna una lista con solo los puntos de diferencias.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno.        
        
    def SoloPuntosDiferencias(self):
        lis = self.lista
        nuevo = []
        for i in lis:
            nuevo=nuevo+[int(i[7])]
        return nuevo

    #----------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método OrdenarPuntosDiferencias y retorna una lista ordenada con solo los puntos de diferencias.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno. 
    
    def OrdenarPuntosDiferencias(self):
        l = self.SoloPuntosDiferencias()
        n = []
        while l != []:
            n = n + [max(l)]
            l.remove(max(l))
        return n

    #---------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método OrdenadoPorPuntosDiferencias y retorna una lista ordenada con solo los puntos de diferencias es complemento del método anterior.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno. 

    def OrdenadoPorPuntosDiferencias(self):
        puntos = self.OrdenarPuntosDiferencias()
        lis = self.lista
        n = []
        for i in puntos:
            for j in lis:
                if i == int(j[7]):
                    n=n+[j]
                    continue
        return n

#-------------------------------------------------------------------------------------------------------------------
#Descripción: Se describe la clase puntos, en donde se tendrá diversos metodos para sacar los puntos de los equipos.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

class PuntosEquipos:
    
    def __init__(self,team):
        self.equipo=team 

    #----------------------------------------------------------------------------------------------------
    #Descripción: Se define método PartidosJugados y retorna la cantidad de partidos jugados de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 
    
    def PartidosJugados(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team or i[2] == team:
                cont=cont+1
        return cont

    #-------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método PartidosGanados y retorna un entero con la cantidad de partidos ganados de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def PartidosGanados(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team:
                if i[1]>i[3]:
                    cont=cont+1
                    continue
                else:
                    continue
            if i[2] == team:
                if i[3]>i[1]:
                    cont=cont+1
                    continue
                else:
                    continue
            else:
                continue
        return cont

    #-----------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método PartidosEmpatados y retorna un entero con la cantidad de partidos empatados de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def PartidosEmpatados(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team:
                if i[1] == i[3]:
                    cont=cont+1
                    continue
                else:
                    continue
            if i[2] == team:
                if i[3] == i[1]:
                    cont=cont+1
                    continue
                else:
                    continue
            else:
                continue
        return cont

    #---------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método PartidosPerdidos y retorna un entero con la cantidad de partidos perdidos de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def PartidosPerdidos(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team:
                if i[1] < i[3]:
                    cont=cont+1
                    continue
                else:
                    continue
            if i[2] == team:
                if i[3] < i[1]:
                    cont=cont+1
                    continue
                else:
                    continue
            else:
                continue
        return cont

    #-----------------------------------------------------------------------------------------------------------
    #Descripción: Se define método GolesFavor y retorna un entero con la cantidad de goles a favor de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def GolesFavor(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team:
                cont=cont+i[1]
                continue
            if i[2] == team:
                cont=cont+i[3]
                continue
            else:
                continue
        return cont

    #--------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método GolesContra y retorna un entero con la cantidad de goles en contra de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def GolesContra(self):
        global ResultadosDePartidos
        team=self.equipo[1]
        cont=0
        for i in ResultadosDePartidos:
            if i[0] == team:
                cont=cont+i[3]
                continue
            if i[2] == team:
                cont=cont+i[1]
                continue
            else:
                continue
        return cont

    #----------------------------------------------------------------------------------------------------------------------
    #Descripción: Se define método GolesDiferencia y retorna un string con la cantidad de goles de diferencia de un equipo.
    #Entradas: Ninguno.
    #Salidas: Un string.
    #Restricciones: Ninguno.

    def GolesDiferencia(self):
        Diferencia = self.GolesFavor()-self.GolesContra()
        if Diferencia > 0:
            return "+" + str(Diferencia)
        else:
            return str(Diferencia)
        
    #-------------------------------------------------------------------------------------------------------
    #Descripción: Se define método Puntos y retorna un entero con la cantidad de puntos que tiene un equipo.
    #Entradas: Ninguno.
    #Salidas: Un entero.
    #Restricciones: Ninguno. 

    def Puntos(self):
        global ConfiguracionLista
        PtsG = ConfiguracionLista[3]
        PtsE = ConfiguracionLista[4]
        TotalG = self.PartidosGanados()*PtsG
        TotalE = self.PartidosEmpatados()*PtsE
        Total = TotalG+TotalE
        return Total

    #----------------------------------------------------------------------------------------------------------
    #Descripción: Se define método CrearListaTeam y retorna una lista con los datos de las variables iniciados.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno. 

    def CrearListaTeam(self):
        team = self.equipo
        return [team[0],self.PartidosJugados(),self.PartidosGanados(),self.PartidosEmpatados(),self.PartidosPerdidos(),self.GolesFavor(),self.GolesContra(),self.GolesDiferencia(),self.Puntos()]
    
#--------------------------------
#Ventana de Consultar Resultados
#--------------------------------

def VentanaResultadosConsultar():

    #----------------------------------------------------------------------------------------------------------
    #Descripción: Se crea la función para eliminar un resultado de la lista de resultados.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
    
    def EliminarDefinitivo():
        if EstaEnResultados() == True:
            return EliminarResultado()
        else:
            return messagebox.showerror("Error","No se encuentra este resultado")

    #--------------------------------------------------------------------------------------------
    #Descripción: Se crea la función para ver si esta un resultado de la lista de resultados.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno. 

    def EstaEnResultados():
        c=Casa2.get()
        v=Visita2.get()
        global ResultadosDePartidos
        Resul = ResultadosDePartidos
        n=[]
        for i in Resul:
            if i[0] == c and i[2] == v:
                return True
        return False

    #-------------------------------------------------------------------------------------
    #Descripción: Se crea la función para eliminar un resultado de la lista de resultados.
    #Entradas: Ninguno.
    #Salidas: Una lista.
    #Restricciones: Ninguno. 

    def EliminarResultado():
        c=Casa2.get()
        v=Visita2.get()
        global ResultadosDePartidos
        Resul = ResultadosDePartidos
        n=[]
        for i in Resul:
            if i[0] == c and i[2] == v:
                continue
            else:
                n=n+[i]
        ResultadosDePartidos = n
        SobreescribeResultados(ResultadosDePartidos)
        return messagebox.showinfo("Info","Eliminado con éxito")
        
    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas3.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
    
    def Eventos3(eventos):
        canvas3.configure(scrollregion=canvas3.bbox("all"),width=250,height=280)

    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
        
    def Eventos1(eventos):
        canvas.configure(scrollregion=canvas.bbox("all"),width=250,height=280)

    #-------------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels de partidos al nootebook.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
        
    def AgregarResultadosAlNote():
        global ResultadosDePartidos#Utiliza la variable global
        if ResultadosDePartidos == []:
            return
        fila=2
        Label(frameDeCanvas1,fg="white",text="Casa",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=1)
        Label(frameDeCanvas1,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=2)
        Label(frameDeCanvas1,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=3)
        Label(frameDeCanvas1,fg="white",text="Visita",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=4)
        for i in ResultadosDePartidos:
            Label(frameDeCanvas1,fg="black",text=i[0],font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas1,fg="black",text=i[1],font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas1,fg="black",text=i[3],font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
            Label(frameDeCanvas1,fg="black",text=i[2],font=("ms sans Serif",9,"bold")).grid(row=fila,column=4)
            fila=fila+1


    #---------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es una funcion es para limpiar la pantalla de jugadores consultar de la pantalla principal.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
                       
    def Clean():
        fila=2
        for i in range(100):
            Label(frameDeCanvas3,bg="white",height=1,width=8).grid(row=fila,column=1)
            Label(frameDeCanvas3,bg="white",height=1,width=8).grid(row=fila,column=2)
            Label(frameDeCanvas3,bg="white",height=1,width=8).grid(row=fila,column=3)
            Label(frameDeCanvas3,bg="white",height=1,width=8).grid(row=fila,column=4)

            fila=fila+1

    #--------------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels de jugadores al nootebook.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def AgregarJugadorResulNote():
        global ResultadosDePartidos#Utiliza la variable global
        Clean()
        H = Casa.get()
        V = Visita.get()
        if H == "" or V == "":
            return messagebox.showerror("Error","Por favor escriba los códigos del equipo que desea consultar")
        if Esta2(H,V,ResultadosDePartidos) == False:
            return messagebox.showerror("Error","No se encuentra registrado este partido "+str(H)+"-"+str(V))
        else:
            l=Encontrar(H,V)
            fila=2
            Label(frameDeCanvas1,fg="white",text="Jugadores",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=0,column=1)
            Label(frameDeCanvas1,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=0,column=2)
            Label(frameDeCanvas1,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=0,column=3)
            Label(frameDeCanvas1,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=0,column=4)
            Label(frameDeCanvas3,fg="white",text="Nombre",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=1)
            Label(frameDeCanvas3,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=2)
            Label(frameDeCanvas3,fg="white",text="-",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=3)
            Label(frameDeCanvas3,fg="white",text="País",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=1,column=4)
            for i in l:
                Label(frameDeCanvas3,fg="black",text=i[0],font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
                Label(frameDeCanvas3,fg="black",text="--",font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
                Label(frameDeCanvas3,fg="black",text="--",font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
                Label(frameDeCanvas3,fg="black",text=i[1],font=("ms sans Serif",9,"bold")).grid(row=fila,column=4)
                fila=fila+1

    #---------------------------------------------------------------------------
    #Descripción: La siguiente fucnión cierra la ventana de consulta resultados.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def CerrarVentanaResultadosConsultar():
        ventanaResultadosConsultar.withdraw()
    
    ventanaResultadosConsultar = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaResultadosConsultar.title("Torneos de fútbol") #Titulo de la ventana.
    icono = ventanaResultadosConsultar.iconbitmap("futbol.ico") #Icono de la ventana.
    ventanaResultadosConsultar.geometry("310x550") #Tamano de la ventana.
    ventanaResultadosConsultar.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaResultadosConsultar.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no = Image.open("error.png") #Imagen de no.
    error = ImageTk.PhotoImage(no)
    si = Image.open("exito.png") #Imagen de si.
    exito = ImageTk.PhotoImage(si)
    lupa = Image.open("lupa.png") #Imagen de buscar.
    buscar = ImageTk.PhotoImage(lupa)
    balon = Image.open("balon.png") #Imagen de goleadores.
    bola = ImageTk.PhotoImage(balon)
    patio = Image.open("cancha.png") #Imagen de consultar partidos.
    cancha = ImageTk.PhotoImage(patio) 
    EtiquetaContacto = Label(ventanaResultadosConsultar,bg = "light sea green",width = 50,height = 4).place(x = 0,y = 1) #Se le asigna una etiqueta a la variable.
    TextoContacto = Label(ventanaResultadosConsultar,text = "Consultar resultados",fg = "white",relief = FLAT,bg = "light sea green",font=("ms sans Serif",11,"bold")).place(x=7,y=25) #Se le asigna una etiqueta a la variable.
    botonSi = Button(ventanaResultadosConsultar,image=exito,command=CerrarVentanaResultadosConsultar,bg="RoyalBlue4",relief=FLAT).place(x=70,y=480) #Se le asigna un boton a una variable.
    botonNo = Button(ventanaResultadosConsultar,command=CerrarVentanaResultadosConsultar,image=error,bg="RoyalBlue4",relief=FLAT).place(x=200,y=480) #Se le asigna un boton a una variable.
    nbook = ttk.Notebook(ventanaResultadosConsultar,height=306,width=290) #Sea un nootebook dentro de la ventana.
    nbook.place(x=7,y=90) #Ubica el nootebook en esa posición x,y.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas = Canvas(frame1,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas) #Se crea ua miniventana.
    frameDeCanvas1=Frame(canvas) #Se crea una ventana dentro de una ventana dentro de una ventana.
    Barra1 = Scrollbar(frame1,orient = "vertical",command = canvas.yview) #Se crea un scrollbar.
    canvas.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
    Barra1.pack(side="right",fill="y") #El scrollbar se empaca y lo ubica en y.
    canvas.pack(side="left") #El canvas se empaca.
    canvas.create_window((0,0),window=frameDeCanvas1,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
    frame2=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame2.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas1 = Canvas(frame2,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla1 = ttk.Frame(canvas1) #Se crea ua miniventana.
    canvas1.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    frame3=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame3.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas3 = Canvas(frame3,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla3 = ttk.Frame(canvas3) #Se crea ua miniventana.
    frameDeCanvas3=Frame(canvas3) #Se crea una ventana dentro de una ventana dentro de una ventana.
    Barra3 = Scrollbar(frame3,orient = "vertical",command = canvas3.yview) #Se crea un scrollbar.
    canvas3.configure(yscrollcommand = Barra3.set) #Configura el scrollbar.
    Barra3.pack(side="right",fill="y") #El scrollbar se empaca y lo ubica en y.
    canvas3.pack(side="left") #El canvas se empaca.
    canvas3.create_window((0,0),window=frameDeCanvas3,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas3.bind("<Configure>",Eventos3) #Configura el scrollbar con respecto a los objectos que tenga.
    EtiquetaEliminar = Label(canvas1,bg="#134E84",text="Digite el código de los equipos:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaCasa = Label(canvas1,bg="#134E84",text="Casa",fg="white",font=("ms sans Serif",9,"bold")).place(x=50,y=100) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaVisita = Label(canvas1,bg="#134E84",text="Visita",fg="white",font=("ms sans Serif",9,"bold")).place(x=170,y=100) #Se le asigna una etiqueta de texto a la variable.
    Casa = StringVar() #Variable local string del equipo en casa.
    EspacioConsu1 = Entry(canvas1,textvariable=Casa,width=10).place(x=40,y=150) #Se le asigna un campo de texto a la variable.
    Visita = StringVar() #Variable local string del equipo en visita.
    EspacioConsu = Entry(canvas1,textvariable=Visita,width=10).place(x=160,y=150) #Se le asigna un campo de texto a la variable.
    BotonEliminar = Button(canvas1,text="Consultar",command=AgregarJugadorResulNote,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=200)#Se le asigna un boton a la variable.
    frame4=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame4.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas4 = Canvas(frame4,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla4 = ttk.Frame(canvas4) #Se crea ua miniventana.
    canvas4.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    EtiquetaEliminar2 = Label(canvas4,bg="#134E84",text="Digite el código de los equipos:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaCasa2 = Label(canvas4,bg="#134E84",text="Casa",fg="white",font=("ms sans Serif",9,"bold")).place(x=50,y=100) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaVisita2 = Label(canvas4,bg="#134E84",text="Visita",fg="white",font=("ms sans Serif",9,"bold")).place(x=170,y=100) #Se le asigna una etiqueta de texto a la variable.
    Casa2 = StringVar() #Variable local string del equipo en casa.
    EspacioConsu2 = Entry(canvas4,textvariable=Casa2,width=10).place(x=40,y=150) #Se le asigna un campo de texto a la variable.
    Visita2 = StringVar() #Variable local string del equipo en visita.
    EspacioConsu2 = Entry(canvas4,textvariable=Visita2,width=10).place(x=160,y=150) #Se le asigna un campo de texto a la variable.
    BotonEliminar2 = Button(canvas4,text="Eliminar",command=EliminarDefinitivo,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=200)#Se le asigna un boton a la variable.
    modificar1 = Image.open("modificar.png") #Imagen. 
    modificar = ImageTk.PhotoImage(modificar1) #Imagen de modificar jugador.
    tab1=nbook.add(frame1,image=cancha,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab2=nbook.add(frame2,image=buscar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab3=nbook.add(frame3,image=bola,padding = 10) #Se le agrega al cuaderno una etiqueta y
    tab4=nbook.add(frame4,image=modificar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de modificar.
    AgregarResultadosAlNote() #Llama la función para insertar labels de los resultados de los partidos.
    ventanaResultadosConsultar.mainloop() #Espera hasta que el usuario interactué en el.

#--------------------------------
#Ventana de Registrar resultados
#--------------------------------

def VentanaRegistrarResultados():

    #-------------------------------------------------------------------------------------------------        
    #Descripción: La siguiente funcion valida los datos de entradas de la pantalla de registrar datos.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def VálidarDatos():
        global JugadoresAnotadores,ResultadosDePartidos
        player = Jugador.get()
        team = Equipo.get()
        if Casa.get() == "":
            return messagebox.showerror("Error","Por favor seleccione la cantidad de goles")
        if Visita.get() == "":
            return messagebox.showerror("Error","Por favor seleccione la cantidad de goles")
        if CasaCode.get() == "":
            return messagebox.showerror("Error","Por favor escriba el código del equipo")
        if VisitaCode.get() == "":
            return messagebox.showerror("Error","Por favor escriba el código del equipo")
        House=int(Casa.get())
        Code1=CasaCode.get()
        Visita2=int(Visita.get())
        Code2=VisitaCode.get()
        Objecto=JugadorAnotador(player,team)
        print(House,Code1,Visita2,Code2)
        if Objecto.VálidoEquipo() == False:
            return messagebox.showerror("Error","El código del equipo debe ser de tres letras")
        if Objecto.VálidoNombre() == False:
            return messagebox.showerror("Error","El nombre del jugador deb tener entre 1 a 50 letras")
        if ContarGoles(team,JugadoresAnotadores) == House and team == Code1:
            return messagebox.showerror("Error","Máximo cantidad de goles registrados")
        if ContarGoles(team,JugadoresAnotadores) == Visita2 and team == Code2:
            return messagebox.showerror("Error","Máximo cantidad de goles registrados")
        else:
            JugadoresAnotadores = JugadoresAnotadores + [[player,team]]
            print(JugadoresAnotadores)
            return
    
    #-----------------------------------------------------------------------------------------------        
    #Descripción: La siguiente funcion valida los datos de entradas cuando se registra un resultado.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def ValidarDatosDeEntradas():
        global JugadoresAnotadores,ResultadosDePartidos
        if Casa.get() == "":
            return messagebox.showerror("Error","Por favor seleccione la cantidad de goles")
        if Visita.get() == "":
            return messagebox.showerror("Error","Por favor seleccione la cantidad de goles")
        if CasaCode.get() == "":
            return messagebox.showerror("Error","Por favor escriba el código del equipo")
        if VisitaCode.get() == "":
            return messagebox.showerror("Error","Por favor escriba el código del equipo")
        House=int(Casa.get())
        Code1=CasaCode.get()
        Visita2=int(Visita.get())
        Code2=VisitaCode.get()
        total=House+Visita2
        lista = [Code1,Code2]
        Obj = ListaEsta(lista)
        if Obj.EstaEnResultadosDePartidos() == True:
            return messagebox.showerror("Error","Este partido ya se encuentra registrado")
        if CantidaDeJugadores() != total:
            print(total)
            return messagebox.showerror("Error","La cantidad de goles no coincide con los jugadores agregados")
        Objecto=JugadorAnotador("pp",Code1)
        Objecto2=JugadorAnotador("pp",Code2)
        if Objecto.VálidoEquipo() == False:
            return messagebox.showerror("Error","El código del equipo debe ser de tres letras")
        if Objecto2.VálidoEquipo() == False:
            return messagebox.showerror("Error","El código del equipo debe ser de tres letras")
        else:
            ResultadosDePartidos = ResultadosDePartidos + [[Code1,int(House),Code2,int(Visita2),JugadoresAnotadores]]
            JugadoresAnotadores=[]
            print(ResultadosDePartidos)
            SobreescribeResul()
            messagebox.showinfo("Info","Registrado con exito")
            ventanaResultados.destroy()
            return

    #-------------------------------------------------------------------        
    #Descripción: La siguiente funcion cierra la pantalla de resultados.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
            
    def CerrarVentana():
        ventanaResultados.destroy()
        
    #-----------------------------------------------------------------        
    #Descripción: La siguiente funcion vuelve a la pantalla principal.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def Volver():
        global JugadoresAnotadores
        JugadoresAnotadores = []
        ventanaDTorneosFutbol.deiconify()
        ventanaResultados.destroy()

    ventanaDTorneosFutbol.iconify()
    CargarResultados() #Usa la función para cargar los datos a la variable global.
    ventanaResultados = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaResultados.title("DTorneo de Fútbol") #Titulo de la ventana.
    ventanaResultados.geometry("795x460") #Tamano de la ventana.
    ventanaResultados.maxsize(795,460) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaResultados.minsize(795,460) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaResultados.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    icono = ventanaResultados.iconbitmap("futbol.ico") #Icono de la ventana.
    canvas = Canvas(ventanaResultados,width=300, height=200, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    Registrar = Image.open("Registrar.png") #Imagen de registrar.
    Registrar1 = ImageTk.PhotoImage(Registrar) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = Registrar1 #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor=NW, image=Registrar1) #Crea el fondo de pantalla.
    mas1 = Image.open("mas.png") #Imagen de agregar.
    mas = ImageTk.PhotoImage(mas1) #Imagen de agregar.
    Button(ventanaResultados,command=VálidarDatos,image=mas,relief=FLAT,bg="#2FA4A4").place(x=730,y=350) #Botón de agregar.
    no = Image.open("error.png") #Imagen no o cancelar operación.
    error = ImageTk.PhotoImage(no) #Imagen de no creado.
    Button(ventanaResultados,command=CerrarVentana,image=error,relief=FLAT,bg="#2FA4A4").place(x=730,y=150) #Botón de cerrar ventana.
    si = Image.open("exito.png") #Imagen de si o aceptar.
    exito = ImageTk.PhotoImage(si) #Imagen de aceptar.
    Button(ventanaResultados,command=ValidarDatosDeEntradas,image=exito,relief=FLAT,bg="#2FA4A4").place(x=730,y=250) #Botón de aceptar y validación de datos.
    prin = Image.open("Principal.png") #Imagen de principal.
    Principal = ImageTk.PhotoImage(prin) #Imagen de principal.
    Button(ventanaResultados,image=Principal,command=Volver,relief=FLAT,bg="#2FA4A4").place(x=730,y=300)#Crea el botón para regresar la pantalla principal.
    Lupa = Image.open("BuscarResultados.png") #Imagen.
    Encontrado = ImageTk.PhotoImage(Lupa) #Imagen de consultar resultados.
    Button(ventanaResultados,image=Encontrado,command=VentanaResultadosConsultar,relief=FLAT,bg="#2FA4A4").place(x=730,y=400)#Botón de consultar resultados.
    CasaCode=StringVar() #Variable local de casa tipo string.
    Entry(ventanaResultados,textvariable=CasaCode,width=18,bg="#104A57",fg="white",relief=FLAT).place(x=90,y=215) #Espacio para acceder a la variable de casa.
    VisitaCode=StringVar()#Variable local de visita tipo string.
    Entry(ventanaResultados,textvariable=VisitaCode,width=18,bg="#104A57",fg="white",relief=FLAT).place(x=90,y=360) #Espacio para acceder a la variable de visita.
    Jugador=StringVar()#Variable local de jugador tipo string.
    Equipo=StringVar()#Variable local de equipo tipo string.
    Entry(ventanaResultados,textvariable=Jugador,bg="#104A57",fg="white",width=25,relief=FLAT).place(x=378,y=323) #Espacio para acceder a la variable de jugador.
    Entry(ventanaResultados,textvariable=Equipo,bg="#104A57",fg="white",width=7,relief=FLAT).place(x=605,y=323) #Espacio para acceder a la variable de Equipo.
    Casa = StringVar() #Se le asigna el valor de string a una variable.
    OptionPosicion = ttk.Combobox(ventanaResultados,textvariable = Casa,values =[0]+imprimir(100) ,width=3).place(x=240,y=215) #Se le asigna a una variable el option boton
    Visita = StringVar() #Se le asigna el valor de string a una variable.
    OptionPosicion = ttk.Combobox(ventanaResultados,textvariable = Visita,values =[0]+imprimir(100) ,width=3).place(x=240,y=357) #Se le asigna a una variable el option boton
    ventanaResultados.mainloop()#La ventana espera una acción del usuario

#-----------------------------------
#Ventana de Consultar Configuración
#-----------------------------------

def ConsultarConfiguracion():

    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas3.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos2(eventos):
        canvas3.configure(scrollregion=canvas3.bbox("all"),width=250,height=280)


    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos1(eventos):
        canvas2.configure(scrollregion=canvas.bbox("all"),width=250,height=280)

    #----------------------------------------------------------------------------------------
    #Descripción: La siguiente función carga la configuración almacenada a la variable global.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def CargarConfiguración():
        global ConfiguracionLista
        contenido = leerTodo("configuracion_torneos_de_futbol.txt")
        if contenido == "" :
            ConfiguracionLista  = []
            return contenido
        else:
            ConfiguracionLista  = eval(contenido)
            return eval(contenido)


    #-------------------------------------------------------------------------------------
    #Descripción: La siguiente función borra la configuración guardada en el archivo .txt.
    #Entradas: Ninguna.
    #Salidas: Cuadro de texto.
    #Restricciones: Ninguna.

    def BorrarConfiguracion ():
        global ConfiguracionLista
        if ConfiguracionLista != []:
            archivo = open ("configuracion_torneos_de_futbol.txt", "w")  #Abre el archivo y la operación es sólo escritura.
            archivo.close() #Se cierra el archivo.
            ConfiguracionLista=[]
            ventanaConsultarConfiguracion.destroy()
            return messagebox.showinfo("Info","Configuración borrada con exito")
        else:
            return messagebox.showerror("Error","No se encuentra ninguna configuración")

    #----------------------------------------------------------------------------
    #Descripción: La siguiente función agrega equipos al notebook de la pantalla.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarEquiposAlNote():
        global ConfiguracionLista #Utiliza la variable global
        fila=2
        color=["light blue","cadet blue","khaki","beige"]
        Label(frameDeCanvas1,fg="black",text="Equipos",bg="cadet blue",width=10,font=("ms sans Serif",10,"bold")).grid(row=0,column=1)
        Label(frameDeCanvas1,fg="white",text="Código",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=1)
        Label(frameDeCanvas1,fg="white",text="País",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=2)
        Label(frameDeCanvas1,fg="white",text="Posición",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=3)
        for i in ConfiguracionLista[5]:
            Label(frameDeCanvas1,fg="black",text=i[0],font=("ms sans Serif",10,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas1,fg="black",text=i[1],font=("ms sans Serif",10,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas1,fg="black",text=i[2],font=("ms sans Serif",10,"bold")).grid(row=fila,column=3)
            fila=fila+1

    #---------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es una funcion es para limpiar la pantalla de jugadores consultar de la pantalla principal.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
                       
    def Clean():
        fila=2
        for i in range(100):
            Label(frameDeCanvas2,bg="white",height=2,width=10).grid(row=fila,column=1)
            Label(frameDeCanvas2,bg="white",height=2,width=10).grid(row=fila,column=2)
            Label(frameDeCanvas2,bg="white",height=2,width=10).grid(row=fila,column=3)
            fila=fila+1
            
    #------------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función retorna una lista con los jugadores que pertenece a ese equipo que se desea consultar.
    #Entradas: Un string.
    #Salidas: Ninguna.
    #Restricciones: Sólo strings.
            
    def JugadoresConsultar(equipo):
        global ConfiguracionLista #Utiliza la variable global

        for i in ConfiguracionLista[5]:
            if i[0] == equipo:
                return i[3]

    #------------------------------------------------------------------------------------------
    #Descripción: La siguiente función agrega jugadores al notebook en la sección de jugadores.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def AgregarJugadoresAlNote():
        global ConfiguracionLista #Utiliza la variable global
        Clean()
        nombre=Equipito.get()
        if nombre == "":
            return messagebox.showerror("Error","Digite el nombre que desea consultar los jugadores")
        Lista = JugadoresConsultar(nombre)
        fila=2
        Label(frameDeCanvas2,fg="black",text="Jugadores",bg="cadet blue",width=10,font=("ms sans Serif",10,"bold")).grid(row=0,column=1)
        Label(frameDeCanvas2,fg="white",text="Nombre",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=1)
        Label(frameDeCanvas2,fg="white",text="Posicion",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=2)
        Label(frameDeCanvas2,fg="white",text="Número",bg="#2FA4A4",width=10,font=("ms sans Serif",10,"bold")).grid(row=1,column=3)
        for i in Lista:
            Label(frameDeCanvas2,fg="black",text=i[0],font=("ms sans Serif",10,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas2,fg="black",text=i[1],font=("ms sans Serif",10,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas2,fg="black",text=i[2],font=("ms sans Serif",10,"bold")).grid(row=fila,column=3)
            fila=fila+1
            
    #-----------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana configuración.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def CerrarVentanaConfiguracion():
        ventanaConsultarConfiguracion.destroy()

    #-------------------------------------------------------------
    #Descripción: La siguiente función abre la pantalla principal.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def VentanaPrincipal():
        ventanaDTorneosFutbol.deiconify()
        ventanaConsultarConfiguracion.destroy()

    CargarConfiguración()    
    global ConfiguracionLista
    if ConfiguracionLista == []:
        return messagebox.showinfo("Info","Primero debes configurar el torneo")
    ventanaDTorneosFutbol.iconify()
    ventanaConsultarConfiguracion = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaConsultarConfiguracion.title("DTorneos de Futbol") #Titulo de la ventana.
    canvas = Canvas(ventanaConsultarConfiguracion,width=300, height=210, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    icono = ventanaConsultarConfiguracion.iconbitmap("futbol.ico") #Icono de la ventana.
    ventanaConsultarConfiguracion.geometry("795x469") #Tamano de la ventana.
    ventanaConsultarConfiguracion.maxsize(795,469) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaConsultarConfiguracion.minsize(795,469) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    canvas.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    AcercaDe = Image.open("ConsultarConfiguracion.png") #Imagen.
    AcercaDe1 = ImageTk.PhotoImage(AcercaDe) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = AcercaDe1 #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor=NW, image=AcercaDe1) #Crea la imagen en la pantalla.
    nbook = ttk.Notebook(ventanaConsultarConfiguracion,height=140,width=350) #Sea crea un nootebook dentro de la ventana.
    nbook.place(x=315,y=260) #Ubica el notebook en ese eje.
    bola = Image.open("bolita.png") #Imagen.
    bola2 = ImageTk.PhotoImage(bola) #Imagen de bola.
    chema = Image.open("camisa.png") #Imagen. 
    camisa = ImageTk.PhotoImage(chema) #Imagen de numero de camisa.
    lupita = Image.open("lupa.png") #Imagen.
    lupa = ImageTk.PhotoImage(lupita) #Imagen de buscar.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas2 = Canvas(frame1, borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    frameDeCanvas1 = Frame(canvas2) #Se crea una ventana dentro del canvas.
    Barra1 = Scrollbar(frame1,orient = "vertical",command = canvas2.yview) #Se crea un scrollbar.
    canvas2.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
    Barra1.pack(side="right",fill="y") #Empaca el scrollbar, el primero. 
    canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas2.create_window((0,0),window = frameDeCanvas1,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas1.bind("<Configure>",Eventos1) #En la ventana del canvas espera hasta que ocurra un evento y llama a la función EventosConsultar.
    tab1=nbook.add(frame1,image=bola2,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    frame3=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame3.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas4 = Canvas(frame3,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla2 = ttk.Frame(canvas4) #Se crea ua miniventana.
    tab3=nbook.add(frame3,image=lupa,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    frameDeCanvas3 = Frame(canvas4) #Se crea una ventana dentro del canvas.
    canvas4.pack(side = 'left', fill = 'both', expand=True) #Empaca la ventana.
    frame2=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame2.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas3 = Canvas(frame2,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla1 = ttk.Frame(canvas3) #Se crea ua miniventana.
    tab2=nbook.add(frame2,image=camisa,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    frameDeCanvas2 = Frame(canvas3) #Se crea una ventana dentro del canvas.
    Barra2 = Scrollbar(frame2,orient = "vertical",command = canvas3.yview) #Se crea un scrollbar.
    canvas3.configure(yscrollcommand = Barra2.set) #Configura el scrollbar.
    Barra2.pack(side="right",fill="y") #Empaca el scrollbar.
    canvas3.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas3.create_window((0,0),window = frameDeCanvas2,anchor = 'nw') #Se crea una ventana en el canvas.
    frameDeCanvas2.bind("<Configure>",Eventos2) #Configura el scrollbar con los eventos que se dan cuando se agregan elementos.
    no = Image.open("error.png") #Imagen.
    error = ImageTk.PhotoImage(no) #Imagen de no o cancelar.
    Button(ventanaConsultarConfiguracion,command=CerrarVentanaConfiguracion,image=error,relief=FLAT,bg="#2FA4A4").place(x=740,y=150)#
    si = Image.open("exito.png") #Imagen.
    exito = ImageTk.PhotoImage(si) #Imagen de aceptar o si.
    Button(ventanaConsultarConfiguracion,command=CerrarVentanaConfiguracion,image=exito,relief=FLAT,bg="#2FA4A4").place(x=740,y=230) #Boton de cerrar la ventana.
    bo = Image.open("Borrador.png") #Imagen.
    Borrador = ImageTk.PhotoImage(bo) #Imagen de borrador. 
    Button(ventanaConsultarConfiguracion,command=BorrarConfiguracion,image=Borrador,relief=FLAT,bg="#2FA4A4").place(x=740,y=300) #Boton para borrar la configuracion.
    prin = Image.open("Principal.png") #Imagen.
    Principal = ImageTk.PhotoImage(prin) #Imagen de la ventana principal.
    Button(ventanaConsultarConfiguracion,command=VentanaPrincipal,image=Principal,relief=FLAT,bg="#2FA4A4").place(x=740,y=350)#Boton para regresar a la ventana principal.
    ajuste = Image.open("ajustes.png") #Imagen.
    ajustes = ImageTk.PhotoImage(ajuste) #Imagen de ajustes.
    Button(ventanaConsultarConfiguracion,command=VentanaConsultaConfiguracion,image=ajustes,relief=FLAT,bg="#2FA4A4").place(x=740,y=400)#Boton para consulttar configuración.
    Equipito = StringVar() #Variable local string.
    Label(frame3,relief=FLAT,text="Digite el código del país que desea consultar los jugadores",fg="white",bg="#2FA4A4").place(x=10,y=10)#Label para solicitar la escritura de codigo del equipo.
    Entry(frame3,relief=FLAT,textvariable=Equipito,fg="white",bg="#104A57").place(x=110,y=50) #Este entry se usa para escribir el equipo.
    Button(frame3,text="Consultar",command=AgregarJugadoresAlNote,relief=FLAT,fg="white",bg="#104A57").place(x=140,y=80) #Boton para consultar los jugores configurados.
    if ConfiguracionLista != []: #Pregunta si la configuración tiene algo.
        Label(ventanaConsultarConfiguracion,relief=FLAT,text=ConfiguracionLista[0],height=2,fg="white",bg="#104A57").place(x=70,y=163) #Etiqueta que usa la variable global de configuracion de lista.
        Label(ventanaConsultarConfiguracion,relief=FLAT,text=ConfiguracionLista[1],fg="white",bg="#104A57").place(x=140,y=270) #Etiqueta que usa la variable global de configuracion de lista.                                                    
        Label(ventanaConsultarConfiguracion,relief=FLAT,text=ConfiguracionLista[2],fg="white",bg="#104A57").place(x=140,y=380) #Etiqueta que usa la variable global de configuracion de lista.
        Label(ventanaConsultarConfiguracion,relief=FLAT,text=ConfiguracionLista[3],fg="white",bg="#104A57").place(x=360,y=175) #Etiqueta que usa la variable global de configuracion de lista.
        Label(ventanaConsultarConfiguracion,relief=FLAT,text=ConfiguracionLista[4],fg="white",bg="#104A57").place(x=570,y=175) #Etiqueta que usa la variable global de configuracion de lista.
        AgregarEquiposAlNote() #Agrega jugadores a la ventana del notebook.
    ventanaConsultarConfiguracion.mainloop()#Espera hasta que el usuario haga un evento.          

#----------------------------
#Ventana de tabla de posición
#----------------------------

def VentanaTablaPosicion():
    global ConfiguracionLista,ResultadosDePartidos
    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos1(eventos):
        canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)

    #-----------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels a la tabla de posición.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarPosicionesAlNote():
        global ConfiguracionLista
        fila=2
        l = OrdenarSegunPuntosyDiferencias()
        for i in l:
            Label(frameDeCanvas1,fg="white",text=str(i[0]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas1,fg="white",text=str(i[1]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas1,fg="white",text=str(i[2]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
            Label(frameDeCanvas1,fg="white",text=str(i[3]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=4)
            Label(frameDeCanvas1,fg="white",text=str(i[4]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=5)
            Label(frameDeCanvas1,fg="white",text=str(i[5]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=6)
            Label(frameDeCanvas1,fg="white",text=str(i[6]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=7)
            Label(frameDeCanvas1,fg="white",text=str(i[7]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=8)
            Label(frameDeCanvas1,fg="white",text=str(i[8]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=9)
            fila=fila+1
        Label(frameDeCanvas1,fg="white",text="Equipos",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
        Label(frameDeCanvas1,fg="white",text="que",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
        Label(frameDeCanvas1,fg="white",text="clasifican",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
        Label(frameDeCanvas1,fg="white",text=str(ConfiguracionLista[2]),bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=4)
        Label(frameDeCanvas1,fg="white",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=5)
        Label(frameDeCanvas1,fg="white",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=6)
        Label(frameDeCanvas1,fg="white",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=7)
        Label(frameDeCanvas1,fg="white",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=8)
        Label(frameDeCanvas1,fg="white",bg="#2FA4A4",width=8,font=("ms sans Serif",9,"bold")).grid(row=fila,column=9)

    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la pantalla de tabla de posición.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def CerrarTabla():
        ventanaTablaPosicion.destroy()

    #------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la pantalla de tabla de posición y vuelve a la pantalla principal.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def VolverPantallaPrincipal():
        ventanaTablaPosicion.destroy()
        ventanaDTorneosFutbol.deiconify()

    ventanaDTorneosFutbol.iconify()
    CargarResultados() #Usa la función para cargar a las variables globales.   
    CargarConfiguración() #Usa la función para cargar a las variables globales.
    ventanaTablaPosicion = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaTablaPosicion.title("DTorneo de Fútbol") #Titulo de la ventana.
    ventanaTablaPosicion.geometry("797x436") #Tamano de la ventana.
    ventanaTablaPosicion.maxsize(797,436) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaTablaPosicion.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    icono = ventanaTablaPosicion.iconbitmap("futbol.ico") #Icono de la ventana.
    canvas = Canvas(ventanaTablaPosicion,width=300, height=200, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    AcercaDe = Image.open("TablaPosicion.png") #Imagen.
    AcercaDe1 = ImageTk.PhotoImage(AcercaDe) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = AcercaDe1 #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor=NW, image=AcercaDe1) #Crea la imagen, el fondo de pantalla.
    nbook = ttk.Notebook(ventanaTablaPosicion,height=200,width=590) #Sea un nootebook dentro de la ventana.
    nbook.place(x=70,y=155) #Ubica el notebook en ese eje.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas2 = Canvas(frame1,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas2) #Se crea ua miniventana.
    frameDeCanvas1 = Frame(canvas2) #Se crea ua miniventana.
    Barra1 = Scrollbar(frame1,orient = "vertical",command = canvas2.yview) #Se crea un scrollbar.
    canvas2.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
    Barra1.pack(side="right",fill="y") #Se empaca el scrollbar.
    canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas2.create_window((0,0),window=frameDeCanvas1,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
    if ConfiguracionLista != [] or ResultadosDePartidos != []:
        AgregarPosicionesAlNote() #Llama la función para agregar los datos al notebook.
    tab1=nbook.add(frame1,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    no = Image.open("error.png") #Imagen de no.
    error = ImageTk.PhotoImage(no) #Se crea la imagen de no.
    Button(ventanaTablaPosicion,image=error,command=CerrarTabla,relief=FLAT,bg="black").place(x=725,y=170) #Botón de cancelar operación.
    prin = Image.open("Principal.png") #Imagen de volver.
    Principal = ImageTk.PhotoImage(prin) #Imagen de la ventana principal.
    Button(ventanaTablaPosicion,image=Principal,command=VolverPantallaPrincipal,relief=FLAT,bg="black").place(x=725,y=350)#Boton para regresar a la ventana principal.
    si = Image.open("exito.png") #Imagen de si o aceptar. 
    exito = ImageTk.PhotoImage(si) #Se crea la imagen de si o aceptar.
    Button(ventanaTablaPosicion,image=exito,command=CerrarTabla,relief=FLAT,bg="black").place(x=725,y=250) #Boton de si, aceptar.
    ventanaTablaPosicion.mainloop()#La ventana 

#---------------------------------------
#Ventana para consultar la configuración
#---------------------------------------

def VentanaConsultaConfiguracion():
    global ConfiguracionLista
    #------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
    
    def Eventos2(eventos):
        canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)

    #-----------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas1.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos1(eventos):
        canvas1.configure(scrollregion=canvas1.bbox("all"),width=250,height=280)

    #----------------------------------------------------------------------------
    #Descripción: La siguiente función representa el boton de eliminart jugadores. 
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def EliminarBoton():
        global CodigoPaisConsultar,ConfiguracionLista
        nombre = NombreEliminar.get()
        lista = PaisJugadores(ConfiguracionLista[5],CodigoPaisConsultar)
        if Esta125(nombre,lista):
            nuevo = EliminarJugadores(nombre,lista)        
            Team = PaisEquipo(ConfiguracionLista[5],CodigoPaisConsultar)
            ConfiguracionLista[5].remove(Team)
            Team[3] = nuevo
            ConfiguracionLista[5].append(Team)
            print(ConfiguracionLista)
            NombreEliminar.set("")
            return messagebox.showinfo("Info",nombre+" eliminado con exito")
        else:
            return messagebox.showerror("Error","No se encuentra este jugador")
        
    #-----------------------------------------------------------------
    #Descripción: La siguiente función representa el botón de aceptar.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarBoton():
        global CodigoPaisConsultar,ConfiguracionLista
        nombre = Nombre.get()
        Posicion = Posicion2.get()
        Num = Posicion4.get()
        lista = PaisJugadores(ConfiguracionLista[5],CodigoPaisConsultar)
        if Esta125(nombre,lista) == False:
            nuevo = AgregarJugador(nombre,Posicion,Num,lista)
            print(ConfiguracionLista[5])
            Pais = PaisEquipo(ConfiguracionLista[5],CodigoPaisConsultar)
            ConfiguracionLista[5].remove(Pais)
            Pais[3]=nuevo
            ConfiguracionLista[5].append(Pais)
            print(ConfiguracionLista)
            Nombre.set("")
            Posicion2.set("")
            Posicion4.set("0")
            return messagebox.showinfo("Info",nombre+" agregado con exito")
        else:
            return messagebox.showerror("Error","Ya se encuentra este jugador")

    #---------------------------------------------------------------------
    #Descripción: La siguiente función representa el boton de modificar.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def ModificarBoton():
        global CodigoPaisConsultar,ConfiguracionLista
        nombre = NombreModificar.get()
        print(nombre)
        Posicion = PosicionDelan.get()
        Num = Posicion3.get()
        lista = PaisJugadores(ConfiguracionLista[5],CodigoPaisConsultar)
        print(lista)
        if Esta125(nombre,lista):
            nuevo = ModificarJugador(nombre,Posicion,Num,lista)
            Pais = PaisEquipo(ConfiguracionLista[5],CodigoPaisConsultar)
            ConfiguracionLista[5].remove(Pais)
            Pais[3]=nuevo
            ConfiguracionLista[5].append(Pais)
            print(ConfiguracionLista)
            NombreModificar.set("")
            PosicionDelan.set("")
            Posicion3.set("0")
            return messagebox.showinfo("Info",nombre+" modificado con exito")
        else:
            return messagebox.showerror("Error","No se encuentra este jugador")


    #-----------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es una funcion es para limpiar la pantalla de contactos de la pantalla principal.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
                           
    def Clean():
        fila=1
        for i in range(100):
            Label(frameDeCanvas1,bg="white",height=2,width=10).grid(row=fila,column=1)
            Label(frameDeCanvas1,bg="white",height=2,width=4).grid(row=fila,column=2)
            Label(frameDeCanvas1,bg="white",height=2,width=4).grid(row=fila,column=3)
            fila=fila+1

    #---------------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función actualiza los jugadores de un equipo en la pantalla después de realizar una modificación.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
                
    def Actualizar():
        Clean()
        AgregarJugadoresAlNote()

    #--------------------------------------------------------------------------------------
    #Descripción: La siguiente función agrega labels a la pantalla para mostrar jugadores.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.

    def AgregarJugadoresAlNote():
        global ConfiguracionLista,CodigoPaisConsultar #Utiliza la variable global
        nombre=Equipito.get()
        if nombre == "":
            return messagebox.showerror("Error","Digite el nombre que desea consultar los jugadores")
        CodigoPaisConsultar = nombre
        Lista = JugadoresConsultar(nombre)
        if Lista == None:
            return messagebox.showerror("Error","No se encuentra este equipo")
        fila=2
        Label(frameDeCanvas1,fg="black",text="Jugadores",bg="cadet blue",width=10,font=("ms sans Serif",9,"bold")).grid(row=0,column=1)
        Label(frameDeCanvas1,fg="white",text="Nombre",bg="#2FA4A4",width=10,font=("ms sans Serif",9,"bold")).grid(row=1,column=1)
        Label(frameDeCanvas1,fg="white",text="Posicion",bg="#2FA4A4",width=10,font=("ms sans Serif",9,"bold")).grid(row=1,column=2)
        Label(frameDeCanvas1,fg="white",text="Número",bg="#2FA4A4",width=10,font=("ms sans Serif",9,"bold")).grid(row=1,column=3)
        for i in Lista:
            Label(frameDeCanvas1,fg="black",text=i[0],font=("ms sans Serif",9,"bold")).grid(row=fila,column=1)
            Label(frameDeCanvas1,fg="black",text=i[1],font=("ms sans Serif",9,"bold")).grid(row=fila,column=2)
            Label(frameDeCanvas1,fg="black",text=i[2],font=("ms sans Serif",9,"bold")).grid(row=fila,column=3)
            fila=fila+1

    #-----------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente función representa el boton de aceptar, las modificaciones que se realizaron serán guardadas.
    #Entradas: Ninguna.
    #Salidas: Ninguna.
    #Restricciones: Ninguna.
            
    def AceptarModificaciones():
        global ConfiguracionLista,CodigoPaisConsultar
        CodigoPaisConsultar = ""
        SobreescribeConfi2(ConfiguracionLista)
        CerrarVentanaConsuktaJugador()
        return messagebox.showinfo("Info","Modificaciones guardados con exito")
            
    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la ventana de consultar jugador.
    #Entradas: Ninguno.
    #Salidas: Ninguno. 
    #Restricciones: Ninguno.

    def CerrarVentanaConsuktaJugador():
        global ConfiguracionLista,CodigoPaisConsultar
        CodigoPaisConsultar = ""
        CargarConfiguración()
        ventanaJugador.destroy()

    if ConfiguracionLista == []:
        return messagebox.showinfo("Info","Primero debes configurar el torneo")
    ventanaJugador = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaJugador.title("Torneos de fútbol") #Titulo de la ventana.
    ventanaJugador.geometry("310x550") #Tamano de la ventana.
    ventanaJugador.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaJugador.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no = Image.open("error.png") #Imagen.
    error = ImageTk.PhotoImage(no) #Imagen de no o cancelar operación.
    si = Image.open("exito.png") #Imagen.
    exito = ImageTk.PhotoImage(si) #Imagen de aceptar operación.
    icono = ventanaJugador.iconbitmap("futbol.ico") #Icono de la ventana.
    EtiquetaContacto = Label(ventanaJugador,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoContacto = Label(ventanaJugador,text="Jugadores",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",11,"bold")).place(x=7,y=25) #Se le asigna una etiqueta a la variable.
    botonSi = Button(ventanaJugador,command=AceptarModificaciones,image=exito,bg="RoyalBlue4",relief=FLAT).place(x=70,y=480) #Se le asigna un boton a una variable.
    botonNo = Button(ventanaJugador,command=CerrarVentanaConsuktaJugador,image=error,bg="RoyalBlue4",relief=FLAT).place(x=200,y=480) #Se le asigna un boton a una variable.
    nbook = ttk.Notebook(ventanaJugador,height=306,width=290) #Sea un nootebook dentro de la ventana.
    nbook.place(x=7,y=90) #Ubica el notebook en esa posición.
    lupita = Image.open("lupa.png") #Imagen.
    lupa = ImageTk.PhotoImage(lupita) #Se crea unha lupa.
    frame5=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame5.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas5 = Canvas(frame5,bg="#2FA4A4", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla5 = ttk.Frame(canvas5) #Se crea ua miniventana.
    tab5=nbook.add(frame5,image=lupa,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    frameDeCanvas5 = Frame(canvas5) #Se crea una ventana dentro del canvas.
    canvas5.pack(side = 'left', fill = 'both', expand=True) #Empaca el canvas.
    Equipito = StringVar() #Se crea una variable string local.
    Label(frame5,relief=FLAT,text="Digite el código del país que desea consultar",fg="white",bg="#2FA4A4").place(x=10,y=50) #El label indica que digite el codigo del pais.
    Entry(frame5,relief=FLAT,textvariable=Equipito,fg="white",bg="#104A57").place(x=70,y=100) #Espacio para insertar el código del país.
    Button(frame5,text="Consultar",command=AgregarJugadoresAlNote,relief=FLAT,fg="white",bg="#104A57").place(x=100,y=150) #Boton para consultar los jugores configurados.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    frame2=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame2.place(x=10,y=10) #Se empaca la ventana.
    frame3=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame3.place(x=10,y=10) #Se empaca la ventana.
    frame4 = Frame(nbook) #Se crea una etiqueta o Tab.
    frame4.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas = Canvas(frame1,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas) #Se crea ua miniventana.
    canvas.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas1 = Canvas(frame2,width = 500,height = 200) #Se crea una ventana dentro de una ventana.
    frameDeCanvas1=Frame(canvas1) #Se crea una ventana dentro de una ventana dentro de una ventana.
    Barra1 = Scrollbar(frame2,orient = "vertical",command = canvas1.yview) #Se crea un scrollbar.
    canvas1.configure(yscrollcommand = Barra1.set) #Configura el scrollbar.
    Barra1.pack(side="right",fill="y") #El scrollbar se empaca y lo ubica en y.
    canvas1.pack(side="left") #El canvas se empaca.
    canvas1.create_window((0,0),window=frameDeCanvas1,anchor='nw') #Se crea una ventana dentro de la ventana.
    frameDeCanvas1.bind("<Configure>",Eventos1) #Espera a un evento del scrollbar.
    NombreConsultar = StringVar() #Se le asigna el valor string a la variable.
    canvas2 = Canvas(frame3, bg="#134E84",borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla2 = ttk.Frame(canvas2) #Se crea ua miniventana.
    canvas2.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas2.create_window((0, 0), window = ventanilla2, anchor = 'nw', tags = 'frame') #Se crea canvas un formato como una miniventana.
    NombreEliminar=StringVar() #Se le asigna el valor string
    EtiquetaEliminar = Label(canvas2,bg="#134E84",text="Digite el jugador que desea eliminar:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=60) #Se le asigna una etiqueta de texto a la variable.
    EspacioEliminar = Entry(canvas2,textvariable=NombreEliminar).place(x=70,y=120) #Se le asigna un campo de texto a la variable.
    BotonEliminar = Button(canvas2,text="Eliminar",command=EliminarBoton,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=170)#Se le asigna un boton a la variable.
    canvas3 = Canvas(frame4, borderwidth=0,bg="#134E84") #Se crea una ventana dentro de la ventana contactos.
    ventanilla3 = ttk.Frame(canvas3) #Se crea ua miniventana.
    canvas3.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    canvas3.create_window((0, 0), window = ventanilla3, anchor = 'nw', tags = 'frame') #Se crea canvas un formato como una miniventana.
    NombreModificar = StringVar() #Se le asigna el valor string a la variable.
    EtiquetaModificar = Label(canvas3,bg="#134E84",text="Digite el jugador que desea modificar:",fg="white",font=("ms sans Serif",9,"bold")).place(x=30,y=30) #Se le asigna una etiqueta de texto a la variable.
    EspacioModificar = Entry(canvas3,textvariable = NombreModificar).place(x=70,y=80)#Se le asigna un campo de texto a la variable.
    BotonModificar = Button(canvas3,text="Modificar",command=ModificarBoton,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=230)#Se le asigna un boton a la variable.
    PosicionDelan = StringVar()
    EtiquetaPosicion  = Label(canvas3,bg="#134E84",text="Posición",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=120) #Se le asigna una etiqueta de texto a la variable.
    EspacioConsultar  = Entry(canvas3,textvariable=PosicionDelan,width=12).place(x=50,y=150) #Se le asigna un campo de texto a la variable.
    EtiquetaNumero  = Label(canvas3,bg="#134E84",text="Número",fg="white",font=("ms sans Serif",9,"bold")).place(x=170,y=120) #Se le asigna una etiqueta de texto a la variable.
    Posicion3 = StringVar() #Se le asigna el valor de string a una variable.
    OptionPosicion = ttk.Combobox(canvas3,textvariable = Posicion3 ,values=imprimir(99),width=3).place(x=210,y=150) #Se le asigna a una variable el option boton
    añadir1 = Image.open("anadir.png") #Imagen.
    añadir = ImageTk.PhotoImage(añadir1) #Imagen de añadir jugador.
    modificar1 = Image.open("modificar.png") #Imagen. 
    modificar = ImageTk.PhotoImage(modificar1) #Imagen de modificar jugador.
    Jugadores1 = Image.open("Jugadores.png") #Imagen.
    Jugadores = ImageTk.PhotoImage(Jugadores1) #Imagen de jugadores.
    borrar1 = Image.open("borrar.png") #Imagen.
    borrar = ImageTk.PhotoImage(borrar1) #Imagen de borrar un jugador.
    cargar1 = Image.open("carga.png") #Imagen.
    cargar = ImageTk.PhotoImage(cargar1) #Imagen de cargar o actualizar.
    Button(ventanaJugador,command=Actualizar,image=cargar,bg="light sea green",relief=FLAT).place(x=250,y=20) #Boton de actualizar jugadores.
    Nombre = StringVar() #Variable local de nombre del jugador.
    Posicion2 = StringVar() #Variable local de posición del jugador.
    EtiquetaAgregar  = Label(canvas,bg="#134E84",text="Nombre",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=10) #Se le asigna una etiqueta de texto a la variable.
    EspacioAgregar  = Entry(canvas,textvariable= Nombre,width=25).place(x=50,y=50) #Se le asigna un campo de texto a la variable.
    BotonAgregar  = Button(canvas,text="Agregar",command=AgregarBoton,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=240)#Se le asigna un boton a la variable.
    EtiquetaPosicion  = Label(canvas,bg="#134E84",text="Posición",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=90) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaNumero  = Label(canvas,bg="#134E84",text="Número",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=170) #Se le asigna una etiqueta de texto a la variable.
    EspacioAgr  = Entry(canvas,textvariable=Posicion2,width=25).place(x=50,y=130) #Se le asigna un campo de texto a la variable.
    Posicion4 = StringVar() #Se le asigna el valor de string a una variable.
    OptionPosicion = ttk.Combobox(canvas,textvariable = Posicion4 ,values=imprimir(99),width=3).place(x=50,y=200) #Se le asigna a una variable el option boton
    tab2=nbook.add(frame2,image=Jugadores,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de consultar.
    tab1=nbook.add(frame1,image=añadir,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    tab3=nbook.add(frame3,image=borrar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de eliminar.
    tab4=nbook.add(frame4,image=modificar,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de modificar.
    ventanaJugador.mainloop()#La ventana espera hasta que el usuario digite algo.

#---------------------
#Ventana Configuración
#---------------------

def PlanillaJugadores():

    #-------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas2.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
    
    def Eventos2(eventos):
        
        canvas2.configure(scrollregion=canvas2.bbox("all"),width=250,height=280)

    #-------------------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para esperar hasta que usuario interactue con el scrollbar de la pantalla de canvas1.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def Eventos1(eventos):
        
        canvas1.configure(scrollregion=canvas1.bbox("all"),width=250,height=280)

    #--------------------------------------------------------------------------------------
    #Descripción: La siguiente función valida datos de los jugadores que se van a agregar.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
    
    def ValidarDatosDeJugadoresBoton():
    
        global Jugadores
        Name = Nombre.get()
        Position = Posicion.get()
        try:
            Chema = int(Camisa.get())
        except:
            if Camisa.get() == "":
                return messagebox.showerror("Error","Digite un número de camiseta")
        Player = Jugador(Name,Position,Chema)
        if Player.VálidoNombre() == False:
            return messagebox.showerror("Error","El nombre debe de tener entre 2 a 50 letras")
        if Player.VálidoPosicion() == False:
            return messagebox.showerror("Error","La posición debe de tener entre 5 a 20 letras")
        if Player.VálidoNumero() == False:
            return messagebox.showerror("Error","El número de la camiseta debe estar entre 1 a 99")
        else:
            Jugadores = Jugadores + [Player.CrearListaJugador()]
            Nombre.set("")
            Posicion.set("")
            Camisa.set(0)
            messagebox.showinfo("Info","Jugador "+Name +" ha sido agregado")
            print(Jugadores)

    #--------------------------------------------------------------------
    #Descripción: La siguiente es para agregar cada jugador que se desea.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
            
    def AceptarVentanaJugador():
        
        global EquipoProceso,Jugadores,EquiposAgregar
        EquipoProceso = [EquipoProceso[0] + [Jugadores]]
        EquiposAgregar = EquiposAgregar + EquipoProceso
        EquipoProceso = []
        Jugadores = []
        print(EquiposAgregar)
        ventanaJugador.destroy()
        
    #--------------------------------------------------------------------------
    #Descripción: La siguiente función cierra la pantalla de agregar jugadores.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.
        
    def CerrarVentanaJugador():
        
        global EquipoProceso,Jugadores
        EquipoProceso = []
        Jugadores = []
        ventanaJugador.destroy()

    #-------------------------------
    #Ventana para agregar jugadores
    #-------------------------------
    
    ventanaJugador = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaJugador.title("Torneos de fútbol") #Titulo de la ventana.
    icono = ventanaJugador.iconbitmap("futbol.ico") #Icono de la ventana.
    ventanaJugador.geometry("310x550") #Tamano de la ventana.
    ventanaJugador.maxsize(310,550) #El tamano máximo que se puede agrandar o minimizar la pantalla.
    ventanaJugador.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    no = Image.open("error.png") #Imagen.
    error = ImageTk.PhotoImage(no) #Imagen de no o cancelar operación.
    si = Image.open("exito.png") #Imagen. 
    exito = ImageTk.PhotoImage(si) #Imagen de si o aceptar.
    agregar = Image.open("agregar.png") #Imagen.
    agregar1 = ImageTk.PhotoImage(agregar) #Imagen de agregar jugador.
    EtiquetaContacto = Label(ventanaJugador,bg="light sea green",width=50,height=4).place(x=0,y=1) #Se le asigna una etiqueta a la variable.
    TextoContacto = Label(ventanaJugador,text="Agregar Jugadores",fg="white",relief=FLAT,bg="light sea green",font=("ms sans Serif",11,"bold")).place(x=7,y=25) #Se le asigna una etiqueta a la variable.
    botonSi = Button(ventanaJugador,command=AceptarVentanaJugador,image=exito,bg="RoyalBlue4",relief=FLAT).place(x=70,y=480) #Se le asigna un boton a una variable.
    botonNo = Button(ventanaJugador,command=CerrarVentanaJugador,image=error,bg="RoyalBlue4",relief=FLAT).place(x=200,y=480) #Se le asigna un boton a una variable.
    nbook = ttk.Notebook(ventanaJugador,height=306,width=290) #Sea un nootebook dentro de la ventana.
    nbook.place(x=7,y=90) #Ubica el nootebook en esa posición x,y.
    frame1=Frame(nbook,relief=GROOVE,bd=1) #Se crea una ventana dentro del notebook
    frame1.pack(fill=BOTH, expand=True) #Se empaca la ventana.
    canvas = Canvas(frame1,bg="#134E84", borderwidth=0) #Se crea una ventana dentro de la ventana contactos.
    ventanilla = ttk.Frame(canvas) #Se crea ua miniventana.
    canvas.pack(side = 'left', fill = 'both', expand=True) #Se empaca el Canvas.
    Nombre = StringVar() #Se le asigna el valor string a la variable.
    EtiquetaNombre  = Label(canvas,bg="#134E84",text="Nombre",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=10) #Se le asigna una etiqueta de texto a la variable.
    EspacioNombre  = Entry(canvas,textvariable=Nombre,width=25).place(x=50,y=50) #Se le asigna un campo de texto a la variable.
    BotonAgregar  = Button(canvas,text="Agregar",command=ValidarDatosDeJugadoresBoton,relief=FLAT,fg="white",bg="deep sky blue").place(x=100,y=240)#Se le asigna un boton a la variable.
    EtiquetaPosicion  = Label(canvas,bg="#134E84",text="Posición",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=90) #Se le asigna una etiqueta de texto a la variable.
    EtiquetaNumero  = Label(canvas,bg="#134E84",text="Número",fg="white",font=("ms sans Serif",9,"bold")).place(x=10,y=190) #Se le asigna una etiqueta de texto a la variable.
    Posicion = StringVar() #Variable string, de la posicion del equipo.
    EspacioPosicion = Entry(canvas,textvariable=Posicion,width=25).place(x=50,y=130) #Se le asigna un campo de texto a la variable.
    Camisa = StringVar() #Se le asigna el valor de string a una variable.
    OptionCamisa = ttk.Combobox(ventanaJugador,textvariable = Camisa ,values=imprimir(99),width=3).place(x=95,y=320) #Se le asigna a una variable el option boton
    tab1=nbook.add(frame1,image=agregar1,padding = 10) #Se le agrega al cuaderno una etiqueta y se le asigna la imagen de Contactos.
    ventanaJugador.mainloop()#Espera hasta que el usuario interactue con el.

#----------------------
#Ventana Configuración
#----------------------

def VentanaConfiguracion():

    #--------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para agregar equipos a la variable global y validar los datos de entradas.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.

    def VálidoLosDatosDeLasEntradas():
        
        global EquipoProceso,ConfiguracionLista,EquiposAgregar
        #Validación de entradas según tipo de dato.
        Nombre = NombreTorneo.get()
        try:
            Numero = int(EquiposParticipantes.get())
        except:
            return messagebox.showerror("Error","La cantidad de equipos participantes debe ser un número entero positivo")
        if ContarElementosDeLista(EquiposAgregar) != int(EquiposParticipantes.get()):
            print(EquiposParticipantes.get(),"jhlfo",EquiposAgregar)
            return messagebox.showerror("Error","La cantidad de equipos participantes no coincide con los equipos añadidos")        
        try:
            Cantidad = int(EquiposClasifican.get())
        except:
            return messagebox.showerror("Error","La cantidad de equipos que clasifican debe ser un número entero positivo")
        try:
            Win = int(PtsGanados.get())
        except:
            return messagebox.showerror("Error","Los puntos ganados por partidos debe ser un número entero positivo")
        try:
            Empty = int(PtsEmpatados.get())
        except:
            return messagebox.showerror("Error","Los puntos empatados por partidos debe ser un número entero positivo")
        try:
            Posicion = int(FIFAPosicion.get())
        except:
            return messagebox.showerror("Error","La posición de un equipo debe ser un número entero positivo")
        #Utilización de Clases
        TorneoNuevo = torneo(Nombre,Numero,Cantidad,Win,Empty)
        #Condiciones y mensajes de textos de error
        if TorneoNuevo.ValidoNombre() == False:
            return messagebox.showerror("Error","El nombre del torneo debe tener por lo menos 2 o hasta 50 letras")
        if TorneoNuevo.CantidadDeEquipos() == False:
            return messagebox.showerror("Error","La cantidad de equipos participantes debe ser mayor que 1 y debe ser par")
        if TorneoNuevo.Clasifican() == False:
            return messagebox.showerror("Error","La cantidad de equipos que clasifican debe ser mayor que 0 y menor que la cantidad de equipo participante")
        if TorneoNuevo.PuntosGanados() == False:
            return messagebox.showerror("Error","La cantidad de puntos debe ser mayor que 0")
        if TorneoNuevo.PuntosEmpatados() == False:
            return messagebox.showerror("Error","La cantidad de puntos empatados debe ser mayor que 0 y menor que los puntos por cada partido ganado")
        else:
            Lista = TorneoNuevo.CrearLista()
            ConfiguracionLista = Lista + [EquiposAgregar]
            SobreescribeConfi()
            print(ConfiguracionLista)
            EquipoProceso = []
            EquiposAgregar = []
            ventanaConfiguracion.destroy()
            
    #----------------------------------------------------------------------
    #Descripción: La siguiente función cierra la pantalla de configuracion.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def CerrarVentanaConfiguración():
        ventanaConfiguracion.destroy()
        
    #----------------------------------------------------------------------
    #Descripción: La siguiente función enseña la pantalla de principal.
    #Entradas: Ninguno.
    #Salidas: Ninguno.
    #Restricciones: Ninguno.

    def Volver():
        ventanaConfiguracion.destroy()
        ventanaDTorneosFutbol.deiconify()
        
    #--------------------------------------------------------------------------------------------------------
    #Descripción: La siguiente es para agregar equipos a la variable global y validar los datos de entradas.
    #Entradas: Ninguno.
    #Salidas: Ninguna
    #Restricciones: Ninguno.
            
    def BotonAgregarEquipo():
        global EquiposAgregar,EquipoProceso
        try:
            Posicion = int(FIFAPosicion.get())
        except:
            return messagebox.showerror("Error","La posición de un equipo debe ser un número entero positivo")
        Codigo = Code.get() 
        Country = Pais.get()
        EquipoAgregar1 = Equipo(Codigo,Country,Posicion)
        if Codigo in ListaCodigos(EquiposAgregar,0):
            return messagebox.showerror("Error","Ya se encuentra este código registrado: "+str(Codigo))
        if Country in ListaCodigos(EquiposAgregar,1):
            return messagebox.showerror("Error","Ya se encuentra este país registrado: "+str(Country))
        if Posicion in ListaCodigos(EquiposAgregar,2):
            return messagebox.showerror("Error","Ya se encuentra este posición registrado: "+str(Posicion))
        if EquipoAgregar1.VálidoCodigo() == False:
            return messagebox.showerror("Error","El código de equipo debe ser de 3 letras")
        if EquipoAgregar1.VálidoNombre() == False:
            return messagebox.showerror("Error","El nombre del equipo debe estar entre 1 a 50 letras")
        if EquipoAgregar1.VálidoPosición() == False:
            return messagebox.showerror("Error","El posición del equipo debe estar entre 1 a 270")
        else:
            EquipoProceso = [EquipoAgregar1.CrearLista()] + EquipoProceso
            Code.set("") 
            Pais.set("")
            FIFAPosicion.set(0)
            print(EquipoProceso)
            PlanillaJugadores()
            
    ventanaDTorneosFutbol.iconify()
    ventanaConfiguracion = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
    ventanaConfiguracion.title("DTorneos de Futbol") #Titulo de la ventana.
    canvas = Canvas(ventanaConfiguracion,width=300, height=210, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
    canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
    icono = ventanaConfiguracion.iconbitmap("futbol.ico") #Icono de la ventana.
    ventanaConfiguracion.geometry("798x411") #Tamano de la ventana.
    ventanaConfiguracion.maxsize(798,411) #El tamano máximo que se puede agrandar la pantalla.
    ventanaConfiguracion.minsize(798,411) #El tamano máximo que se puede minimizar la pantalla.
    canvas.config(bg = "RoyalBlue4") #Configura el color de la ventana.
    PantallaConfiguracion1 = Image.open("ConfiguracionPantalla.png") #Imagen.
    PantallaConfiguracion = ImageTk.PhotoImage(PantallaConfiguracion1) #Agregarle la imagen al fondo de la pantalla.
    canvas.img = PantallaConfiguracion #Imagen en la pantalla de dibujo.
    canvas.create_image(0, 0, anchor = NW, image = PantallaConfiguracion) #Crea la imagen en la pantalla.
    NombreTorneo = StringVar() #Variable de tipo string de nombre del torneo.
    EquiposParticipantes = StringVar() #Variable de tipo string de la cantidad de equipos participantes.
    EquiposClasifican = StringVar() #Variable de tipo string de codigo de equipos que clasifican.
    PtsGanados = StringVar() #Variable de tipo string de pts que se ganan por partidos.
    PtsEmpatados = StringVar() #Variable de tipo string de puntos por partidos empatados.
    Code = StringVar() #Variable de tipo string de codigo del equipo.
    Pais = StringVar() #Variables de tipo string, del equipo.
    Entry(ventanaConfiguracion,textvariable = NombreTorneo,relief=FLAT).place(x=150,y=160) #Espacio de nombre de torneo.
    Entry(ventanaConfiguracion,textvariable = EquiposParticipantes,relief=FLAT).place(x=150,y=245) #Espacio de cantidad de equipos participantes.
    Entry(ventanaConfiguracion,textvariable = EquiposClasifican,relief=FLAT).place(x=150,y=325) #Espacio para cantidad de equipos clasifican. 
    Entry(ventanaConfiguracion,textvariable = PtsGanados, relief=FLAT).place(x=550,y=160) #Espacio para puntos ganados.
    Entry(ventanaConfiguracion,textvariable = PtsEmpatados,relief=FLAT).place(x=550,y=240) #Espacio para pts. empatados.
    Entry(ventanaConfiguracion,textvariable = Code, relief=FLAT,width=7).place(x=416,y=330) #Espacio para codigo.
    Entry(ventanaConfiguracion,textvariable = Pais,relief=FLAT,width=13).place(x=510,y=330) #Espacio para país.
    FIFAPosicion = StringVar() #Variable string la posición del equipo.
    OptionPosicion = ttk.Combobox(ventanaConfiguracion,textvariable = FIFAPosicion,values = imprimir(270) ,width = 3).place(x=650,y=330) #Se le asigna a una variable el option boton
    prin = Image.open("Principal.png") #Imagen de principal.
    Principal = ImageTk.PhotoImage(prin) #Imagen de principal.
    Button(ventanaConfiguracion,image=Principal,command=Volver,relief=FLAT,bg="#57DCFC").place(x=735,y=350)#Crea el botón para regresar la pantalla principal.
    no = Image.open("error.png") #Busca la Imagen de no.
    error = ImageTk.PhotoImage(no) #Crea la imagen.
    Button(ventanaConfiguracion,command = CerrarVentanaConfiguración,image = error,relief = FLAT,bg = "#57DCFC").place(x=735,y=130) #Crea el botón de no o cancelar. 
    si = Image.open("exito.png") #Busca la Imagen de si.
    exito = ImageTk.PhotoImage(si) #Crea la imagen.
    Button(ventanaConfiguracion,command = VálidoLosDatosDeLasEntradas,image = exito,relief = FLAT,bg = "#57DCFC").place(x = 735,y = 200) #Crea el botón de si o aceptar.
    mas1 = Image.open("mas.png") #Busca la Imagen de agregar equipo.
    mas = ImageTk.PhotoImage(mas1) #Crea la imagen.
    Button(ventanaConfiguracion,command=BotonAgregarEquipo,image = mas,relief = FLAT,bg = "#57DCFC").place(x = 735,y = 300) #Crea el botón de agregar equipo.
    ventanaConfiguracion.mainloop() #Espera hasta que el usuario interactue con el.

#-----------------------------------------------------------------------
#Descripción: La siguiente clase se define una ventana, el de acerca de.
#Entradas: Ninguno.
#Salidas: Ninguno.
#Restricciones: Ninguno.

class VentanaAcercaDe:
       def __init__(self):
              self.ventanaAcercaDe = Toplevel(ventanaDTorneosFutbol) #Se crea una ventana.
              self.ventanaAcercaDe.title("DTorneos de Futbol") #Titulo de la ventana.
              canvas = Canvas(self.ventanaAcercaDe,width=300, height=210, bg='white') #Se crea una pantalla canvas en donde se le coloca labels, botones etc.
              canvas.pack(expand=YES, fill=BOTH) #Empaca el canvas y lo exapande en toda la pantalla.
              icono = self.ventanaAcercaDe.iconbitmap("futbol.ico") #Icono de la ventana.
              self.ventanaAcercaDe.geometry("688x463") #Tamano de la ventana.
              self.ventanaAcercaDe.maxsize(688,463) #El tamano máximo que se puede agrandar o minimizar la pantalla.
              self.ventanaAcercaDe.minsize(688,463) #Tamaño maximo de la ventana. 
              canvas.config(bg = "RoyalBlue4") #Configura el color de la ventana.
              AcercaDe = Image.open("AcercaDe.png") #Imagen.
              AcercaDe1 = ImageTk.PhotoImage(AcercaDe) #Agregarle la imagen al fondo de la pantalla.
              canvas.img = AcercaDe1 #Imagen en la pantalla de dibujo.
              canvas.create_image(0, 0, anchor=NW, image=AcercaDe1) #Crea la imagen en la pantalla.
              self.ventanaAcercaDe.mainloop() #Espera hasta que el usuario haga un evento.              

#---------------------------------------------------------------------
#Descripción: La siguiente función despliega 2 botones en la pantalla.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def OpcionesConfiguración():
       Button(ventanaDTorneosFutbol,command=ConsultarConfiguracion,bg="black",image=Conf1,relief=FLAT).place(x=510,y=270) #Boton de salida
       Button(ventanaDTorneosFutbol,command=VentanaConfiguracion,image=Conff,bg="black",relief=FLAT).place(x=510,y=390)#Boton de salida
              
#--------------------------------------------------------------------------------------------------
#Descripción: La siguiente función cierra la pantalla principal de la aplicación torneos de futbol.
#Entradas: Ninguna.
#Salidas: Ninguna.
#Restricciones: Ninguna.

def CerrarPrincipal():
    ventanaDTorneosFutbol.destroy()

#------------------------------------------------------------------------------------------------------------------------------------------
#Pantalla Principal
#------------------------------------------------------------------------------------------------------------------------------------------

ventanaDTorneosFutbol = Tk()#Abre una ventana.
ventanaDTorneosFutbol.geometry("871x524") #Tamaño de la ventana.
ventanaDTorneosFutbol.title("DTorneos de Futbol") #Titulo de la ventana.
ventanaDTorneosFutbol.maxsize(871,524) #Tamaño maximo de la ventana.
ventanaDTorneosFutbol.minsize(871,524) #Tamaño maximo de la ventana. 
icono = ventanaDTorneosFutbol.iconbitmap("futbol.ico") #Icono de la ventana.
dibujo = Canvas(ventanaDTorneosFutbol) #Ventana de dibujos.
dibujo.pack(expand=True, fill=BOTH) #Empaca la ventana de dibujo.
pintura = Image.open("Reus.png") #Imagen.
Con = Image.open("ConConf.png") #Imagen.
Conf1 = ImageTk.PhotoImage(Con) #Agregarle la imagen al fondo de la pantalla.
m = Image.open("Manual.png") #Imagen.
manu = ImageTk.PhotoImage(m) #Agregarle la imagen al fondo de la pantalla.
v = Image.open("Video.png") #Imagen.
vide = ImageTk.PhotoImage(v) #Agregarle la imagen al fondo de la pantalla.
Conf = Image.open("ConfConf.png") #Imagen.
Conff = ImageTk.PhotoImage(Conf) #Agregarle la imagen al fondo de la pantalla.
Fondo = ImageTk.PhotoImage(pintura) #Agregarle la imagen al fondo de la pantalla.
dibujo.img = Fondo #Imagen en la pantalla de dibujo.
dibujo.create_image(0, 0, anchor=NW, image=Fondo) #Crea la imagen en la pantalla.
Titulo = Image.open("Torneo2.png") #Imagen.
Torneo = ImageTk.PhotoImage(Titulo) #Imagen del titulo.
titulo = Label(dibujo,image=Torneo,bg="black",relief=FLAT).place(x=20, y=30)#Etiqueta de titulo de la pantalla.
Resultados = Image.open("Registrar-Resultados.png") #Imagen.
Registro1 = ImageTk.PhotoImage(Resultados) #Imagen de registrar resultados.
titulo1 = Button(dibujo,bg="gold",command=VentanaRegistrarResultados,activebackground="white",image=Registro1,relief=FLAT).place(x=60, y=150) #Boton para registrar resulytados.
Tabla1 = Image.open("Tabla.png") #Imagen.
Tabla2 = ImageTk.PhotoImage(Tabla1) #Imagen de tabla de posiciones de equipos.
titulo2 = Button(dibujo,image=Tabla2,command=VentanaTablaPosicion,bg="black",relief=FLAT).place(x=60, y=270) #Boton de tabla de equipos; posiciones.
Goleador = Image.open("Goleadores.png") #Imagen.
Tabla3 = ImageTk.PhotoImage(Goleador) #Imagen de tabla de goleadores.
titulo3 = Button(dibujo,command=VentanaTablaDeGoleadores,image=Tabla3,relief=FLAT,bg="gold").place(x=60, y=390) #Boton de tabla de goleadores.
Configuracion = Image.open("Configuraion.png") #Imagen.
Configuracion1 = ImageTk.PhotoImage(Configuracion) #Imagen de configuracion.
titulo4 = Button(dibujo,image=Configuracion1,command=OpcionesConfiguración,bg="black",relief=FLAT).place(x=290, y=150) #Boton de configuracion.
calendario = Image.open("calendario.png") #Imagen.
calendario1 = ImageTk.PhotoImage(calendario) #Imagen de calendario.
titulo5 = Button(dibujo,command=VentanaDeCalendario,image=calendario1,bg="gold",relief=FLAT).place(x=290, y=270) #Boton de calendario
Ayuda = Image.open("Ayuda.png") #Imagen.
Ayuda1 = ImageTk.PhotoImage(Ayuda) #Imagen de ayuda
titulo6 = Button(dibujo,image=Ayuda1,command=OpcionesAcercaDe,bg="black",relief=FLAT).place(x=400, y=270) #Boton de ayuda
acerca = Image.open("acerca.png") #Imagen.
acerca1 = ImageTk.PhotoImage(acerca) #Imagen de acrca de
titulo7 = Button(dibujo,image=acerca1,command=VentanaAcercaDe,bg="black",relief=FLAT).place(x=290, y=390) #Boton de acerca de
Salir = Image.open("Salir.png") #Imagen.
Salir1 = ImageTk.PhotoImage(Salir) #Imagen de salir
titulo8 = Button(dibujo,image=Salir1,bg="gold",command=CerrarPrincipal,relief=FLAT).place(x=400, y=390) #Boton de salida
ventanaDTorneosFutbol.mainloop() #Se mantiene hasta que ocurra un evento.
