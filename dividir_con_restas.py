"""
Dividir con restas
"""

# Entradas
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

# Proceso
if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:  
    cociente = 0
    acumulador = 0  
    while acumulador + divisor <= dividendo:
        acumulador += divisor  
        cociente += 1
    residuo = dividendo - acumulador

    # Salida
    print(f"El cociente es {cociente} y el residuo es {residuo}.")
