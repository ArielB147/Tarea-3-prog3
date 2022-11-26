import os
from peewee import *

import prettytable
db = SqliteDatabase('personajes de anime.db')


class personajes(Model):
        nombre = CharField(10)
        apellido = CharField(50)
        foto = CharField(50)
        pronunciacion = CharField(50)
        serie = CharField(50)        
        fecha_de_nacimiento = CharField(50)
        poder = CharField(50)
        frase_favorita = CharField(50)
        descripcion_de_su_vestimenta = CharField(50)
        edad = CharField(50)
        altura = CharField(50)
        sexo = CharField(50)
        estado = CharField(50) 
        direccion = CharField(50)
        latitud = IntegerField()
        longitud = IntegerField()

        class Meta:
            database = db
        



def registrar():
    os.system('cls')
    print("""
    
    ██████  ███████  ██████  ██ ███████ ████████ ██████   █████  ██████  
    ██   ██ ██      ██       ██ ██         ██    ██   ██ ██   ██ ██   ██ 
    ██████  █████   ██   ███ ██ ███████    ██    ██████  ███████ ██████  
    ██   ██ ██      ██    ██ ██      ██    ██    ██   ██ ██   ██ ██   ██ 
    ██   ██ ███████  ██████  ██ ███████    ██    ██   ██ ██   ██ ██   ██ 
    
    """)
    print('')
    print('A continuacion ingrese los datos del personaje de anime que desea agregar')
    print('')
    est = personajes()
    est.nombre = input(' Ingrese el nombre')
    print('')
    est.apellido = input(' Ingrese el apellido ')
    print('')
    est.foto = input(' Ingrese la foto del personaje ')
    print('')
    est.pronunciacion = input(' Ingrese la pronunciacion de personaje ')
    print('')
    est.serie = input(' Ingrese la serie del personaje ')
    print('')
    est.fecha = input(' Ingrese la fecha ')
    print('')
    est.poder = input(' Ingrese el poder del personaje ')
    print('')
    est.frace_favorita = input(' Ingrese la frase favorita del personaje ')
    print('')
    est.descripcion_de_vestimenta = input(' Ingrese la descripcion de la vestimenta del personaje ')
    print('')
    est.edad = input(' Ingrese la edad del personaje ')
    print('')
    est.altura = input(' Ingrese la altura ')
    print('')
    est.sexo = input(' Ingrese el sexo del personaje ')
    print('')
    est.estado = input(' Ingrese el estado del personaje ')
    print('')
    est.direccion = input(' Ingrese la direccion del personaje ')
    print('')
    est.latitud = input(' Ingrese la latitud del personaje ')
    print('')
    est.longitud = input(' Ingrese la longitud del personaje ')
    print('')
    est. = input(' Ingrese la fecha ')
    print('')
    est.save()
    input(' Los datos del estudiante se han guardado, precione enter para continuar con el programa')
    print('')
    

db.connect()
db.create_tables([estudiantes])


def modificar():
    os.system('cls')

    print("""


    ████     █████ ████     ███   ██  ██ ███████ █████   █████     
    ██  ██   ██    ██  ██ ██   ██ ██  ██   ██    ██    ██       
    ████     █████ ████   ██   ██ ████     ██    █████  █████   
    ██  ██   ██    ██     ██   ██ ██       ██    ██         ██       
    ██    ██ █████ ██       ███   ██       ██    █████ █████      
       
    """)
   
    print('')
    print(' personajes registrados en la base de datos ')
    print(" ")
    print('')
    for est in personajes.select():
        print(f"   {est.nombre}  {est.apellido}  {est.serie}  {est.genero}  {est.edad} 
        print('')

est = personajes.select().where(personajes.id == id_persoajes).get()

print('')
    est = personajes()
    est.nombre = input(' Ingrese el nombre')
    print('')
    est.apellido = input(' Ingrese el apellido ')
    print('')
    est.foto = input(' Ingrese la foto del personaje ')
    print('')
    est.pronunciacion = input(' Ingrese la pronunciacion de personaje ')
    print('')
    est.serie = input(' Ingrese la serie del personaje ')
    print('')
    est.fecha = input(' Ingrese la fecha ')
    print('')
    est.poder = input(' Ingrese el poder del personaje ')
    print('')
    est.frace favorita = input(' Ingrese la frase favorita del personaje ')
    print('')
    est.descripcion de vestimenta = input(' Ingrese la descripcion de la vestimenta del personaje ')
    print('')
    est.edad = input(' Ingrese la edad del personaje ')
    print('')
    est.altura = input(' Ingrese la altura ')
    print('')
    est.sexo = input(' Ingrese el sexo del personaje ')
    print('')
    est.estado = input(' Ingrese el estado del personaje ')
    print('')
    est.direccion = input(' Ingrese la direccion del personaje ')
    print('')
    est.latitud = input(' Ingrese la latitud del personaje ')
    print('')
    est.longitud = input(' Ingrese la longitud del personaje ')
    print('')
    est. = input(' Ingrese la fecha ')
    print('')
    est.save()
def Datos(campo, valor):
    print('')
    print('el campo ', campo, ' tiene el valor ', valor)
    print('')
    
    new_valor = input(' Ingrese el nuevo valor o deje el el espacio en blando para no modificarlo ')
    if new_valor == '':
        return valor
    else:
        return new_valor

def modificar():
    os.system('cls')

    print("""

    ███    ███  ██████  ██████  ██ ███████ ██  ██████  █████  ██████  
    ████  ████ ██    ██ ██   ██ ██ ██      ██ ██      ██   ██ ██   ██ 
    ██ ████ ██ ██    ██ ██   ██ ██ █████   ██ ██      ███████ ██████  
    ██  ██  ██ ██    ██ ██   ██ ██ ██      ██ ██      ██   ██ ██   ██   
    ██      ██  ██████  ██████  ██ ██      ██  ██████ ██   ██ ██   ██ 
    
    """)

    print('')
    print(' Estudiantes registrados en la base de datos ')
    print(" ")
    print('')
    for est in estudiantes.select():
        print(f"   {est.id}  {est.Matricula}  {est.Nombre}  {est.Apellido}  {est.Nota1}  {est.Nota2}  {(est.Nota1 + est.Nota2) / 2}  {eq((est.Nota1 + est.Nota2) / 2)}  ")
        print('')
    print('')
    id_estu = input(' Ingrese el ID del estudiante a modificar o X para cancelar la modificación ')
    if id_estu == 'x' or id_estu == 'X':
        return False

    est = estudiantes.select().where(estudiantes.id == id_estu).get()

    print('')
    est.Matricula = Datos('Matricula', est.Matricula)
    print('')
    est.Nombre = Datos('Nombre', est.Nombre)
    print('')
    est.Apellido = Datos('Apellido', est.Apellido)
    print('')
    est.Nota1 = Datos('Nota1', est.Nota1)
    print('')
    est.Nota2 = Datos('Nota2', est.Nota2)
    print('')
    est.save()






    def mostrar():
    for est in estudiantes.select():

        print(f"   {est.id}  {est.Nombre}  {est.Apellido}  {est.Nota1}  {est.Nota2}  {(est.Nota1 + est.Nota2) / 2}  {eq((est.Nota1 + est.Nota2) / 2)}  ")
        print('')


def eliminar():
    os.system('cls')
    print("""
    
    ███████ ██      ██ ███    ███ ██ ███    ██  █████  ██████  
    ██      ██      ██ ████  ████ ██ ████   ██ ██   ██ ██   ██ 
    █████   ██      ██ ██ ████ ██ ██ ██ ██  ██ ███████ ██████  
    ██      ██      ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ ██   ██ 
    ███████ ███████ ██ ██      ██ ██ ██   ████ ██   ██ ██   ██ 
    """)


    print('')
    mostrar()
    print('')


    id_estu = input(' Ingrese el ID del estudiante a eliminar o X para cancelar la modificación ')
    if id_estu == 'x' or id_estu == 'X':
        return False

    est = estudiantes.select().where(estudiantes.id == id_estu).get()
    est.delete_instance()
    print('')
    print(f" El estudiante {est.id} {est.Nombre} {est.Apellido} se ha borrado de la base de datos")
    print('')










def exportar():
    arh.open('estudiantes.html', 'w+')
    arh.write(f"""
    
    
    
    
    """)
    a.close
