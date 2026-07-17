# Solicitar información al usuario
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad de residencia: ")

# Información adicional para la historia
profesion = input("¿Cuál es tu profesión o a qué te dedicas?: ")
hobby = input("¿Cuál es tu pasatiempo favorito?: ")
sueno = input("¿Cuál es tu mayor sueño?: ")

# Crear la historia
print(f"\n=== LA HISTORIA DE {nombre.upper()} ===\n")
print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
print(f"Se dedica a {profesion} y en su tiempo libre disfruta {hobby}.")
print(f"A pesar de su rutina diaria, {nombre} nunca olvida que su mayor sueño es {sueno}.")
print(f"Un día, mientras caminaba por las calles de {ciudad}, {nombre} decidió que era el momento de perseguir ese sueño...")