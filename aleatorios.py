import random
import matplotlib.pyplot as plt
import numpy as np

# Lista auxiliar para las funciones random.choice() y random.sample()
numbers_liste_aux = [i for i in range(10000)]

# List comprehensions

random_numbers_f1 = [random.random() for i in range(1000)]
random.seed()
random_numbers_f2 = [random.random() for i in range(1001)]
random_numbers_f3 = [random.uniform(1, 10000) for i in range(1001)]
random_numbers_f4 = [random.randint(1, 10000) for i in range(1001)]
random_numbers_f5 = [random.choice(numbers_liste_aux) for i in range(1001)]
random_numbers_f6 = [random.sample(numbers_liste_aux, k=1) for i in range(1001)]


# Función utilizada para graficar
def grafica(random_numbers):
    x = np.arange(0, len(random_numbers), 1)
    plt.plot(x, random_numbers, "o")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Distribución números aleatorios")
    plt.show()


grafica(random_numbers_f1)
grafica(random_numbers_f2)
grafica(random_numbers_f3)
grafica(random_numbers_f4)
grafica(random_numbers_f5)
grafica(random_numbers_f6)
