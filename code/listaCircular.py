class NoMedicamento:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.proximo = None

class ListaCircularFarmacia:
    def __init__(self):
        self.inicio = None

    def adicionar_medicamento(self, nome, preco, quantidade):
        novo_medicamento = NoMedicamento(nome, preco, quantidade)
        if not self.inicio:
            self.inicio = novo_medicamento
            novo_medicamento.proximo = self.inicio
        else:
            atual = self.inicio
            while atual.proximo != self.inicio:
                atual = atual.proximo
            atual.proximo = novo_medicamento
            novo_medicamento.proximo = self.inicio

    def exibir_medicamentos(self):
        if not self.inicio:
            print("A lista está vazia.")
            return

        atual = self.inicio
        while True:
            print(f"Nome: {atual.nome}, Preço: {atual.preco}, Quantidade: {atual.quantidade}")
            atual = atual.proximo
            if atual == self.inicio:
                break
farmacia = ListaCircularFarmacia()

farmacia.adicionar_medicamento("Paracetamol", 5.0, 50)
farmacia.adicionar_medicamento("Ibuprofeno", 8.0, 30)
farmacia.adicionar_medicamento("Aspirina", 3.5, 40)

farmacia.exibir_medicamentos()