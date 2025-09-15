class Calculadora:
    def __init__(self):
        pass 
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b


mi_calculadora = Calculadora()

# Ejemplos de uso
print("Suma: ", mi_calculadora.sumar(10, 5))
print("Resta: ", mi_calculadora.restar(10, 5))
print("Multiplicación: ", mi_calculadora.multiplicar(10, 5))
print("División: ", mi_calculadora.dividir(10, 0)) 
