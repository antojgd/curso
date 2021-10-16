# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto
# escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(cadena):

    longitud = len(cadena)
    resultado = True

    if longitud > 0:
        mitad = int(longitud / 2)

        i = 0
        while i < mitad:
            if (cadena.upper())[i] != (cadena.upper())[longitud-1-i]:
                resultado = False
                break
            i += 1
    else:
        resultado = False

    if resultado == True:
        print("La cadena introducida " + cadena + " SI es palíndromo")
    else:
        print("La cadena introducida " + cadena + " NO es palíndromo")






