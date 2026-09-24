personas = ["Jose", "Maria", "Juan", "Karla"]

materias = ["Matematicas", "Programacion", "Ciencias"]

grupos = ["A", "B"]



alumnos = ["Jose", "Maria", "Karla"]

maestros = ["Juan"]

cursa = [("Jose", "Matematicas"), 
        ("Karla", "Programacion"), 
        ("Maria", "Ciencias")]

imparte = [("Juan", "Matematicas")]


def consultar_alumno(persona):
    return persona in alumnos

def consultar_maestro(persona):
    return persona in maestros

def consultar_materia(materia):
    return materia in materias

def consultar_cursa(persona, materia):
    return (persona, materia) in cursa

def consultar_imparte(maestro, materia):
    return (maestro, materia) in imparte



print("----CONSULTAS----\n")

print("----PREDICADOS ALUMNOS----\n")
print("Jose es alumno?")
print(consultar_alumno("Jose"))

print("Juan es alumno?")
print(consultar_alumno("Juan"))

print("\n----PREDICADOS MAESTROS----\n")
print("juan es maestro?")
print(consultar_maestro("Juan"))

print("Maria es maestro?")
print(consultar_maestro("Maria"))

print("\n----PREDICADOS MATERIAS----\n")
print("Matematicas es materia?")
print(consultar_materia("Matematicas"))

print("Historia es materia?")
print(consultar_materia("Historia"))

print("\n----PREDICADOS CURSA----\n")
print("Jose cursa Matematicas?")
print(consultar_cursa("Jose", "Matematicas"))

print("Jose cursa Programacion?")
print(consultar_cursa("Jose", "Programacion"))

print("\n----PREDICADOS IMPARTE----\n")
print("Juan imparte Matematicas?")
print(consultar_imparte("Juan", "Matematicas"))

print("Juan imparte Programacion?")
print(consultar_imparte("Juan", "Programacion"))