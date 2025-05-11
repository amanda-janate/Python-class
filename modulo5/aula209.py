class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # é um decorator
    def create_50_yrs(cls, name): # permite acesso à classe, mas nao à instancia 
        return cls(name, 50)
    
    @staticmethod # este é um caso inutil pois não possui acesso nem ao self e nem ao cls 
    def funcao(*args, **kwargs): # é o mesmo que fazer a função externa à classe
        print(args, kwargs)


p1 = Pessoa.create_50_yrs('Amanda')

print(vars(p1))

p1.funcao(1,2,3, nomeado='A')