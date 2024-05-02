import random
import string

from palabras import palabras
from diagramas_ahorcado import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #Seleccionar palabra al azar de la lista de palabras validas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)


def ahorcado ():

    print("===================================")
    print(" Bienvenido al juego del Arhocado! ")
    print("===================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() #no se puede escribir un par de llaves vacio
    abc = set(string.ascii_uppercase)

    
    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"te quedan {vidas} vidas y has usado estas letras: {''.join(letras_adivinadas)}")
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar estado del ahorcado
        print (vidas_diccionario_visual [vidas])
        #Mostrar las letras separadsa por un espacio
        print (f"Palabra: {''.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario esta en el abc y no esta en el conjunto de letras que ya se han ingresado, se anade la letra al conjunto de letras ingresadas. Ahi se restan conjuntos, le sacamos elementos a ese conjunto. letras que estan el abc que no estan en conjunto de letras adivinadas.
        if letra_usuario in abc - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #si la letra esta en la palabra o no
            #si la letra que escogio el user esta en letras por adivinar, se la saca de letras por adivinar
            #si no esta en la palabra, quitar una vida al user
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            #si no esta la letra en la palabra
            else:
                vidas = vidas - 1
                #o tambien se puede poner vidas -= 1, seria resta uno antes de asignar el resultado a la misma variable, cualqueir de las dos.
                print(f"\n Tu letra, {letra_usuario} no esta en la palabra.")
        #si la letra escogida por el user ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print ("\nYa escogista esa letra. Por favor escoge una letra nueva.")
        else:
            print ("\nEsta letra no es valida.")

    #el juego llega a esta linea cuando se adivinan todas las letras de la palabra o cuando se agotan las vidas del juegador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    #si este no es el caso el ljugador gano
    else:
        print(f"Excelente! Adivinaste la palabra {palabra}!")


ahorcado()