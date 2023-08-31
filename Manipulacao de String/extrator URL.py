class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1 : ] # quando se omite o segundo argumento (após :), o fatiamento é até o final da STRING
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1 
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor) # procura & a partir de indice_valor
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]    
        return valor


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")     
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)