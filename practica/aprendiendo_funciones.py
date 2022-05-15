#Con este programita aprendo a NO repetir código. Para eso creo una función

def mensaje(teclado):
     print("hola")
     print("aaa")
     print("elegite la opcion " + teclado)
     print("chaau")

teclado = input("ingrese  una opcion del 1 al 3:  ")
if teclado == '1': 
     mensaje(teclado)
elif teclado == '2':
     mensaje(teclado)
elif teclado == '3':
     mensaje(teclado)
else :
    print("esta opcion no es correcta")


'''práctica para invocar una funcion corta pero resumida'''

# def suma (a,b):
#     print ("se suman dos numeros")
#     resultado = a + b 
#     return resultado


# print(suma (2,4))