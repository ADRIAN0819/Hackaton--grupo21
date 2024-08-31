def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    while True:
        operacion = input("Escribe tu operación: ")
        if operacion.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            resultado = eval(operacion)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculadora()