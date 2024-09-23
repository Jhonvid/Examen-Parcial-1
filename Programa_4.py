EstudiantesA = ["David","Angel","Luis","Carmen","Samuel","Sergio","Adriana","Maria","Ana","Laura"]
EstudiantesB = ["Jesus","Adrian","Eduardo","Tomas","Felipe","Lourdes","Lucia","Marta","Kelly","Cristina"]
EstudiantesComun = []

def agregar_estudiante1():
    A = int(input("\nIngrese el numero del estudiante del Grupo B para ingresarlo al A (Del 0 al 9): "))
    EstudiantesA.append(EstudiantesB[A])
    EstudiantesComun.append(EstudiantesB[A])
    Resp = input("\n¿Desea ingresar otro estudiante del Grupa B al A? (Si/No):")
    if Resp.lower() == "si":
        agregar_estudiante1()
    else:
        print("La nueva lista es:",EstudiantesA)

def agregar_estudiante2():
    B = int(input("\nIngrese el numero del estudiante del Grupo B para ingresarlo al A (Del 0 al 9): "))
    EstudiantesB.append(EstudiantesA[B])
    EstudiantesComun.append(EstudiantesA[B])
    Resp = input("\n¿Desea ingresar otro estudiante del Grupa B al A? (Si/No):")
    if Resp.lower() == "si":
        agregar_estudiante2()
    else:
        print("La nueva lista es:",EstudiantesB)

print("\nEsta es la lista actual de estudiantes en el grupo A:","\n",EstudiantesA)
print("\nEsta es la lista actual de estudiantes en el grupo B:","\n",EstudiantesB)
agregar_estudiante1()
agregar_estudiante2()

print("\nLos estudiantes del grupo B que no estan en el a son:",EstudiantesB[:10])
print("\nLos estudiantes del grupo A que no estan en el a son:",EstudiantesA[:10])
print("\nLos estudiantes que estan en grupo A y B son:",EstudiantesComun)