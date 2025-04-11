# a classe é um molde para criar objetos do mundo real
class Pessoa:

    # metodo contrututor python
    def __init__(self, nome, idade):

        # definimos as caracteristicas do objeto
        self.nome = nome
        self.idade = idade
    
    # metodo do objeto, toda pessoa precisa se apresentar
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, e estou aprendendo a programar.")


if __name__ == "__main__":

    # criamos o objeto
    objeto1 = Pessoa("Valter", 30)

    # Realizamos a ação do objeto
    objeto1.apresentar()

    # podemos alterar as caracteristicas desse objeto
    objeto1.nome = "Wagner"
    objeto1.idade = 33

    objeto1.apresentar()

    # Podemos criar outro objeto usando a mesma classe
    objeto2 = Pessoa("Wanderley", 28)
    objeto2.apresentar()