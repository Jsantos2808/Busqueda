import random
import string
import time

# Clase para representar un usuario
class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User (ID: {self.user_id}, Name: {self.name}, Age: {self.age})"

# Generar 100,000 usuarios con datos aleatorios
def generate_users(num_users):
    users = []
    for i in range(num_users):
        user_id = i + 1  # ID único
        name = ''.join(random.choices(string.ascii_letters, k=5))  # Nombre aleatorio de 5 letras
        age = random.randint(18, 99)  # Edad aleatoria entre 18 y 99
        users.append(User(user_id, name, age))
    return users

# Búsqueda lineal
def linear_search(users, user_id):
    for user in users:
        if user.user_id == user_id:
            return user
    return None

# Búsqueda binaria
def binary_search(users, user_id):
    left, right = 0, len(users) - 1
    while left <= right:
        mid = (left + right) // 2
        if users[mid].user_id == user_id:
            return users[mid]
        elif users[mid].user_id < user_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Función para medir tiempo de ejecución de una función y mostrar resultados
def measure_search_time(search_fn, users, user_id, method_name):
    start_time = time.perf_counter()
    user_found = search_fn(users, user_id)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"{method_name} - Usuario encontrado: {user_found}")
    print(f"{method_name} - Tiempo de ejecución: {elapsed:.8f} segundos\n")


if __name__ == "__main__":
    num_users = 100000
    users = generate_users(num_users)

    # Ordenar usuarios por ID para búsqueda binaria
    users.sort(key=lambda x: x.user_id)

    user_id_to_search = random.randint(1, num_users)
    print(f"Buscando usuario con ID = {user_id_to_search}\n")

    # Medir y mostrar tiempos de búsqueda
    measure_search_time(linear_search, users, user_id_to_search, "Búsqueda Lineal")
    measure_search_time(binary_search, users, user_id_to_search, "Búsqueda Binaria")
