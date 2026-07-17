# Lista con al menos 5 nombres de personas
nombres = ["Ana", "Carlos", "María", "Pedro", "Laura", "Juan"]

# Diccionario con los nombres como claves y las edades como valores
edades = {
    "Ana": 30,
    "Carlos": 25,
    "María": 28,
    "Pedro": 35,
    "Laura": 22,
    "Juan": 40
}

# Solicitar al usuario que ingrese un nombre
nombre_buscar = input("Ingresa un nombre: ")

# Verificar si el nombre está en el diccionario usando condicional
if nombre_buscar in edades:
    print(f"{nombre_buscar} tiene {edades[nombre_buscar]} años.")
else:
    print(f"La persona '{nombre_buscar}' no fue encontrada.")