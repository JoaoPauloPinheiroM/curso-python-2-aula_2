from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome:str, categoria:str):
        """Construtor da classe restaurante
            espera receber duas strings
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = [] #vai ser uma lista de classe do tipo avaliacao, ou seja, vai ser uma relacao de composicao
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Representa a classe como ela é em string, equivalente ao to string"""
        return f'{self.nome.ljust(15)} | {self.categoria.ljust(15)}'

    @classmethod
    def listar_restaurantes(cls):
        """um metodo da classe, ou seja, somente a classe pode acessar, equivalente a uma static metodo do C#"""
        print(f'{'Nome'.ljust(15)} | {'Categoria'.ljust(15)}| {'Média da nota'.ljust(15)} | {'Status'.ljust(15)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(15)} | {restaurante._categoria.ljust(15)}| {str(restaurante.media_avaliacao).ljust(15)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """um property, é tipo um getter e setter este é um getter"""
        return 'Ativo' if self._ativo else 'Desativado'

    def alterar_estado(self):
        """Metodo de objeto, pode ser acessado pelo objet
            esse altera o estado da classe entre ativo e inativo conforme o valor da var bool        
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente : str, nota : int):
        """Esse metodo cria um objeto de avaliacao e adiciona a lista do objeto sua avaliaçao"""
        if nota > 0 and nota < 5:
            avaliacao = Avaliacao(cliente, nota) # aqui ocorre meio que uma composiçao 
            self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        return round((sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao)),1)#vai retornar a média do restaurante

