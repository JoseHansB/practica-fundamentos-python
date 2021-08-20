import random

#para instalar esto 
# python -m pip install -U pip
# python -m pip install -U matplotlib
import matplotlib.pyplot as plt
print(random.randint(0,20))
print(random.randrange(10, 100, 2))

#reacomodar una lista al asar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("lista original", lista)
random.shuffle(lista)
print("lista mixeada", lista)

#grafica de GAUSS
campana = [random.gauss(0,1.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()