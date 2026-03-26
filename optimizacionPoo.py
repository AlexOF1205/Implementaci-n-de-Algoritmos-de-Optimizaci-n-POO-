import math

# Funciones

class FuncionCuadratica:
    def evaluar(self, x):
        return x**2 - 4*x + 4

class FuncionTrigonometrica:
    def evaluar(self, x):
        return x + math.sin(x)


class FuncionPolinomial:
    def evaluar(self, x):
        return x**4 - 14*x**3 + 60*x**2 - 70*x

    
# Optimizador

class Optimizador:
    def __init__(self, funcion, a, b, precision):
        self.__funcion = funcion
        self.__limiteA = a
        self.__limiteB = b
        self.__precision = precision
    
    def busqueda_exhaustiva(self):
        n = int((self.__limiteB - self.__limiteA)/self.__precision)
        delta_x = (self.__limiteB - self.__limiteA)/n
        x0 = self.__limiteA
        x1 = x0 + delta_x
        x2 = x1 + delta_x

        while x2 <= self.__limiteB:
            if self.__funcion.evaluar(x0)>self.__funcion.evaluar(x1) and self.__funcion.evaluar(x1)<self.__funcion.evaluar(x2):
                return x1, self.__funcion.evaluar(x1)
            else:
                x0 = x1
                x1 = x2
                x2 = x1 + delta_x

        return self.__limiteA, self.__funcion.evaluar(self.__limiteA)

# Main

opt1 = Optimizador(FuncionCuadratica(), 0, 5, 0.001)
opt2 = Optimizador(FuncionTrigonometrica(), 0, 10, 0.001)
opt3 = Optimizador(FuncionPolinomial(), 0, 5, 0.001)

x, fx = opt1.busqueda_exhaustiva()
print(f"Cuadrática x* = {x:.4f}   f(x*) = {fx:.4f}")

x, fx = opt2.busqueda_exhaustiva()
print(f"Trigonométrica x* = {x:.4f}   f(x*) = {fx:.4f}")

x, fx = opt3.busqueda_exhaustiva()
print(f"Polinomial x* = {x:.4f}   f(x*) = {fx:.4f}")