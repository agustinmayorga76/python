def palindromo(palabra):
    palabra = palabra.replace(' ','')            #elimino los espacios por "nada"
    palabra = palabra.lower()                    #paso todo a minuscula
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():                                       #funcion inicial que arraca el programa. SIEMPRE hay q crearla. puede ser tambien main()
    palabra = input ('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
    
                                                 #siempre se deja dos espacios entre funcion y funcion
if __name__ == '__main__':                       #punto de entrada de python.Siempre empieza a correr desde acá
    run()                                        #enseguida el programa empieza a correr a funcion main

