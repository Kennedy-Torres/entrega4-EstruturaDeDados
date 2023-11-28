class Medicamento:
  def __init__(self, nome, preco):
      self.nome = nome
      self.preco = preco
  def __repr__(self):
      return "< Nome: " + self.nome + ", Preco: R$ " + str(self.preco) + " >"

class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    # inserir na fila
    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1

    # remover da fila
    def pop(self):
        if self._size > 0: 
            #Não queremos fazer essa operação quando não há nós
            elem = self.first.data
            self.first = self.first.next #tanto next como first recebem posições, endereços de memória

            if self.first is None:
            #Se chegarmos ao final, portanto tirando todos os elementos,
            #o último deve ser none também
                self.last = None

            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")

    # observar o primeiro da fila
    def peek(self):
        """Retorna o topo sem remover"""
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()
    
fila_medicamentos = Queue()

while True:
  print("\n----------------------")
  print("\nEscolha uma opção:")
  print("1. Mostra o primeiro da fila")
  print("2. Adicionar medicamento ao fim da fila")
  print("3. Remover o primeiro da fila")
  print("4. Exibir produtos da fila")
  print("5. Sair")

  opcao = input("Digite o número da opção desejada: ")

  if opcao == '1':
    print(fila_medicamentos.peek())


  elif opcao == '2':

    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))

    novo_medicamento = Medicamento(nome, preco)
    fila_medicamentos.push(novo_medicamento)

  elif opcao == '3':
    print(fila_medicamentos.pop())

  elif opcao == '4':
    print(fila_medicamentos.__str__())

  elif opcao == '5':
    print("Programa encerrado.")
    break

  else:
    print("Opção inválida. Tente novamente.")