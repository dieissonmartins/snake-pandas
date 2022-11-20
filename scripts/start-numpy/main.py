import numpy as np

# declara e imprime array com numpy
arr_1 = np.array([0, 1, 2, 3, 4, 5])

# imprime valores do array
print(arr_1)

# imprime tipo do array
print(arr_1.dtype)

# imprime quantidade de elementos
print(arr_1.size)

# imprime tamanho de X bytes
print(arr_1.itemsize * arr_1.size)

# imprime item acima
print(arr_1.nbytes)

# imprime numero de dimensoes
print(arr_1.ndim)