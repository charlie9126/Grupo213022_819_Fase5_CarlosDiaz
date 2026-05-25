# definir la matriz de clientes con su ID, 
# duración en segundos y número de clics
data = [
    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 150, 8],
    ["C004", 300, 15],
    ["C005", 80, 3]
]
# definir función para clasificar clientes según duración y clics
def clasifica(duracion, clics):
    # Uso del operador lógico AND para determinar la categoría del cliente
    if duracion > 180 and clics > 8:
        return "Alto"
    # Uso del operador lógico OR para determinar la categoría del cliente
    elif duracion < 60 or clics < 3:
        return "Bajo"
    # Si no cumple ninguna de las condiciones anteriores, 
    # se clasifica como "Medio"
    else:
        return "Medio"
# procesar cada cliente y mostrar su categoría   
for cliente in data:
    id, duracion, clics = cliente
    categoria = clasifica(duracion, clics)
    print(f"Cliente {id}: Duración={duracion} segundos, Clics={clics}, Categoría={categoria}")