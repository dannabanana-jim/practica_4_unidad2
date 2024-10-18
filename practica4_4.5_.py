print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#2- Hacer un diccionario de traducción español-inglés, se van a introducir las palabras en español e inglés separadas por dos puntos,
#y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
#Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.
# Crear el diccionario de traducción
input_data = input("Introduce las traducciones (palabra:traducción), separadas por comas: ")
traducciones = {}

# Procesar las traducciones
for par in input_data.split(","):
    espanol, ingles = par.split(":")
    traducciones[espanol.strip()] = ingles.strip()

# Pedir una frase en español para traducir
frase = input("Introduce una frase en español para traducir: ")
palabras = frase.split()

# Traducir la frase
traduccion = []
for palabra in palabras:
    traduccion.append(traducciones.get(palabra, palabra))  # Si no está, deja la palabra sin traducir

# Mostrar la traducción
print("Traducción:", " ".join(traduccion))
