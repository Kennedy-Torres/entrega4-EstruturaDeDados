class Medicamento:
    def __init__(self, nome=None, preco=None, codigo_barras=None):
        self.nome = nome
        self.preco = preco
        self.codigo_barras = codigo_barras

class NodoArvore:
    def __init__(self, medicamento=None, esquerda=None, direita=None):
        self.medicamento = medicamento
        self.esquerda = esquerda
        self.direita = direita
        
    

def insere(raiz, nodo):
    if raiz is None:
        raiz = nodo
    elif raiz.medicamento.codigo_barras < nodo.medicamento.codigo_barras:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def em_ordem(raiz):
    if not raiz:
        return

    em_ordem(raiz.esquerda)
    print(f"Nome: {raiz.medicamento.nome}, Preço: {raiz.medicamento.preco}, Código de Barras: {raiz.medicamento.codigo_barras}")
    em_ordem(raiz.direita)

def buscar_medicamento(raiz, codigo_barras):
    if raiz is None or raiz.medicamento.codigo_barras == codigo_barras:
        return raiz
    if raiz.medicamento.codigo_barras < codigo_barras:
        return buscar_medicamento(raiz.direita, codigo_barras)
    return buscar_medicamento(raiz.esquerda, codigo_barras)

# Exemplo de uso
raiz = None

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar medicamento")
    print("2. Exibir produtos da árvore")
    print("3. Procurar medicamento por código de barras")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do medicamento: ")
        preco = float(input("Digite o preço do medicamento: "))
        codigo_barras = input("Digite o código de barras do medicamento: ")

        novo_medicamento = Medicamento(nome, preco, codigo_barras)
        nodo = NodoArvore(novo_medicamento)

        if raiz is None:
            raiz = nodo
        else:
            insere(raiz, nodo)
        print("Medicamento adicionado com sucesso!")

    elif opcao == '2':
        print("\nEstrutura da Árvore:")
        em_ordem(raiz)

    elif opcao == '3':
        codigo_barras = input("Digite o código de barras do medicamento a ser procurado: ")
        encontrado = buscar_medicamento(raiz, codigo_barras)

        if encontrado:
            print(f"Medicamento encontrado - Nome: {encontrado.medicamento.nome}, Preço: {encontrado.medicamento.preco}")
        else:
            print("Medicamento não encontrado.")

    elif opcao == '4':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
