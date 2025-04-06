"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

a = int(input("Digite um primeiro número: \n"))
b = int(input("Digite um segundo número: \n"))
c = int(input("Digite um último número: \n"))

# como as aulas são de condicionais

if (a > b) and (a > c): # checa se o A é maior
    print(f"O maior numero é o ", a)
elif (b > a) and (b > c): # checa se o B é maior
    print("O maior numero é o ", b)
else:
    print("O maior numero é o ", c)

if (a < b) and (a < c): # checa se o A é menor
    print(f"O menor numero é o ", a)
elif (b < a) and (b < c): # checa se o B é menor
    print("O menor numero é o ", b)
else:
    print("O menor numero é o ", c)

# ou 

print("\nO maior numero: ", max([a, b, c]))
print("O menor numero: ", min([a, b, c]))