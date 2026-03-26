with open("dna.txt", "r") as arquivo:
    dna = arquivo.read().strip()

dna_invertido = dna[ ::-1]

print("Entrada:", dna)
print("Saída:", dna_invertido)