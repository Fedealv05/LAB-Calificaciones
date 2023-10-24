#Módulo para definir funciones

#a)

def nota_teoria(nota1, nota2):
    """
    Calcula la nota del bloque teórico de un cuatrimestre como la media de las notas.
    
    :param nota1: Nota del primer examen teórico.
    :param nota2: Nota del segundo examen teórico.
    :return: Nota del bloque teórico (media de las dos notas, tratando None como 0).
    """
    if nota1 is None:
        nota1 = 0
    if nota2 is None:
        nota2 = 0
    
    return (nota1 + nota2) / 2

# b)

def nota_cuatrimestre(teoria, practicas):
    """
    Calcula la nota del cuatrimestre a partir de las notas de los exámenes teóricos y el examen práctico.

    :param notas_teoria: Tupla con las notas de los exámenes teóricos (T1, T2).
    :param nota_practico: Nota del examen práctico (P).
    :return: Nota del cuatrimestre calculada según la fórmula especificada o 0 si la media de teoría es menor que 4.
    """
    T1, T2 = teoria
    if T1 is None:
        T1 = 0
    if T2 is None:
        T2 = 0
    if practicas is None:
        practicas = 0

    media_teoria = (T1 + T2) / 2

    if media_teoria >= 4:
        nota_cuatrimestre = 0.1 * (T1 + T2) + 0.8 * practicas
    else:
        nota_cuatrimestre = 0

    return nota_cuatrimestre

#c)

def nota_continua(notas_teoria,notas_practicas):
    """
    Calcula la nota total de la asignatura

    :param notas_teoria: Tupla con las notas de los exámenes teóricos (T1, T2, T3, T4).
    :param nota_practico: Tupla con las notas de los exámenes prácticos (P1, P2).
    :return: Nota del curso
    
    """
    T1, T2, T3, T4 = notas_teoria

    P1, P2 = notas_practicas

    if T1 is None:
        T1 = 0
    if T2 is None:
        T2 = 0
    if T3 is None:
        T3 = 0
    if T4 is None:
        T4 = 0
    if P1 is None:
        P1 = 0
    if P2 is None:
        P2 = 0

    if (0.1 * (T1 + T2) + 0.8 * P1)<4:
        nota_continua= min(4,((0.1 * (T1 + T2) + 0.8 * P1) + (0.1 * (T3 + T4) + 0.8 * P2))/2)

    elif (0.1 * (T3 + T4) + 0.8 * P2)<4:
        nota_continua= min(4,((0.1 * (T1 + T2) + 0.8 * P1) + (0.1 * (T3 + T4) + 0.8 * P2))/2)

    else:
        nota_continua = ((0.1 * (T1 + T2) + 0.8 * P1) + (0.1 * (T3 + T4) + 0.8 * P2))/2

    return nota_continua
    


        






    