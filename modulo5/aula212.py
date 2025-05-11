# @property -> getter (metodo para obter atributo)

# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     # getter
#     def get_cor(self):
#         return self.cor
# caneta = Caneta('Azul')
# print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self._cor = cor # o _ na frente do nome significa que nao deve ser utilizado fora do escopo
        # self.cor = cor chama o setter diretamente no init
    # getter pythonico
    @property   
    def cor(self):
        return self._cor
    
    @cor.setter # o setter permite receber valores e configurar 
    def cor(self, valor):
        self._cor = valor

caneta = Caneta('Azul')
# se usar o @property nao pode colocar os parenteses
print(caneta.cor) # parece um atriuto mas esta referindo ao metodo cor
# setter é util para restringir valores recebidos 
caneta.cor = 'Rosa'
print(caneta.cor)