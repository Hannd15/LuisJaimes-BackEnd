# Calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

if __name__ == "__main__":
    # Solicitar al usuario ingresar dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar operaciones
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    resultado_multiplicacion = multiplicacion(num1, num2)

    # Mostrar resultados
    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")
