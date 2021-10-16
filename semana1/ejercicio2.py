from random import randint


def adivina_numero():
    num = randint(1,10)

    adivinado = False
    intentos = 0

    while not adivinado:
        intentos += 1
        ent = int(input('Introduzca un número entre 1 y 10: '))

        if ent < 1 or ent > 10:
            print("El número introducido está fuera del rango 1-10. Vuelva a intentarlo")
        else:
            if ent == num:
                print("CORRECTO. Has acertado en " + str(intentos) + " intentos.")
                adivinado = True
            elif ent < num:
                print("El número introducido es menor que el buscado. Vuelva a intentarlo.")
            else:
                print("El número introducido es mayor que el buscado. Vuelva a intentarlo.")

    return
