from calificaciones import*


def solicita_notas():

    nombre = input("Introduzca su nombre: ")
    teoria_1 = input("Ingrese la nota del examen de teoría 1: ")
    teoria_2 = input("Ingrese la nota del examen de teoría 2: ")
    teoria_3 = input("Ingrese la nota del examen de teoría 3: ")
    teoria_4 = input("Ingrese la nota del examen de teoría 4: ")
    practico_1 = input("Ingrese la nota del examen práctico 1: ")
    practico_2 = input("Ingrese la nota del examen práctico 2: ")

    notas = (teoria_1, teoria_2, teoria_3, teoria_4, practico_1, practico_2)
    
    return notas

def mostrar_notas():

    nombre = input("Introduzca su nombre: ")
    teoria_1 = float(input("Ingrese la nota del examen de teoría 1: "))
    teoria_2 = float(input("Ingrese la nota del examen de teoría 2: "))
    teoria_3 = float(input("Ingrese la nota del examen de teoría 3: "))
    teoria_4 = float(input("Ingrese la nota del examen de teoría 4: "))
    practico_1 = float(input("Ingrese la nota del examen práctico 1: "))
    practico_2 = float(input("Ingrese la nota del examen práctico 2: "))

    nota_final = nota_continua((teoria_1, teoria_2, teoria_3, teoria_4),(practico_1, practico_2))

    return nota_final
    





    




