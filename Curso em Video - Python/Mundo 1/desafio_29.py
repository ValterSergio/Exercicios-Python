"""
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = int(input("Velocidade do carro: \n"))
if velocidade > 80:
    print(f"Você está acima do limite permitido! \nVelocidade de {velocidade}km/h!")
    multa = 7 * (velocidade - 80)
    print(f"Sua multa é de R${multa:.2f}.")
else:
    print("Velocidade dentro do limite. Boa viagem.")
