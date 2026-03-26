with open("texto.txt", "r") as arquivo:
    texto = arquivo.read()

novo_texto = texto.replace(" ", "_")

print(novo_texto)