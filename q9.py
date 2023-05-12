def verificar_prescricao(prescricao, estoque):
    estoque_dict = {}

    # Criar um dicionário para contar a frequência de cada medicamento no estoque
    for medicamento in estoque:
        estoque_dict[medicamento] = estoque_dict.get(medicamento, 0) + 1

    # Verificar se cada medicamento na prescrição está disponível no estoque
    for medicamento in prescricao:
        if medicamento not in estoque_dict or estoque_dict[medicamento] == 0:
            return False
        else:
            estoque_dict[medicamento] -= 1
    return True


# Exemplos de testes
print(verificar_prescricao("a", "bb"))  # Saída: False
print(verificar_prescricao("aa", "b"))  # Saída: False
print(verificar_prescricao("aa", "aab"))  # Saída: True
print(verificar_prescricao("aba", "cbaa"))  # Saída: True

