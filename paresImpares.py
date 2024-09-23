def paresImpares(numero):
 #Aqui agrego las condicionales para verificar si un numero es par o impar
if numero % 2 == 0:
        return True
    else:
        return False
     
# Función para imprimir números pares e impares del 1 al 50
def imprimir_pares_impares():
    # Crear listas vacías para guardar los números pares e impares
    numeros_pares = []
    numeros_impares = []

    # Bucle para recorrer los números del 1 al 50

            # Si es par, agregarlo a la lista de pares
            numeros_pares.append(numero)
        else:
            # Si no es par, es impar, así que lo agregamos a la lista de impares
            numeros_impares.append(numero)
    
    # Imprimir los números pares e impares en la consola
    print("Números pares del 1 al 50:")
    print(numeros_pares)
    
    print("\nNúmeros impares del 1 al 50:")
    print(numeros_impares)

# Llamar a la función para ejecutar el código
imprimir_pares_impares()

