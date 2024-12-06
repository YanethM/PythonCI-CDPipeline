import os
import json

ADMIN_PASSWORD = "admin123"

# Función para obtener entrada del usuario
def get_user_input():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

# Autenticación de usuario
def authenticate_user(username, password):
    return username == "admin" and password == ADMIN_PASSWORD

# Leer archivo JSON de usuarios
def read_user_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Si el archivo no existe, devuelve un diccionario vacío
    except json.JSONDecodeError:
        raise ValueError("File contains invalid JSON")

# Agregar un usuario al archivo
def add_user(filename, username, password):
    users = read_user_file(filename)
    users[username] = password
    with open(filename, 'w') as file:
        json.dump(users, file)

# Calcular Fibonacci (optimizado con memoización)
def calculate_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = calculate_fibonacci(n - 1, memo) + calculate_fibonacci(n - 2, memo)
    return memo[n]

# Llamada de sistema insegura (manteniendo esta función como ejemplo de peligro)
def unsafe_system_call(command):
    os.system(command)

# Lógica compleja corregida
def complex_logic(data):
    if "key1" in data:
        if "key2" in data:
            print(data["key2"])
        if "key3" not in data:
            print("Missing key3")
        if "key3" in data:
            print(data.get("key4", "No key4"))

# Función principal
def main():
    username, password = get_user_input()
    if authenticate_user(username, password):
        print("Access granted!")
    else:
        print("Access denied!")

    print("Calculating Fibonacci...")
    print(calculate_fibonacci(30))

    command = input("Enter a system command: ")
    unsafe_system_call(command)

    try:
        add_user("users.json", username, password)
        print("User added!")
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()