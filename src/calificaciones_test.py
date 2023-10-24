from calificaciones import*

#Test A

print("9.1, 7.2 ==> " + str(nota_teoria(9.1, 7.2)))
print("4.0, 6.0  ==> " + str(nota_teoria(4.0, 6.0)))
print("4.0, 3.0 ==> " + str(nota_teoria(4.0, 3.0)))
print("None, 3.0 ==> " + str(nota_teoria(None, 3.0)))
print("9.0, None ==> " + str(nota_teoria(9.0, None)))

#Test B

print("9.1, 7.2, 8.1 ==> " + str(nota_cuatrimestre((9.1,7.2),8.1)))
print("4.0, 6.0, 5.0 ==> " + str(nota_cuatrimestre((4.0,6.0),5.0)))
print("4.0, 3.0, None ==> " + str(nota_cuatrimestre((4.0,3.0),None)))
print("None, 3.0, None ==> " + str(nota_cuatrimestre((None,3.0),None)))
print("9.0, None, 4.5 ==> " + str(nota_cuatrimestre((9.0,None),4.5)))

#Test C

print("notas teoría: 9.6, 9.9, 10.0, 9.8, notas_práctico: 9.7, 9.5 ==> " + str(nota_continua((9.6, 9.9, 10.0, 9.8),(9.7, 9.5))))
print("notas teoría: 4.4, 4.9, 5.1, 4.7, notas_práctico: 4.6, 4.8 ==> " + str(nota_continua((4.4, 4.9, 5.1, 4.7),(4.6,4.8))))
print("notas teoría: 4.0, 6.0, 4.0, 3.0, notas_práctico: 5.0, None ==> " + str(nota_continua((4.0, 6.0, 4.0, 3.0),(5.0,None))))
print("notas teoría: 9.0, None, 4.0, 3.0, notas_práctico: 4.5, None ==> " + str(nota_continua((9.0, None, 4.0, 3.0),(4.5,None))))