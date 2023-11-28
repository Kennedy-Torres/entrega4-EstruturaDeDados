def busca_sequencial(lista_medicamentos, medicamento_procurado):
    """
    Realiza uma busca sequencial em uma lista de medicamentos.
    
    Parameters:
        lista_medicamentos (list): Lista de medicamentos disponíveis na farmácia.
        medicamento_procurado (str): Nome do medicamento que está sendo procurado.
    
    Returns:
        int or None: Retorna o índice do medicamento se encontrado, ou None se não encontrado.
    """
    for i, medicamento in enumerate(lista_medicamentos):
        if medicamento.strip() == medicamento_procurado:
            return i  # Medicamento encontrado, retorna o índice
    return None  # Medicamento não encontrado

# Carregar a lista de medicamentos a partir de um arquivo
def carregar_lista_medicamentos(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]

# Caminho do arquivo contendo a lista de medicamentos
caminho_arquivo_medicamentos = './data/lista_medicamentos.txt'

# Carregar a lista de medicamentos do arquivo
lista_medicamentos = carregar_lista_medicamentos(caminho_arquivo_medicamentos)

# Exemplo de uso
medicamento_procurado = input("Digite o nome do medicamento que deseja buscar: ")

resultado = busca_sequencial(lista_medicamentos, medicamento_procurado)

if resultado is not None:
    print(f"O medicamento {medicamento_procurado} foi encontrado no índice {resultado}.")
else:
    print(f"O medicamento {medicamento_procurado} não foi encontrado.")
