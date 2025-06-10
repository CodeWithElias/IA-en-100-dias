import numpy as np

X = np.array([-1.2, -0.7, -3.0])

pesos = np.array([0.5, -1.2, 0.8])

sesgo = 0.1

z =np.dot(X, pesos) + sesgo
print (z)


def relu(x):
    return max(0,x)

salida = relu(z)

print(f"Salida de la neurona: {salida}")