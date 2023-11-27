class Medicamento: 
    def __init__(self, nome, preco): 
        self.nome = nome 
        self.preco = preco 

def insertion_sort_farmacia(medicamentos): 
    for i in range(1, len(medicamentos)): 
        chave = medicamentos[i]  
        j = i - 1 

        while j >= 0 and chave.preco < medicamentos[j].preco: 
            medicamentos[j + 1] = medicamentos[j] 
            j -= 1 

        medicamentos[j + 1] = chave  
medicamento1 = Medicamento("Paracetamol", 15.50) 
medicamento2 = Medicamento("Aspirina", 10.20)
medicamento3 = Medicamento("Amoxicilina", 25.00)
medicamento4 = Medicamento("Ibuprofeno", 12.75)

lista_medicamentos = [medicamento1, medicamento2, medicamento3, medicamento4] 

insertion_sort_farmacia(lista_medicamentos) 

print("+=====================================+")
print("|            Insertion Sort           |")
print("+=====================================+")
print("\nLista de medicamentos ordenada por preço:\n")
for medicamento in lista_medicamentos:
    print(f"{medicamento.nome}: R${medicamento.preco:.2f}") 
