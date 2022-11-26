import os
os.system('cls')
import funtions



rep = True

while rep == True:
    os.system('cls')
    print("""

        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████  
        ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██ 
        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██ ██ ██ 
        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██ ██ ██ 
        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   █ ████  


        Base de datos de los estudiantes:

        1.Registra un personaje de anime.

        2.reportes.

        3.configuracion.

        4.Exportar datos de los estudiantes a un archivo HTML.

        5.acerca de.

        6.salir el programa.

        """)
    

    respuesta = input('ingrese el numero de la accion que desea realizar ')




    if respuesta == '1':
        a = True
        while a == True:
            funtions.registrar()
            i = input('¿Desea agregar otro personaje de anime a la base de datos?  S  o  N ')
            print('')

            if i == 'n' or i == 'N':
                a = False
        
    elif respuesta == '2':
        funtions.modificar()

    elif respuesta == '3':
        funtions.eliminar()

    elif respuesta == '4':
        funtions.exportar()

    elif respuesta ==  '5':
        funtions.respuesta()

    elif respuesta == '6':
        rep = False
        print("""
         █████  ██████  ██  ██████  ███████ 
        ██   ██ ██   ██ ██ ██    ██ ██      
        ███████ ██   ██ ██ ██    ██ ███████ 
        ██   ██ ██   ██ ██ ██    ██      ██ 
        ██   ██ ██████  ██  ██████  ███████ 
        """)

        input('presione enter para salir del programa')

    else:
        print('la opcion que usted a ingresado no se encuantra disponible eliga otra opción')
        input('')
    print('')
    r = input('¿le gustaria elegir otra opcion del programa? S o M ')
    if r == 'M' or r == 'n':
        rep = False