# Actividad 2 

# Integrantes: Tamayo Juan Alejandro,Sergio Andres Bustos,Jojoa Sebastian Meneses,Javier Steven Solis Ruiz
indicador=int(input("cuantos estudiantes vas a ingresar?(maximo 5): "))
estudiantes=[]
if indicador==1:
    nombre_estudiante=str(input("ingresa el nombre del estudiante: "))
    nota_evaluacion_1=float(input("ingresa la nota de la primera evaluacion: "))
    nota_evaluacion_2=float(input("ingresa la nota de la segunda  evaluacion: "))
    nota_evaluacion_3=float(input("ingresa la nota de la tercera evaluacion: "))
    promedio=nota_evaluacion_1+nota_evaluacion_2+nota_evaluacion_3/3
    if promedio>=3.5:
        situacion="Aprobado"
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio<=3.4 and promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    estudinate1={
    "nombre":nombre_estudiante,
    "notas":(nota_evaluacion_1,nota_evaluacion_2,nota_evaluacion_3),
    "promedio":promedio,
    "situacion":situacion
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante} tiene un promedio de {promedio}, descuerdo a este ultimo dato podemos decir que {estudinate1['situacion']}")
elif indicador==2:
    nombre_estudiante=str(input("ingresa el nombre del estudiante: "))
    nota_evaluacion_1=float(input("ingresa la nota de la primera evaluacion: "))
    nota_evaluacion_2=float(input("ingresa la nota de la segunda  evaluacion: "))
    nota_evaluacion_3=float(input("ingresa la nota de la tercera evaluacion: "))
    promedio=nota_evaluacion_1+nota_evaluacion_2+nota_evaluacion_3/3
    if promedio>=3.5:
        situacion="Aprobado"
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio<=3.4 and promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    estudinate1={
    "nombre":nombre_estudiante,
    "notas":(nota_evaluacion_1,nota_evaluacion_2,nota_evaluacion_3),
    "promedio":promedio,
    "situacion":situacion
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante} tiene un promedio de {promedio}, descuerdo a este ultimo dato podemos decir que {estudinate1['situacion']}")
    #2
    print("                                                                                                                                   ")
    nombre_estudiante2=str(input("ingresa el nombre del estudiante 2: "))
    nota_evaluacion_12=float(input("ingresa la nota de la primera evaluacion 2: "))
    nota_evaluacion_22=float(input("ingresa la nota de la segunda  evaluacion 2: "))
    nota_evaluacion_32=float(input("ingresa la nota de la tercera evaluacion 2: "))
    promedio2=nota_evaluacion_12+nota_evaluacion_22+nota_evaluacion_32/3
    if promedio2>=3.5:
        situacion2="Aprobado"
    if promedio2>=3.5:
        situacion2="Aprobado"
    elif promedio2<=3.4 and promedio2>=2.5:
        situacion2="En recuperacion"
    else:
        situacion2="Reprobado"
    estudinate2={
    "nombre2":nombre_estudiante2,
    "notas2":(nota_evaluacion_12,nota_evaluacion_22,nota_evaluacion_32),
    "promedio2":promedio2,
    "situacion2":situacion2
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante2} tiene un promedio de {promedio2}, descuerdo a este ultimo dato podemos decir que {estudinate2['situacion2']}")
elif indicador==3:
    nombre_estudiante=str(input("ingresa el nombre del estudiante: "))
    nota_evaluacion_1=float(input("ingresa la nota de la primera evaluacion: "))
    nota_evaluacion_2=float(input("ingresa la nota de la segunda  evaluacion: "))
    nota_evaluacion_3=float(input("ingresa la nota de la tercera evaluacion: "))
    promedio=nota_evaluacion_1+nota_evaluacion_2+nota_evaluacion_3/3
    if promedio>=3.5:
        situacion="Aprobado"
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio<=3.4 and promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    estudinate1={
    "nombre":nombre_estudiante,
    "notas":(nota_evaluacion_1,nota_evaluacion_2,nota_evaluacion_3),
    "promedio":promedio,
    "situacion":situacion
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante} tiene un promedio de {promedio}, descuerdo a este ultimo dato podemos decir que {estudinate1['situacion']}")
    #2
    print("                                                                                                                               ")
    nombre_estudiante2=str(input("ingresa el nombre del estudiante 2: "))
    nota_evaluacion_12=float(input("ingresa la nota de la primera evaluacion 2: "))
    nota_evaluacion_22=float(input("ingresa la nota de la segunda  evaluacion 2: "))
    nota_evaluacion_32=float(input("ingresa la nota de la tercera evaluacion 2: "))
    promedio2=nota_evaluacion_12+nota_evaluacion_22+nota_evaluacion_32/3
    if promedio2>=3.5:
        situacion2="Aprobado"
    if promedio2>=3.5:
        situacion2="Aprobado"
    elif promedio2<=3.4 and promedio2>=2.5:
        situacion2="En recuperacion"
    else:
        situacion2="Reprobado"
    estudinate2={
    "nombre2":nombre_estudiante2,
    "notas2":(nota_evaluacion_12,nota_evaluacion_22,nota_evaluacion_32),
    "promedio2":promedio2,
    "situacion2":situacion2
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante2} tiene un promedio de {promedio2}, descuerdo a este ultimo dato podemos decir que {estudinate2['situacion2']}")
    #3
    print("                                                                                                                                   ")
    nombre_estudiante3=str(input("ingresa el nombre del estudiante 3: "))
    nota_evaluacion_13=float(input("ingresa la nota de la primera evaluacion 3: "))
    nota_evaluacion_23=float(input("ingresa la nota de la segunda  evaluacion 3: "))
    nota_evaluacion_33=float(input("ingresa la nota de la tercera evaluacion 3: "))
    promedio3=nota_evaluacion_13+nota_evaluacion_23+nota_evaluacion_33/3
    if promedio3>=3.5:
        situacion3="Aprobado"
    if promedio3>=3.5:
        situacion3="Aprobado"
    elif promedio3<=3.4 and promedio3>=2.5:
        situacion3="En recuperacion"
    else:
        situacion3="Reprobado"
    estudinate3={
    "nombre3":nombre_estudiante3,
    "notas3":(nota_evaluacion_13,nota_evaluacion_23,nota_evaluacion_33),
    "promedio3":promedio3,
    "situacion3":situacion3
    }
    estudiantes.append(estudinate3)
    print(f"el estudiante {nombre_estudiante3} tiene un promedio de {promedio3}, descuerdo a este ultimo dato podemos decir que {estudinate3['situacion3']}")
elif indicador==4:
    nombre_estudiante=str(input("ingresa el nombre del estudiante: "))
    nota_evaluacion_1=float(input("ingresa la nota de la primera evaluacion: "))
    nota_evaluacion_2=float(input("ingresa la nota de la segunda  evaluacion: "))
    nota_evaluacion_3=float(input("ingresa la nota de la tercera evaluacion: "))
    promedio=nota_evaluacion_1+nota_evaluacion_2+nota_evaluacion_3/3
    if promedio>=3.5:
        situacion="Aprobado"
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio<=3.4 and promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    estudinate1={
    "nombre":nombre_estudiante,
    "notas":(nota_evaluacion_1,nota_evaluacion_2,nota_evaluacion_3),
    "promedio":promedio,
    "situacion":situacion
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante} tiene un promedio de {promedio}, descuerdo a este ultimo dato podemos decir que {estudinate1['situacion']}")
    #2
    print("                                                                                                                               ")
    nombre_estudiante2=str(input("ingresa el nombre del estudiante 2: "))
    nota_evaluacion_12=float(input("ingresa la nota de la primera evaluacion 2: "))
    nota_evaluacion_22=float(input("ingresa la nota de la segunda  evaluacion 2: "))
    nota_evaluacion_32=float(input("ingresa la nota de la tercera evaluacion 2: "))
    promedio2=nota_evaluacion_12+nota_evaluacion_22+nota_evaluacion_32/3
    if promedio2>=3.5:
        situacion2="Aprobado"
    if promedio2>=3.5:
        situacion2="Aprobado"
    elif promedio2<=3.4 and promedio2>=2.5:
        situacion2="En recuperacion"
    else:
        situacion2="Reprobado"
    estudinate2={
    "nombre2":nombre_estudiante2,
    "notas2":(nota_evaluacion_12,nota_evaluacion_22,nota_evaluacion_32),
    "promedio2":promedio2,
    "situacion2":situacion2
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante2} tiene un promedio de {promedio2}, descuerdo a este ultimo dato podemos decir que {estudinate2['situacion2']}")
    #3
    print("                                                                                                                                   ")
    nombre_estudiante3=str(input("ingresa el nombre del estudiante 3: "))
    nota_evaluacion_13=float(input("ingresa la nota de la primera evaluacion 3: "))
    nota_evaluacion_23=float(input("ingresa la nota de la segunda  evaluacion 3: "))
    nota_evaluacion_33=float(input("ingresa la nota de la tercera evaluacion 3: "))
    promedio3=nota_evaluacion_13+nota_evaluacion_23+nota_evaluacion_33/3
    if promedio3>=3.5:
        situacion3="Aprobado"
    if promedio3>=3.5:
        situacion3="Aprobado"
    elif promedio3<=3.4 and promedio3>=2.5:
        situacion3="En recuperacion"
    else:
        situacion3="Reprobado"
    estudinate3={
    "nombre3":nombre_estudiante3,
    "notas3":(nota_evaluacion_13,nota_evaluacion_23,nota_evaluacion_33),
    "promedio3":promedio3,
    "situacion3":situacion3
    }
    estudiantes.append(estudinate3)
    print(f"el estudiante {nombre_estudiante3} tiene un promedio de {promedio3}, descuerdo a este ultimo dato podemos decir que {estudinate3['situacion3']}")
    #4
    print("                                                                                                                                   ")
    nombre_estudiante4=str(input("ingresa el nombre del estudiante 4: "))
    nota_evaluacion_14=float(input("ingresa la nota de la primera evaluacion 4: "))
    nota_evaluacion_24=float(input("ingresa la nota de la segunda  evaluacion 4: "))
    nota_evaluacion_34=float(input("ingresa la nota de la tercera evaluacion 4: "))
    promedio4=nota_evaluacion_14+nota_evaluacion_24+nota_evaluacion_34/3
    if promedio4>=3.5:
        situacion4="Aprobado"
    if promedio4>=3.5:
        situacion4="Aprobado"
    elif promedio4<=3.4 and promedio4>=2.5:
        situacion4="En recuperacion"
    else:
        situacion4="Reprobado"
    estudinate4={
    "nombre4":nombre_estudiante4,
    "notas4":(nota_evaluacion_14,nota_evaluacion_24,nota_evaluacion_34),
    "promedio4":promedio4,
    "situacion4":situacion4
    }
    estudiantes.append(estudinate4)
    print(f"el estudiante {nombre_estudiante4} tiene un promedio de {promedio4}, descuerdo a este ultimo dato podemos decir que {estudinate4['situacion4']}")
elif indicador==5:
    nombre_estudiante=str(input("ingresa el nombre del estudiante: "))
    nota_evaluacion_1=float(input("ingresa la nota de la primera evaluacion: "))
    nota_evaluacion_2=float(input("ingresa la nota de la segunda  evaluacion: "))
    nota_evaluacion_3=float(input("ingresa la nota de la tercera evaluacion: "))
    promedio=nota_evaluacion_1+nota_evaluacion_2+nota_evaluacion_3/3
    if promedio>=3.5:
        situacion="Aprobado"
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio<=3.4 and promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    estudinate1={
    "nombre":nombre_estudiante,
    "notas":(nota_evaluacion_1,nota_evaluacion_2,nota_evaluacion_3),
    "promedio":promedio,
    "situacion":situacion
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante} tiene un promedio de {promedio}, descuerdo a este ultimo dato podemos decir que {estudinate1['situacion']}")
    #2
    print("                                                                                                                               ")
    nombre_estudiante2=str(input("ingresa el nombre del estudiante 2: "))
    nota_evaluacion_12=float(input("ingresa la nota de la primera evaluacion 2: "))
    nota_evaluacion_22=float(input("ingresa la nota de la segunda  evaluacion 2: "))
    nota_evaluacion_32=float(input("ingresa la nota de la tercera evaluacion 2: "))
    promedio2=nota_evaluacion_12+nota_evaluacion_22+nota_evaluacion_32/3
    if promedio2>=3.5:
        situacion2="Aprobado"
    if promedio2>=3.5:
        situacion2="Aprobado"
    elif promedio2<=3.4 and promedio2>=2.5:
        situacion2="En recuperacion"
    else:
        situacion2="Reprobado"
    estudinate2={
    "nombre2":nombre_estudiante2,
    "notas2":(nota_evaluacion_12,nota_evaluacion_22,nota_evaluacion_32),
    "promedio2":promedio2,
    "situacion2":situacion2
    }
    estudiantes.append(estudinate1)
    print(f"el estudiantes {nombre_estudiante2} tiene un promedio de {promedio2}, descuerdo a este ultimo dato podemos decir que {estudinate2['situacion2']}")
    #3
    print("                                                                                                                                   ")
    nombre_estudiante3=str(input("ingresa el nombre del estudiante 3: "))
    nota_evaluacion_13=float(input("ingresa la nota de la primera evaluacion 3: "))
    nota_evaluacion_23=float(input("ingresa la nota de la segunda  evaluacion 3: "))
    nota_evaluacion_33=float(input("ingresa la nota de la tercera evaluacion 3: "))
    promedio3=nota_evaluacion_13+nota_evaluacion_23+nota_evaluacion_33/3
    if promedio3>=3.5:
        situacion3="Aprobado"
    if promedio3>=3.5:
        situacion3="Aprobado"
    elif promedio3<=3.4 and promedio3>=2.5:
        situacion3="En recuperacion"
    else:
        situacion3="Reprobado"
    estudinate3={
    "nombre3":nombre_estudiante3,
    "notas3":(nota_evaluacion_13,nota_evaluacion_23,nota_evaluacion_33),
    "promedio3":promedio3,
    "situacion3":situacion3
    }
    estudiantes.append(estudinate3)
    print(f"el estudiante {nombre_estudiante3} tiene un promedio de {promedio3}, descuerdo a este ultimo dato podemos decir que {estudinate3['situacion3']}")
    #4
    print("                                                                                                                                   ")
    nombre_estudiante4=str(input("ingresa el nombre del estudiante 4: "))
    nota_evaluacion_14=float(input("ingresa la nota de la primera evaluacion 4: "))
    nota_evaluacion_24=float(input("ingresa la nota de la segunda  evaluacion 4: "))
    nota_evaluacion_34=float(input("ingresa la nota de la tercera evaluacion 4: "))
    promedio4=nota_evaluacion_14+nota_evaluacion_24+nota_evaluacion_34/3
    if promedio4>=3.5:
        situacion4="Aprobado"
    if promedio4>=3.5:
        situacion4="Aprobado"
    elif promedio4<=3.4 and promedio4>=2.5:
        situacion4="En recuperacion"
    else:
        situacion4="Reprobado"
    estudinate4={
    "nombre4":nombre_estudiante4,
    "notas4":(nota_evaluacion_14,nota_evaluacion_24,nota_evaluacion_34),
    "promedio4":promedio4,
    "situacion4":situacion4
    }
    estudiantes.append(estudinate4)
    print(f"el estudiante {nombre_estudiante4} tiene un promedio de {promedio4}, descuerdo a este ultimo dato podemos decir que {estudinate4['situacion4']}")
    #5
    print("                                                                                                                                   ")
    nombre_estudiante5=str(input("ingresa el nombre del estudiante 5: "))
    nota_evaluacion_15=float(input("ingresa la nota de la primera evaluacion 5: "))
    nota_evaluacion_25=float(input("ingresa la nota de la segunda  evaluacion 5: "))
    nota_evaluacion_35=float(input("ingresa la nota de la tercera evaluacion 5: "))
    promedio5=nota_evaluacion_15+nota_evaluacion_25+nota_evaluacion_35/3
    if promedio5>=3.5:
        situacion5="Aprobado"
    if promedio5>=3.5:
        situacion5="Aprobado"
    elif promedio5<=3.4 and promedio5>=2.5:
        situacion5="En recuperacion"
    else:
        situacion5="Reprobado"
    estudinate5={
    "nombre5":nombre_estudiante5,
    "notas5":(nota_evaluacion_15,nota_evaluacion_25,nota_evaluacion_35),
    "promedio5":promedio5,
    "situacion5":situacion5
    }
    estudiantes.append(estudinate5)
    print(f"el estudiante {nombre_estudiante5} tiene un promedio de {promedio5}, descuerdo a este ultimo dato podemos decir que {estudinate5['situacion5']}")
else:
    print("sintax error, posiblemente psuite mas de 5 estudiantes")