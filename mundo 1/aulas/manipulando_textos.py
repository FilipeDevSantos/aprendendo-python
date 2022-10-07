frase = 'Curso em Vídeo Python'
print(frase)

# Fatiamento
print("\nFatiamento\n")
print(frase[2:3])
print(frase[0:20:2])
print(frase[::2])

# Ánalise
print("\nÁnalise\n")
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 19))
print(frase.find('Py'))
print(frase.find('Julia'))
print('Curso' in frase)

# Transformação
print("\nTransformação\n")
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print("      Aprenda Python    ".strip())

# Divisão
print("\nDivisão\n")
print(frase.split())
print("-".join(frase))

# Frases de multiplas linhas
print("""
    Estou adorando esse curso de Python.
    Sério, estou muito feliz com o aprendizado!
""")