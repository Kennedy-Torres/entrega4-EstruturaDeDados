'''O algoritmo de ordenação por inserção (Insertion Sort) é um método eficiente para ordenar pequenos conjuntos de elementos. Ele 
funciona construindo uma sequência ordenada de elementos um de cada vez, pegando um elemento da lista e inserindo-o na posição correta.'''

#Para explicar mais detalhadamente o funcionamento dessa ferramenta irei utilizar de um exemplo e de comentários ao código a seguir:

class Medicamento: #A classe Medicamento é usada para representar os medicamentos com seus atributos nome e preco.
    def __init__(self, nome, preco): #Esta linha define o método __init__ da classe Medicamento. O método __init__ é chamado automaticamente quando um objeto da classe é criado. O parâmetro self é uma referência ao próprio objeto sendo criado, e nome e preco são parâmetros que o usuário passa ao criar um novo objeto da classe.
        self.nome = nome #self.nome é um atributo da instância (objeto) da classe Medicamento, e nome é o parâmetro que o usuário fornece ao criar um novo objeto. Isso significa que, quando você cria uma instância da classe Medicamento e fornece um valor para nome, esse valor é atribuído ao atributo nome do objeto.
        self.preco = preco #self.preco é um atributo da instância da classe Medicamento, e preco é o parâmetro que o usuário fornece ao criar um novo objeto. O valor fornecido para preco é atribuído ao atributo preco do objeto.

def insertion_sort_farmacia(medicamentos): #A função insertion_sort_farmacia recebe uma lista de medicamentos e a ordena com base nos preços.
    for i in range(1, len(medicamentos)): #Este é um loop que itera sobre a lista de medicamentos a partir do segundo elemento 
        chave = medicamentos[i] #chave é uma variável que armazena temporariamente o medicamento atual que estamos considerando para inserção na posição correta.
        j = i - 1 #A variável j é usada para comparar o preço do medicamento atual com os preços dos medicamentos anteriores na lista.

        while j >= 0 and chave.preco < medicamentos[j].preco: #Este é um loop while que continua enquanto j é maior ou igual a zero e o preço do medicamento atual é menor que o preço do medicamento na posição j na lista.
            medicamentos[j + 1] = medicamentos[j] #Se o preço do medicamento atual for menor do que o preço do medicamento na posição j, o medicamento na posição j é deslocado para a direita para abrir espaço para o medicamento atual.
            j -= 1 # O índice j é então decrementado para comparar o medicamento atual com o próximo medicamento anterior na lista.

        medicamentos[j + 1] = chave # Após o término do loop while, o medicamento atual é inserido na posição correta na sequência ordenada, que pode ser a posição original de j ou a posição à direita da última comparação bem-sucedida.
#Cadastro e passagem de parâmetros dos produtos
medicamento1 = Medicamento("Paracetamol", 15.50) 
medicamento2 = Medicamento("Aspirina", 10.20)
medicamento3 = Medicamento("Amoxicilina", 25.00)
medicamento4 = Medicamento("Ibuprofeno", 12.75)

lista_medicamentos = [medicamento1, medicamento2, medicamento3, medicamento4] #cria-se uma lista com os produtos cadastrados

insertion_sort_farmacia(lista_medicamentos) #a função insertion_sort_farmacia é chamada para ordenar a lista por preço. 

print("+=====================================+")
print("|            Insertion Sort           |")
print("+=====================================+")
print("\nLista de medicamentos ordenada por preço:\n")
for medicamento in lista_medicamentos:
    print(f"{medicamento.nome}: R${medicamento.preco:.2f}") #Por fim, a lista ordenada é impressa.

'''Em resumo o algoritmo percorre a lista de medicamentos da esquerda para a direita, considerando cada elemento um por vez. Ele compara o preço 
do medicamento atual com os preços dos medicamentos anteriores na lista, movendo os elementos maiores para a direita até encontrar a 
posição correta para inserir o medicamento atual.'''