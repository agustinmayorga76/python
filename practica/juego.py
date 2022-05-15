import random  #libreria q me permite importar numeros aleatorios


def run():
    valor = random.randint(1, 100) # puede ser tambien valor = rendint(1,101)
    numero = int(input('ingresa un numero del 1 al 100: '))
    while numero != valor :
        if numero < valor :
          print('El nuemro es mas grande ')
        else: 
          print('El numero es mas chico ')
        numero = int(input('ingresa otro numero: '))
    print('Ganastre!')

  

if __name__ == '__main__' :
    run()