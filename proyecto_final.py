import pickle
import os
class tarea_ad:
        def __init__(self,tarea,tipo):
            self.tarea = tarea
            self.tipo = tipo
if os.path.exists("tareas.pickle"):
    with open("tareas.pickle", "rb") as f:
        l1st = pickle.load(f)
else:
    l1st = []
    with open("tareas.pickle", "wb") as f:
        pickle.dump(l1st,f)
def listt(s):
    l1st.extend([tarea_ad(s,tipo)])
def lists():
    listt(input("Nombre de la tarea\n"))
print("AufgabeChef\nby i\ndescricion ")
n = True
while n:
    opciones = input("agregar tarea 1\nlistar tareas 2\nsalir 3\n")
    if opciones == "1" or opciones == "agregar tarea":
        tipo = input("escolar 1\nlaboral 2\ngrupal 3\neconomica 4\npersonal 5\notros 6\nsi no desea elegir un tipo use el entrer\n")
        if  tipo == "1" or tipo =="escolar":
            tipo = "escolar"
            lists()
        elif tipo == "2" or tipo =="laboral":
            tipo = "laboral"
            lists()
        elif tipo == "3" or tipo =="grupal":
            tipo = "grupal"
            lists()
        elif tipo == "4" or tipo =="economica":
            tipo = "economica"
            lists()
        elif tipo == "5" or tipo =="personal":
            tipo = "personal"
            lists()
        elif tipo == "6" or tipo =="otros":
            tipo = "otros"
            lists()
        elif tipo == "" :
            lists()
        else:
            print("no existe la opcion selecionala")
    elif opciones == "2" or opciones == "listar" or opciones == "listar tarea":
        for obj in l1st:
            print("Tarea:",obj.tarea,"Tipo:", obj.tipo)
    elif opciones == "3" or opciones == "salir":
        with open("tareas.pickle", "wb") as f:
            pickle.dump(l1st,f)
        n = False
    else:
        print("el programa no reconoce la opcion")
