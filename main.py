import pickle;import os;n = True
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
while n:
    opciones = input("agregar tarea 1\nlistar tareas 2\nsalir 3\n")
    match opciones:
        case "1" | "agregar tarea":
            tipo = input("escolar 1\nlaboral 2\ngrupal 3\neconomica 4\npersonal 5\notros 6\nsi no desea elegir un tipo use el entrer\n")
            match tipo:
                case "1" | "escolar":
                    tipo = "escolar"
                    lists()
                case "2" | "laboral":
                    tipo = "laboral"
                    lists()
                case "3" | "grupal":
                    tipo = "grupal"
                    lists()
                case "4" | "economica":
                    tipo = "economica"
                    lists()
                case "5" | "personal":
                    tipo = "personal"
                    lists()
                case "6" | "otros":
                    tipo = "otros"
                    lists()
                case "":
                    lists()
                case _:
                    print("no existe la opcion selecionala")
        case "2" | "listar" | "listar tarea":
            for obj in l1st:
                print("Tarea:",obj.tarea,"Tipo:", obj.tipo)
        case "3" | "salir":
            with open("tareas.pickle", "wb") as f:
                pickle.dump(l1st,f)
            n = False
        case _:
            print("el programa no reconoce la opcion")
