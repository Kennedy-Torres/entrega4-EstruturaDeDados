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

  def __repr__(self):
      return "< Nome: " + self.nome + ", Preco: R$ " + str(self.preco) + " >"
#IMPLEMENTAÇÕES
# 1. inserir na pilha
# 2. remover da pilha
# 3. observar o topo da pilha
class Stack:

  def __init__(self):
    self.top = None
    self._size = 0

  def __len__(self):
    """Retorna o tamanho da lista"""
    return self._size

  def push(self, elem):
    #insere um elemento na pilha
    node = Node(elem)
    node.next = self.top #self.top estaria valendo 1, por exemplo
    self.top = node 
    self._size = self._size + 1

  def pop(self):
    # remove o elemento do topo da pilha
    if self._size > 0:
        node = self.top
        self.top = self.top.next 
        self._size = self._size - 1
        return node.data
    raise IndexError("The stack is empty")

  def peek(self):
    # retorna o topo sem remover
    if self._size > 0:
        return self.top.data
    raise IndexError("The stack is empty")  

  def __repr__(self):
    r = "\n"
    pointer = self.top
    while(pointer):
        r = r + str(pointer.data) + "\n"
        pointer = pointer.next
    return r

  def __str__(self):
    return self.__repr__()   

#criando um objeto da classe pilha
pilha_medicamentos = Stack()

while True:
  print("\n----------------------")
  print("\nEscolha uma opção:")
  print("1. Mostrar o topo da pilha")
  print("2. Adicionar medicamento ao topo da pilha")
  print("3. Remover o topo da pilha")
  print("4. Exibir produtos da pilha")
  print("5. Sair")

  opcao = input("Digite o número da opção desejada: ")

  if opcao == '1':
    print(pilha_medicamentos.peek())


  elif opcao == '2':

    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))

    novo_medicamento = Medicamento(nome, preco)
    pilha_medicamentos.push(novo_medicamento)

  elif opcao == '3':
    print(pilha_medicamentos.pop())

  elif opcao == '4':
    print(pilha_medicamentos.__str__())

  elif opcao == '5':
    print("Programa encerrado.")
    break

  else:
    print("Opção inválida. Tente novamente.")
