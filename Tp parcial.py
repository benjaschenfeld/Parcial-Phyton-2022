import json
from tkinter import Variable
from xml.etree.ElementTree import QName

# lista = {} # dicccionario
lista = [] # lista
lista.append({
    'nombre': 'Paradise',
    'artista': 'coldplay',
    'letra': 'When she was just a girl she expected the world But it flew away from her reach And the bullets catch in her teeth Life goes on, it gets so heavy The wheel breaks the butterfly'
})


lista.append({
    'nombre' :'jijiji',
    'artista': 'indio solari',
    'letra': '¡No lo soñé! Se enderezó y brindó a tu suerte ¡No lo soñé! Y se ofreció mejor que nunca No mires, por favor Y no prendas la luz La imagen te desfiguró'
})

lista.append({
    'nombre':'Hayya Hayya',
    'artista':'(Better Together) (feat. Trinidad Cardona & DAVIDO)',
    'letra': 'I promise, I promise, I promise you now Everything, everything gonna work out Every tomorrow, no matter what goes down I promise, I promise, I promise you now Gonna be, gonna be sticking around Every tomorrow, no matter what goes down'
})


lista.append({
    'nombre' :'Lindo Viaje',
    'artista':'Tercer cielo',
    'letra':'En el cielo está faltando una estrella Será que tú eres una de ellas Y ahora estás aquí Frente a mí Entonces porque eres tan bella Dios te ha creado tan perfecta No dejo de pensar en ti'
})

lista.append({
    'nombre' :'Let her go',
    'artista':'Passenger',
    'letra':'Well, you only need the light when it s burning low Only miss the sun when it starts to snow Only know you love her when you let her go Only know you ve been high when youre feeling low Only hate the road when you re missing home Only know you love her when you let her go And you let her go'
})
# aca cree el json, que es un arreglo de objetos, en donde por cada 
# posicion del arreglo guardo un objeto y el objetoguarda el nombre, artista y letra de una cancion
# (esta declarado globalmente, lo que quiere decir que lo puedo acceder y manipular de cualquier parte del programa)

def menu():
    #Creo el menu del Programa
    print('\n')
    print('**********Lista de Canciones**********')
    print('\n')
    print('1-Ver Canciones')
    print('\n')
    print('2-Agregar canciones')
    print ('\n')
    print('3-Buscar canciones')
    print ('\n')
    print('4-Editar canciones')
    print ('\n')
    print('5-Exit')
    print ('\n')
    resultado = int(input('Elija una opcion: '))
    funcionalidades(resultado)


def funcionalidades(resultado):
    #Evaluo la accion que quiere hacer el usuario con el programa
    if resultado is 1:
        mostrarCanciones()
    elif resultado is 2:
        agregarCanciones()
    elif resultado is 3:
        buscarCanciones()
    elif resultado is 4:
        editarCanciones()
    else:
        exit()

    #Le paso la variable resultado y capturo la opcion que haya elejido el usuario.
    #A partir de esa opcion llamamos a distintas funciones que realizan dsistintas operaciones


def mostrarCanciones():
    print('\n')
    print('**********Lista de Canciones**********')
    print("\n")
    print('los elementos de la lista son: ')
    print('\n')


    #con mostrar Canciones recorremos el json y lo imprimimos por consola para mosgtrarle las canciones al usurario

    for i in lista:
        print('********************************')
        print("Nombre: " + i['nombre']) # es el indice del for y es el que captura cada cancion del json
        print("Artista: " + i['artista'])
        print("Letra: " + i['letra'])
        print('********************************')  
        print('\n')

    #El for recorre el json global de arriba
    
    resultado = int(input('Elija una opcion: '))
    funcionalidades(resultado)

def agregarCanciones():
    nombre = input('Agregar cancion: ')
    artista = input('Artista: ')
    letra = input('Letra: ')

    #Le pedimos al usuario los datos necesarios para que agregue una cancion 

    lista.append({
        'nombre': nombre,
        'artista': artista,
        'letra': letra
    })

    for cancion in lista:
        if cancion['nombre'] == nombre:
            print('\n')
            print('********************************')
            print("Nombre: " + cancion['nombre']) 
            print("Artista: " + cancion['artista'])
            print("Letra: " + cancion['letra'])
            print('********************************')
            print('\n')
    
    resultado = int(input('Que desea hacer ahora?: '))
    funcionalidades(resultado)

    #Al json le agregamos esa cancion que agrego el usuario con el metodo .append .
    #Despues llamamos a la funcion interfaz para poder mostrar que la cancion se agrego

def buscarCanciones():
    nombre = input('Escribi el nombre de una cancion: ')
    for cancion in lista:
        if cancion['nombre'] == nombre:
            print('Cancion encontrada')
            print('\n')
            print('********************************')
            print("Nombre: " + cancion['nombre']) 
            print("Artista: " + cancion['artista'])
            print("Letra: " + cancion['letra'])
            print('********************************')
            print('\n')
            break
        else: 
            print('La cancion que esta buscando no existe')
            
    resultado = int(input('Elija una opcion: '))
    funcionalidades(resultado)
    
    #Accedimos por posicion al arreglo 
    #Y con el if preguntamos si el atributo nombre del objeto correspondiente
    #A dicha posicion es igual al nombre que ingreso el usuario.
    #Una vez encontrado el nombre el for corta por la sentencia break.

def editarCanciones():
    nombre = input('Que cancion desea editar? (Introduzca el nombre): ')
    for cancion in lista:
        if cancion['nombre'] == nombre:
            
            print('Cancion encontrada')
            nombreEdit = input('Editar nombre: ')
            artistaEdit = input('Editar artista: ')
            letraEdit = input('Editar letra: ')

            cancion['nombre'] = nombreEdit
            cancion['artista'] = artistaEdit
            cancion['letra'] = letraEdit
            print('Editado')

            resultado = int(input('Elija una opcion: '))
            funcionalidades(resultado)
            break    
        else: 
            print('La cancion que esta buscando no existe')
            resultado = int(input('Elija una opcion: '))
            funcionalidades(resultado)

menu()