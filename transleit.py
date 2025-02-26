import random
from vocabylary import vocabylary

# longitud del dict
cantidad = len(vocabylary)

# mensaje a mostrar
print(f' Traduce las siguientes {len(vocabylary)} palabras al inglés '.center(60, '-'))
while cantidad > 0:
    values = list(vocabylary.keys())
    generateWord = random.sample(values, 1)[0]
    wordValue = vocabylary[generateWord]

    # Solicitamos al usuario la palabra
    print(f'{wordValue}:\n', end= '')
    inputWord = input('-> ').lower()

    # verificamos si existe la palbra dada
    if inputWord in vocabylary:
        # validamos si la palabra dada coicide con el valor dado
        for key, value in vocabylary.items():
            if inputWord == key and wordValue == value:
                print(f'Very nice\n')
                # eliminamos la palabra del dict
                vocabylary.pop(key)
                cantidad=len(vocabylary)
                break
            elif inputWord == key and wordValue != value:
                print(f'Incorrect, is: ({generateWord}) not: ({inputWord}).\n')
    else:
        print(f'Incorrect\n is: ({generateWord}) not: ({inputWord})\n')
else:
    print('Vocabulario consolidado.')