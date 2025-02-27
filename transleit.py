import random
from vocabylary import vocabylary

def lista_opciones(opcion_usuario):
    # longitud del dict
    cantidad = len(vocabylary)

    match opcion_usuario:
        case 1:
            print('')
            print(f'{cantidad} palabras'.center(50, '-'))
            for key, value in vocabylary.items():
                print(f'{key}={value}')
        case 2:
            # mensaje a mostrar
            print('')
            print(f' Traduce las siguientes {len(vocabylary)} palabras al inglés '.center(60, '-'))

            '''
            En este bluque se realiza la comparacion
            del dato dado por el usuario con los
            datos almacenados en el modulo vocabylary.
        
            Si este presenta un error tendra un mensaje
            en donde se le muestra la manera correcta de escribir
            la palabra y la manera incorrecta en que digito la traduccion.
        
            Si todo esta bien, al usuario se le mostrara
            mensaje 'Very nice'.
            '''
            while cantidad > 0:
                # castin del diccionario a lista
                values = list(vocabylary.keys())
                # generamos clave aleatoria
                generateWord = random.sample(values, 1)[0]
                # extraemos valor relacionado a la clave
                wordValue = vocabylary[generateWord]

                # Solicitamos al usuario la palabra
                print(f'{wordValue}:\n', end='')
                inputWord = input('-> ').lower()

                # verificamos si existe la palbra dada
                if inputWord in vocabylary:
                    # validamos si la palabra dada coicide con el valor dado
                    for key, value in vocabylary.items():
                        if inputWord == key and wordValue == value:
                            print(f'Very nice\n')
                            # eliminamos la palabra del dict
                            vocabylary.pop(key)
                            cantidad = len(vocabylary)
                            break
                        elif inputWord == key and wordValue != value:
                            print(f'Incorrect, is: ({generateWord}) not: ({inputWord}).\n')
                else:
                    print(f'Incorrect\n is: ({generateWord}) not: ({inputWord})\n')
            else:
                print('Vocabulario consolidado.')

while True:
    print(f'\nSelecciona una de las siguientes opciones:\n'
              f'\n  1. Listar vocabulario.'
              f'\n  2. Practicar traducción (español-ingles).'
              f'\n  3. Salir.\n')

    try:
        opcion = int(input('-> '))

        if opcion < 1 or opcion > 3:
            raise ValueError()

        elif opcion == 3:
            print(f'\nHasta la proxima.')
            break
        else:
            lista_opciones(opcion)

    except ValueError as e:
        print('\n¡¡¡Por favor, proprociona un numero de 1 a 3!!!')