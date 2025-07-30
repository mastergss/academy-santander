frutas = ["maçã", "banana", "laranja", "uva"]

frutas.append("kiwi")  # Adiciona "kiwi" ao final da lista
print(frutas)  # Imprime a lista atualizada

frutas.insert(2, "abacaxi")  # Insere "abacaxi" na posição 2
print(frutas)  # Imprime a lista atualizada

frutas.remove("banana")  # Remove "banana" da lista
print(frutas)  # Imprime a lista atualizada

fruta_removida = frutas.pop(2)  # Remove e retorna o elemento na posição 2
print(frutas)  # Imprime a lista atualizada
print(f"Fruta removida: {fruta_removida}")  # Imprime

frutas.sort()  # Ordena a lista em ordem alfabética
print(frutas)  # Imprime a lista ordenada

frutas.reverse()  # Inverte a ordem da lista
print(frutas)  # Imprime a lista invertida