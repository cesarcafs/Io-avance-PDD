from sympy.utilities.iterables import multiset_partitions

# Definir los datos del problema
P = [1,20,3,9,2,11,4]
objetivo = sum(P) // 2

# Encontrar todas las particiones de los datos
partitions = multiset_partitions(P)

# Buscar la partición con la suma de elementos igual a la mitad de la suma total
for partition in partitions:
    if sum(partition[0]) == objetivo:
        p1 = list(partition[0])
        p2 = list(partition[1])
        break

# Imprimir la solución
if sum(p1) == sum(p2):
    print("P1:", p1)
    print("P2:", p2)
else:
    print("No se encontró solución.")
