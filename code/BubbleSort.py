def ordena_medicamentos_usando_BubbleSort():
    
    def bubble_sort(arr,chave_ordenacao):
        n = len(arr)
        for i in range(n):
            
            for j in range(n-i-1):
                if arr[j][chave_ordenacao] > arr[j+1][chave_ordenacao]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        return arr

    # lista de dicionários 
    lista_de_medicamentos = [
        {'ID':1,'Nome':'Dipirona','Preco':5.70},
        {'ID':7,'Nome':'Paracetamol','Preco':12.40},
        {'ID':3,'Nome':'Dorflex','Preco':3.20},
        {'ID':5,'Nome':'Rivotril','Preco':33.70},
        {'ID':2,'Nome':'Sonrisal','Preco':2.00},
    ]

    print('''
    +----------------------------------+      
    |      LISTA ORDENADA PELO ID      |
    +----------------------------------+''')
    bubble_sort(lista_de_medicamentos,'ID')
    #Lista ordenada pelo ID
    for dicionario in lista_de_medicamentos:
        print(f"ID: {dicionario['ID']} Nome: {dicionario['Nome']} Preco: {dicionario['Preco']}") 
        

    print('''
    +----------------------------------+      
    |    LISTA ORDENADA PELO Preco     |
    +----------------------------------+         ''')
    bubble_sort(lista_de_medicamentos,'Preco')
    #Lista ordenada pelo preco
    for dicionario in lista_de_medicamentos:
        print(f"ID: {dicionario['ID']} Nome: {dicionario['Nome']} Preco: {dicionario['Preco']}") 
        