"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
Além disso, indique qual tipo de triângulo será formado, se possível:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo.")
    if a == b == c:
        print("Tipo: Triângulo Equilátero (todos os lados iguais).")
    elif a == b or a == c or b == c:
        print("Tipo: Triângulo Isósceles (dois lados iguais).")
    else:
        print("Tipo: Triângulo Escaleno (todos os lados diferentes).")
else:
    print("As retas não podem formar um triângulo.")
