def ordena_medicamentos_usando_SelectionSort():
    class Medicamento: 
        def __init__(self, nome, preco): 
            self.nome = nome 
            self.preco = preco 

    def selection_sort(medicamentos): 
        n = len(medicamentos) 

        for i in range(n - 1): 
            indice_menor = i 

            for j in range(i + 1, n): 
                if medicamentos[j].preco < medicamentos[indice_menor].preco: 
                    indice_menor = j 

            medicamentos[i], medicamentos[indice_menor] = medicamentos[indice_menor], medicamentos[i] 

    def exibir_medicamentos(medicamentos): 
        for medicamento in medicamentos: 
            print(f"{medicamento.nome}: R${medicamento.preco:.2f}")
            
    #Cadastro e passagem de parâmetros dos produtos
    medicamento1 = Medicamento("Paracetamol", 15.50)
    medicamento2 = Medicamento("Aspirina", 10.20)
    medicamento3 = Medicamento("Amoxicilina", 25.00)
    medicamento4 = Medicamento("Ibuprofeno", 12.75)

    lista_medicamentos = [medicamento1, medicamento2, medicamento3, medicamento4] # lista com os produtos cadastrados

    selection_sort(lista_medicamentos) # ordenar a lista de medicamentos com base nos preços.

    print("+=====================================+")
    print("|            Selection Sort           |")
    print("+=====================================+")
    print("\nLista de medicamentos ordenada por preços:") 
    exibir_medicamentos(lista_medicamentos) 