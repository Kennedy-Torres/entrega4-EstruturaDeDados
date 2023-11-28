class NoMedicamento:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None

class ListaEncadeadaFarmacia:
    def __init__(self):
        self.inicio = None
    def adicionar_medicamento(self, nome, preco, quantidade):
        novo_medicamento = NoMedicamento(nome, preco, quantidade)
        novo_medicamento.proximo = self.inicio
        self.inicio = novo_medicamento

    def exibir_medicamentos(self):
        atual = self.inicio

        while atual:
            print(f"Nome: {atual.nome}, Preço: {atual.preco}, Quantidade: {atual.quantidade}")
            atual = atual.proximo

farmacia = ListaEncadeadaFarmacia()

farmacia.adicionar_medicamento("Paracetamol", 5.0, 50)
farmacia.adicionar_medicamento("Ibuprofeno", 8.0, 30)
farmacia.adicionar_medicamento("Aspirina", 3.5, 40)
farmacia.exibir_medicamentos()