class Animal:
    def __init__(self, tipo, nome):
        self.nome = nome
        self.tipo = tipo
    
    def identificar_animal(self):
        print(f"Eu sou um {self.tipo}, me chamo {self.nome}")

if __name__ == "__main__":
    gato = Animal("Gato", "Pretinho")
    gato.identificar_animal()

    cachorro = Animal("Cachorro", "Bob")
    cachorro.identificar_animal()