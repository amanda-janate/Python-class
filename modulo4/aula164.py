def concatenar(init):
    valor_final = init
    def interna(conc):
        nonlocal valor_final # essa variavel nao sera limpa sempre carregando o valor da execução anterior
        valor_final += conc
        return valor_final
    return interna

conc = concatenar('a')

print(conc('b'))
print(conc('c'))
print(conc('d'))
print(conc('e'))


