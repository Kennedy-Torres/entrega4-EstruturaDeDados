'''Modulo para exemplificar uma Busca Binaria'''
from os import system


class BuscaBinaria:
    """Modulo para exemplificar uma Busca Binaria

    Returns:
        _type_: _description_
    """

    @staticmethod
    def leitura_lista_medicamentos(path_file_txt: str = './data/lista_medicamentos.txt') -> list:
        """_summary_

        Args:
            path_file_txt (str, optional): _description_. Defaults to './data/lista_medicamentos.txt'.

        Returns:
            list: _description_
        """
        with open(path_file_txt, encoding='utf-8') as file:
            lista_medicamentos = file.read()
            lista_medicamentos = lista_medicamentos.split('\n')
        return lista_medicamentos


    @staticmethod
    def busca(palavra: str, medicamentos: list) -> None:
        """_summary_

        Args:
            palavra (str): _description_
            medicamentos (list, optional): _description_. Defaults to medicamentos.

        Returns:
            str: _description_
        """
        medicamentos_temp = medicamentos
        while True:
            if len(medicamentos_temp) == 0:
                print('\nPalavra não encontrada :(\n')
                print({"Palavra procurada": palavra, "Indica na lista de medicamentos": None})
                break
            i = len(medicamentos_temp) // 2 # Pega o idice da metada da lista
            palavra_meio_da_lista = medicamentos_temp[i] # Qual e a palavra que esta no meio da lista
            if palavra_meio_da_lista == palavra:
                print('\nPalavra encontrada !\n')
                print({"Palavra procurada": palavra, "Indica na lista de medicamentos": medicamentos.index(palavra)})
                break
            # Em qual lado esta a palavra buscada (Esquerda ou Direita)
            if palavra > palavra_meio_da_lista:
                medicamentos_temp = medicamentos_temp[i+1:]
            else:
                medicamentos_temp = medicamentos_temp[:i]


if __name__ == "__main__":
    system('cls')
    BUSCA = BuscaBinaria
    p = input('Digite o nome do medicamento: ').upper()
    lista_medicamentos_ = BUSCA.leitura_lista_medicamentos()
    BUSCA.busca(medicamentos=lista_medicamentos_, palavra=p)
