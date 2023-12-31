url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"

# limpeza da URL
url = url.strip() # retirar os espaços em branco da url

# Validação d URL
if url == "":
    raise ValueError('A URL está vazia')

# separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1 : ] # quando se omite o segundo argumento (após :), o fatiamento é até o final da STRING
print(url_parametros)

# Busca o valor de um parâmetro 
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1 
indice_e_comercial = url_parametros.find('&', indice_valor) # procura & a partir de indice_valor
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]    

print(valor)     
