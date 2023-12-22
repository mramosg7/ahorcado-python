from random import choice
import os
import time
palabras_posibles = ['gato', 'perro', 'python', 'programacion', 'datos', 'computadora', 'aleatorio', 'lista']

palabra = choice(palabras_posibles)
intentos = 6
pizarraPalabra = list('_' for n in palabra)
def preguntarLetra():
    letraPregunta = ''
    while not letraPregunta.isalpha():
        letraPregunta = input("\tDime un letra: ")
    return letraPregunta

def comprobarLetra(letra):
    letraAnadida = False
    for index,l in enumerate(palabra):
        if letra == l:
            pizarraPalabra[index] = l
            letraAnadida = True

    return letraAnadida

def comprobarWin():
    global pizarraPalabra
    for p in pizarraPalabra:
        if not p.isalpha():
            return False
    return True
def draw():
    os.system('cls')
    global intentos
    if intentos == 6:
        print("\t  +---+")
        print("\t  |   |")
        print("\t      |")
        print("\t      |")
        print("\t      |")
        print("\t      |")
        print("\t=========")
    elif intentos == 5:
        print("\t  +---+")
        print("\t  |   |")
        print("\t  O   |")
        print("\t      |")
        print("\t      |")
        print("\t      |")
        print("\t=========")
    elif intentos == 4:
        print("\t  +---+")
        print("\t  |   |")
        print("\t  O   |")
        print("\t  |   |")
        print("\t      |")
        print("\t      |")
        print("\t=========")
    elif intentos == 3:
        print("\t  +---+")
        print("\t  |   |")
        print("\t  O   |")
        print("\t /|   |")
        print("\t      |")
        print("\t      |")
        print("\t=========")
    elif intentos == 2:
        print("\t  +---+")
        print("\t  |   |")
        print("\t  O   |")
        print("\t /|\\  |")
        print("\t      |")
        print("\t      |")
        print("\t=========")
    elif intentos == 1:
        print("\t  +---+")
        print("\t  |   |")
        print("\t  O   |")
        print("\t /|\\  |")
        print("\t /    |")
        print("\t      |")
        print("\t=========")
    if not comprobarWin():

        print("\t"+" ".join(pizarraPalabra))
        letra = preguntarLetra()

        if not comprobarLetra(letra):
           intentos -= 1
        if intentos >0:
            draw()
        else:
            os.system('cls')
            print("\t  +---+")
            print("\t  |   |")
            print("\t  O   |")
            print("\t /|\\  |")
            print("\t / \\  |")
            print("\t      |")
            print("\t=========")
            print("\tHas perdido")
            time.sleep(2)
    else:
        print("\t" + " ".join(pizarraPalabra))
        print("\tHas ganado")
        time.sleep(2)



draw()