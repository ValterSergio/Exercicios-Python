# Faça um programa que leia uma frase qualquer e mostre:
# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input("Digite qualquer frase: ").lower()

# print(len([letra for letra in frase if letra == 'a']))

# opção 1 - manualmente
primeira_vez = 0
ultima_vez = 0
contador = 0 # marcar posição
contar_letra_a = 0

for letra in frase:    
    contador += 1
    if letra == 'a':
        if not primeira_vez:
            primeira_vez = contador - 1 # -1 é para marcar posição na lista
        contar_letra_a += 1
        ultima_vez = contador - 1

print(f"\nA primeira letra A esta na posição: {primeira_vez}")
print(f"A ultima letra A esta na posição: {ultima_vez}")
print(f"Foram encontradas {contar_letra_a} letras 'a'.\n")

# ou

# opção 2 - modo python
print(f"A primeira letra A esta na posição: {frase.find("a")}")
print(f"A ultima letra A esta na posição: {frase.rfind("a")}")
print(f"Foram encontradas {frase.count("a")} letras 'a'.\n")