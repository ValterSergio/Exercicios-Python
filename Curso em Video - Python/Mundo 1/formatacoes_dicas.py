# Exemplo de diferentes formas de formatação de strings

nome = "Mitsurugi"

# Formata o nome para ocupar 20 espaços, alinhado à esquerda
print(f"Prazer em te conhecer, {nome:20}!")  # Alinha à esquerda com 20 caracteres no total

# Formata o nome para ocupar 20 espaços, alinhado à direita
print(f"Prazer em te conhecer, {nome:>20}!")  # Alinha à direita com 20 caracteres no total

# Formata o nome para ocupar 20 espaços, alinhado à esquerda
print(f"Prazer em te conhecer, {nome:<20}!")  # Alinha à esquerda com 20 caracteres no total

# Formata o nome para ocupar 20 espaços, centralizado
print(f"Prazer em te conhecer, {nome:^20}!")  # Centraliza com 20 caracteres no total

# Formata o nome para ocupar 20 espaços, com preenchimento por '=' (simbolizando uma borda)
print(f"Prazer em te conhecer, {nome:=^20}!")  # Centraliza e preenche com '='

# Leitura de dois valores inteiros do usuário
n1 = int(input("Um valor: \n"))
n2 = int(input("Outro valor: \n"))

# Realiza as operações com os dois números
s = n1 + n2      # Soma
m = n1 * n2      # Multiplicação
d = n1 / n2      # Divisão (com resultado float)
di = n1 // n2    # Divisão inteira
e = n1**n2       # Potência

# Exibe os resultados das operações
# Formatação das saídas: soma, produto e divisão com 3 casas decimais
print(f"A soma é {s}, \no produto é {m} \ne a divisão é {d:.3f}", end=" ")

# Exibe os resultados das operações restantes (divisão inteira e potência)
print(f"\nDivisão inteira: {di} \ne potência: {e}.")
