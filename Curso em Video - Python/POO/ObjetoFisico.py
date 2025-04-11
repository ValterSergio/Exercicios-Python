"""
Exercicio de POO - aula 2
Indentifique dois objetos fisicos do seu ambiente e classifique-os.

link: https://youtu.be/aR7CKNFECx0?si=ENI6ZhtaQNUjL6uZ
"""


# estou com um caderno em mão
class Caderno():
    
    def __init__(self):
        # O que eu tenho ?

        # ele tem tamanho
        self.largura = 20
        self.altura = 27.5 
        
        # ele tem capa
        self.capa = 2 

        # ele tem folhas
        self.folhas = 350

        # tem 20 folhas pautadas - para cada materia
        self.folhas_pautadas = 20

        # ele tem marca
        self.marca = "tilibra"

        # ele tem cor
        self.cor = "preto" 

        # ele tem desenho alguns pode ser de cor unica
        self.desenho = True  

        # ele tem um espiral, tem alguns que não
        self.espiral = True

        # eu posso estar aberto ou fechado
        self.aberto = False

        # eu posso anotar informações
        self.anotar = []

    # O que eu Faço ? 
    
    # eu abro
    def abrir_caderno(self):
        if not self.aberto:
            self.aberto = True
    
    # Eu fecho o caderno
    def fechar_caderno(self):
        if self.aberto:
            self.aberto = False
    
    # Eu posso guardar informações
    def escrever_anotacao(self):
        if self.aberto:
            anotar = input("Anotar informações para guardar: ")
            self.anotar.append(anotar)
        else:
            print("Caderno Fechado")
    
    # Eu posso ter uma folha removida
    def remover_folha(self):
        self.folhas -= 1

    # eu posso ter uma folha totalmente preenchida
    def folha_preenchida(self):
        # vamos supor que cada folha tenho 30 linhas
        # e que cada linha caiba 10 palavras - media com base no meu caderno e letra
        
        # armazenar total de palavras
        palavras = 10

        # total de linhas
        linhas = 30
        for anotacao in self.anotar:
            palavras -= 1
            if not palavras:
                linhas -= 1
                palavras = 10

            if not linhas:
                self.folhas -= 1
                linhas = 30
        

c1 = Caderno()
c1.abrir_caderno()
c1.escrever_anotacao()
