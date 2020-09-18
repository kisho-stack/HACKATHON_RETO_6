from objetos import Alumno
from objetos import Profesor
from objetos import Notas
from objetos import Salones


def menu():
    print('Bienvenido al Colegio Perez de Cuella')
    print('Selecciona un opción : ')
    print('\t1 -  Registrar Docentes')
    print('\t2 -  Registrar Alumnos') 
    print('\t3 -  Registrar Notas')
    print('\t4 -  Modificar Alumnos') 
    print('\t5 -  Modificar profesor') 
    print('\t6 -  Eliminar Alumnos') 
    print('\t7 -  Eliminar Profesor') 
    print('\t8 -  Ver Docentes')
    print('\t9 -  Ver Alumnos') 
    print('\t10 - Ver Salones')
    print('\t11 - Salir')


def continuar(error=False):
    result = True
    while result:
        if error==True:
            print("No has ingresado una opción correcta")
        opcion = input("¿Deseas continuar con la aplicación? (S/N) >> ")
        if opcion.lower() == "s":
            break
        elif opcion.lower() == "n":
            result = False
            break
        else:
            pass

    return result


def preguntar(pregunta, entero=False):
    while True:
        if entero:
            try:
                dato = int(input(pregunta).strip())
                if dato != '': break
                else: print("No has ingresado ningún número")
            except ValueError:
                print("Debes ingresar un número, intente nuevamente")
        else:
            dato = input(pregunta).strip()
            if dato != '': break
            else: print("No has ingresado ningún texto")

    return dato


try:
    while True:
        menu()
        opcion_menu = input("Ingresa la opción >> ")
        if opcion_menu == "1":
            
            nombre_docente = preguntar("Nombre del docente >> ")
            edad_docente = preguntar("Edad del docente >> ", True)
            profesor = Profesor(nombre_docente,edad_docente)
            profesor.insert_profesor()
            
            if continuar(): pass
            else: break

        elif opcion_menu == "2":
            nombre_alumno = preguntar("Nombre del alumno >> ")
            edad_alumno = preguntar("Edad del Alumno >> ")
            alumno = Alumno(nombre_alumno,edad_alumno)
            alumno.insert_alumno()
            
            if continuar(): pass
            else: break

        elif opcion_menu == "3":
            cantidad_notas = preguntar("Cantidad de notas a registrar >> ", True)
            i = 0
            notas = []
            while i < cantidad_notas:
                notas = preguntar(f"Ingresa la nota n° {i + 1} >> ", True)
                                    
                notas_alumno = Notas(notas)
                notas_alumno.insert_notas()
                i += 1
                                
            if continuar(): pass
            else: break

        elif opcion_menu == "4":
            print('Hola esta es la lista alumnos registrados') 
            alumno = Alumno('','')
            alumno.fetchall_alumno()
            id = int(input("Por favor inserte el id del alumno para actualizar informacion : "))
            nombre_alumno = preguntar("Nombre del alumno >> ")
            edad_alumno = preguntar("Edad del Alumno >> ")
            alumno = Alumno(nombre_alumno,edad_alumno)
            alumno.update_alumno(id)
            
            if continuar(): pass
            else: break
            
        elif opcion_menu == "5":
            print('Hola esta es la lista de profesores registrados') 
            profesor = Profesor('','')
            profesor.fetchall_profesor()
            id = int(input("Por favor inserte el id del profesor para actualizar informacion : "))
            nombre_profesor = preguntar("Nombre del profesor >> ")
            edad_profesor = preguntar("Edad del profesor >> ")
            profesor = Profesor(nombre_profesor,edad_profesor)
            profesor.update_profesor(id)

            if continuar(): pass
            else: break
            
        elif opcion_menu == "6":
            print('Hola esta es la lista alumnos registrados') 
            alumno = Alumno('','')
            alumno.fetchall_alumno()
            id = int(input("Por favor inserte el id del registro que desea eliminar : "))
            alumno.delete_alumno(id)
            
            if continuar(): pass
            else: break
            
        elif opcion_menu == "7":
            print('Hola esta es la lista de profesores registrados') 
            profesor = Profesor('','')
            profesor.fetchall_profesor()
            id = int(input("Por favor inserte el id del registro que desea eliminar : "))
            profesor.delete_profesor(id)

            if continuar(): pass
            else: break
        
        elif opcion_menu == "8":
            
            profesor = Profesor('','')
            profesor.fetchall_profesor()
           
            if continuar(): pass
            else: break
            
        elif opcion_menu == "9":
            
            alumno = Alumno('','')
            alumno.fetchall_alumno()
           
            if continuar(): pass
            else: break
            
        elif opcion_menu == "10":
                        
            salon = Salones()
            salon.fetchall_salones()
           
            if continuar(): pass
            else: break
                   
        elif opcion_menu == "11":
            break
        else:
            if continuar(True): pass
            else: break
        
    print("Gracias por usar el programa")
        
except KeyboardInterrupt:
    print('La aplicación se detuvo')
