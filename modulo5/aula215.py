# Relacionamento entre classes
# Associação
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._tool = None

    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, tool):
        self._tool = tool 


class Tool:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} esta escrevendo'
    

escritor = Escritor('Amanda')
caneta = Tool('Caneta bic')
# esta é a associação - tipo weak pois ainda posso chamar 
# print(caneta.escrever())
escritor.tool = caneta

# print(escritor.tool.escrever())

# Agregação - Associação um pouco melhor
# ambos existem idependentemente, mas algumas tarefas dependem da associação de ambos
# exemplo o carro existe sem roda, e a roda existe sem o carro, mas o carro
# precisa das rodas para andar

class Carrinho:
    def __init__(self):
        self._produtos = []
    
    @property
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def listar(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
    
    def inserir_produtos(self, *produtos):
        # for produto in produtos:
        #     self._produtos.append(produto)
        # self._produtos.extend(produtos)
        self._produtos += produtos


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)

# carrinho.listar()
# print(carrinho.total)

# Composição
# Os filhos somente existem se o pai existir 

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_end(self, rua, num):
        self.enderecos.append(Endereco(rua, num))
    
    def listar(self):
        for end in self.enderecos:
            print(end.rua, end.num)

class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.num = num

cliente = Cliente('Maria')
cliente.inserir_end('Av Brasil', 123)
cliente.inserir_end('Av xis', 456)

cliente.listar()
# se o cliente for apagado, os endereços sao automaticamente apagos (garbage collector)