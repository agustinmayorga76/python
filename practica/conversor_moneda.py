#Primer programa para aprender a usar el código de Python ...

mensaje = """Bienvenido  al conversor de moneda
ingrese 1 si desea convertir dolares a pesos
ingrese 2 si desea convertir pesos a dolares: """
print (mensaje)
operacion = float(input())                      # convierto el texto ingresado a un float y le asigno el nombre operacion


print("ingrese en pesos argentinos el precio del dolar")
precio_dolar = float(input())                   # convierto el texto ingresado a un float
                                                # precio_dolar=float(precio_dolar)  esta operacion está resumida en el párrafo anterior


if operacion == 1 :

    numero = float(input("¿cuantos pesos desea convertir en dólares?: ")) # convierto el texto ingresado a un float
                                               # numero = float(numero) esta operacion está resumida en el párrafo anterior


    dolares = numero / precio_dolar
    dolares = str(dolares)                     #convierto mi numero a un string para que me muestre el monto exacto

    print("Usted tiene " + dolares + " dólares")

else :

    dolar = float( input("¿cuántos dólares desea convertir en pesos?: ") )# convierto el texto ingresado a un float
                                                # dolar = float(dolar) esta operacion está resumida en el párrafo anterior

    pesos = dolar * precio_dolar
    pesos = str(pesos)                          # convierto el texto ingresado a un float

    print ("usted tiene " + pesos + "pesos")
