from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        
class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
            
        
class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        
class Estoque:
    def __init__(self, nome, quantidade, local):
        self.nome = nome
        self.quantidade = quantidade
        self.local = local       
        
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, categoria, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.categoria = categoria
        self.endereco = endereco
        
class Venda:
    def __init__(self, itemVendido: Produto, vendedor: Pessoa, comprador: Pessoa, quantidadeVendida, data = datetime.now().strftime('%d/%m/%y')):
        self.itemVendido = itemVendido
        self.vendedor = vendedor 
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data