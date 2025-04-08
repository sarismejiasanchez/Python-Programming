import big_o

def constant_time_example(n):
    return n * 2  # O(1)

# Crear generador de datos de prueba
data_generator = big_o.datagen.integers  # Generador de listas de enteros

# Medir la complejidad
best, _ = big_o.big_o(constant_time_example, data_generator)

print(f"Complejidad estimada: {best}")
