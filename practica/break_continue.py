def run():
    
    # for contador in range (1000):
    #    if contador % 2 != 0:         si el resto es diferente de cero,me salto lo q esta despues de continue y sigo ejecuntando el ciclo 
    #        continue
    #    print(contador)

    #for i in range (10000):
    #    print(i)
    #    if i == 5678:
    #        break        se cumple la condicion y termino de ejecutar el for

    texto = input('Escribe un texto: ')
    for letra in texto :
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    run()