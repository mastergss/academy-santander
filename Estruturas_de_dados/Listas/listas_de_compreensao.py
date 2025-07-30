# nova_lista = [expressão for elemento in iterável if condição]
# Exemplo de lista de compreensão
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")
quadrados = [n**2 for n in numeros]  # Cria uma nova lista com os quadrados dos números
print(f"lista números ao quadrado: {quadrados}")  # Imprime a lista de quadrados

quadrados_pares = [n**2 for n in numeros if n % 2 == 0]  # Cria uma lista com quadrados de números pares
print(quadrados_pares)  # Imprime a lista de quadrados de números pares

quadrados_impares = [n**2 for n in numeros if n % 2 != 0]  # Cria uma lista com quadrados de números ímpares
print(quadrados_impares)  # Imprime a lista de quadrados de números ímpares