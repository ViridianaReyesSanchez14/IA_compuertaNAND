import random


class Perceptron:

    def __init__(self):
        self.w1 = random.uniform(-1,1)
        self.w2 = random.uniform(-1,1)
        self.bias = random.uniform(-1,1)

    def prediccion(self,x1,x2):
        result = self.w1 * x1 + self.w2 * x2 + self.bias 

        if result >= 0:
            return 1
        else:
            return 0
        
def train(perceptron,tablaNand,rango_de_aprendizaje = 0.1,generaciones = 30):
    

    for generacion in range(generaciones):
        for  x1,x2,y_real in tablaNand:
            y_prediccion = perceptron.prediccion(x1,x2)
            error = y_real - y_prediccion 

            perceptron.w1 += rango_de_aprendizaje * error * x1
            perceptron.w2 += rango_de_aprendizaje * error * x2
            perceptron.bias += rango_de_aprendizaje * error

def prueba(perceptron,tablaNand):
    print("Compuerta lógica NAND")

    for x1,x2, _ in tablaNand:
        resultado = perceptron.prediccion(x1,x2)
        print(f"{x1} {x2}  {resultado}")

def main ():
    tablaNand = [
        (0,0,1),
        (0,1,1),
        (1,0,1),
        (1,1,0)
    ]

    perceptron = Perceptron()

    train( perceptron, tablaNand, rango_de_aprendizaje=0.1,generaciones=10)

    prueba( perceptron,tablaNand)

if __name__ == "__main__": 
    main()
