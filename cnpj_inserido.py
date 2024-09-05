'''
Esse código é caso você não queira inserir uma planilha para fazer tratamento, se quiser tratar uma quantidade isolada de CNPJS
'''
#adicona nessa lista os CNPJS que deseja realizar o tratamento.
#IMPORTANTE: INSIRA O CNPJ AQUI 
cnpjs_lista = ["23.444.277/0001-76"


]

#função para remover caracter
def remover_caracter(cnpj):
  return cnpj.replace(".", "").replace("/", "").replace("-", "")

#aplicando a função para limpar todos os cnpjs na lista
retirando_caracter = [remover_caracter(cnpj) for cnpj in cnpjs_lista]

print(retirando_caracter)