'''O Selection Sort é um algoritmo de ordenação simples, mas não muito eficiente para conjuntos de dados grandes. Ele funciona 
selecionando repetidamente o menor (ou maior, dependendo da ordem desejada) elemento da lista e trocando-o com o primeiro elemento 
não ordenado.'''

#Exemplo, contexto farmácia:

class Medicamento: #A classe Medicamento é definida com dois atributos, nome e preco, representando o nome e o preço do medicamento, respectivamente.
    def __init__(self, nome, preco): #é um método construtor, chamado automaticamente quando um novo objeto da classe é criado. 
        self.nome = nome #Dentro do método __init__, essa linha atribue o valore do parâmetro nome aos atributos da classe Medicamento. 
        self.preco = preco #Dentro do método __init__, essa linha atribue o valore do parâmetro preco aos atributos da classe Medicamento. 

def selection_sort(medicamentos): #A função selection_sort implementa o algoritmo de Selection Sort para ordenar a lista de medicamentos com base no preço.
    n = len(medicamentos) #Determina o comprimento da lista de medicamentos, ou seja, o número de elementos na lista. Isso será usado para controlar os loops de iteração.

    for i in range(n - 1): #Este é o loop externo, que percorre a lista de medicamentos até o penúltimo elemento. 
        indice_menor = i #Inicializa a variável indice_menor com o valor do índice atual do loop externo.

        for j in range(i + 1, n): # Este é o loop interno que começa do próximo elemento após o elemento atual do loop externo até o final da lista.
            if medicamentos[j].preco < medicamentos[indice_menor].preco: #Compara os preços dos medicamentos nos índices j e indice_menor. Se o preço do medicamento no índice j for menor, atualiza indice_menor para j.
                indice_menor = j 

        medicamentos[i], medicamentos[indice_menor] = medicamentos[indice_menor], medicamentos[i] # Após encontrar o índice do menor preço no loop interno, realiza a troca dos medicamentos nos índices i e indice_menor.

def exibir_medicamentos(medicamentos): #A função exibir_medicamentos é responsável por imprimir na tela os medicamentos, mostrando o nome e o preço formatado.
    for medicamento in medicamentos: # Este é um loop que percorre cada objeto da lista medicamentos e associa cada objeto à variável medicamento durante cada iteração.
        print(f"{medicamento.nome}: R${medicamento.preco:.2f}")
#Cadastro e passagem de parâmetros dos produtos
medicamento1 = Medicamento("Paracetamol", 15.50)
medicamento2 = Medicamento("Aspirina", 10.20)
medicamento3 = Medicamento("Amoxicilina", 25.00)
medicamento4 = Medicamento("Ibuprofeno", 12.75)

lista_medicamentos = [medicamento1, medicamento2, medicamento3, medicamento4] #cria-se uma lista com os produtos cadastrados

selection_sort(lista_medicamentos) #A função selection_sort é chamada para ordenar a lista de medicamentos com base nos preços.

print("+=====================================+")
print("|            Selection Sort           |")
print("+=====================================+")
print("\nLista de medicamentos ordenada por preços:") 
exibir_medicamentos(lista_medicamentos) #A função exibir_medicamentos é chamada para mostrar a lista de medicamentos ordenada na tela.