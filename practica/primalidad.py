#un numero primo se puede dividir SOLAMENTE por uno y por si mismo

def es_primo(numero):
    if numero == 1:
        return False
    else : 
        contador = 0

    for i in range(1,numero + 1):
        if i == 1 or i == numero :
            continue    #si se cumple esta condicion, nos saltamos esta vuelta del ciclo
        if numero % i == 0:  #  si no nos saltamos la velta del ciclo, seguimos con esta linea
            contador += 1 
    if contador == 0:
        return True
    else:
        return False


def main():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print("Es primo ")
    else :
        print('No es primo')


if __name__ == '__main__':
    main()