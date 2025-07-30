pontos = (10, 20, 30, 40, 50)
print(f"Elementos da Tupla: {pontos}")  # Exibindo todos os elementos da tupla
# Método count
pontos.count(20)  # Contando quantas vezes o número 20 aparece na tupla
print(pontos.count(20))  # Exibindo o resultado da contagem
print(f"Quantidade de vezes que 20 aparece: {pontos.count(20)}") # Exibindo a quantidade de vezes que 20 aparece na tupla

# Método index
pontos.index(30)  # Encontrando o índice do número 30 na tupla
print(pontos.index(30))  # Exibindo o índice do número 30
print(f"Índice do número 30: {pontos.index(30)}") # Exibindo o índice do número 30 na tupla
# Método index com início e fim da busca
repetidos = (1, 2, 3, 1, 2, 3, 1)
print(f"Tupla com elementos repetidos: {repetidos}")  # Exibindo a tupla com elementos repetidos
print(repetidos.index(2, 2))  # Encontrando o índice do número 2 a partir do índice 2
print(f"Índice do número 2 a partir do índice 2: {repetidos.index(2, 2)}")  # Exibindo o índice do número 2 a partir do índice 2

# Método len
print(f"Comprimento da tupla 'pontos': {len(pontos)}")  # Exibindo o tamanho da tupla 'pontos'
print(f"Comprimento da tupla 'repetidos': {len(repetidos)}")  # Exibindo o tamanho da tupla 'repetidos'