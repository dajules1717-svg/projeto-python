with open("frases.txt", "r") as arquivo:
    texto = arquivo.read()

palavras = texto.split()

lista_sem_repeticao = []

for palavra in palavras:
    if palavra not in lista_sem_repeticao:
        lista_sem_repeticao.append(palavra)

print(lista_sem_repeticao)