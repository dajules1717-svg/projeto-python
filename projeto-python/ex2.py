with open("texto.txt", "r") as arquivo:
    texto = arquivo.read()

palavras = texto.split()
quantidade = len(palavras)

print("Quantidade de palavras:", quantidade)