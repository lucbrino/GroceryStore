from model import *

class CategoriaDao:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('Categorias.txt', 'a') as arq:
            
            arq.writelines(categoria.categoria) 
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('Categorias.txt', 'r') as arq:
            
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))    
        
        cat = []
        
        for i in cls.categoria:
            cat.append(Categoria(i))
            
            return cat 

class PessoaDao:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('Pessoas.txt', 'a') as arq:
            
            arq.writelines(pessoa.nome + '|' + pessoa.telefone + '|' + pessoa.cpf + '|' + 
                           pessoa.email + '|' + pessoa.endereco)
            arq.writelines('\n')          

    @classmethod
    def ler(cls):
        with open('Pessoas.txt', 'r') as arq:
            
            cls.pess = arq.readlines()
        
        cls.pess = list(map(lambda x: x.replace('\n', ''), cls.pess))    
        cls.pess = list(map(lambda x: x.split('|'), cls.pess))
        
        pess = []
        
        for i in cls.pess:
            
            pess.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
            
        return pess
        
class FuncionarioDao:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('Funcionarios.txt', 'a') as arq:
            
            arq.writelines(funcionario.clt + ' ' + funcionario.nome + ' ' + funcionario.telefone + ' ' + 
                           funcionario.cpf + ' ' + funcionario.email + ' ' + funcionario.endereco)
            arq.writelines('\n')  

    @classmethod
    def ler(cls):
        
        with open('Funcionarios.txt', 'r') as arq:
        
            cls.func = arq.readlines()
        
        cls.func = list(map(lambda x: x.replace('\n', ''), cls.func))    
        cls.func = list(map(lambda x: x.split('|'), cls.func))
        
        func = []
        
        for i in cls.func:
            
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return func    
        
class ProdutoDao:
    @classmethod
    def salvar(cls, produto: Produto):
        with open('Produtos.txt', 'a') as arq:
            
            arq.writelines(produto.nome + ' ' + produto.categoria + ' ' + str(produto.preco))
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('Produtos.txt', 'r') as arq:
            
            cls.prod = arq.readlines        
        
        cls.prod = list(map(lambda x: x.replace('\n', ''), cls.prod))
        cls.prod = list(map(lambda x: x.split('|'), cls.prod))    
        
        prod = []
        
        for i in cls.prod:
            
            prod.append(Produto(i[0], i[1], i[2]))
            
        return prod    
                
class EstoqueDao:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open('Estoque.txt', 'a') as arq:
            
            arq.writelines(estoque.nome + '|' + str(estoque.quantidade) + '|' + estoque.local)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('Estoque.txt', 'r') as arq:
            
            cls.estoq = arq.readlines()
        
        cls.estoq = list(map(lambda x: x.replace('\n', ''), cls.estoq))
        cls.estoq = list(map(lambda x: x.split('|'), cls.estoq))      
        
        estoq = []
        
        for i in cls.estoq:
            
            estoq.append(Estoque(i[0], i[1], i[2]))  
            
        return estoq              
                    
class FornecedorDao:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('Fornecedores.txt', 'a') as arq:
            
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' + fornecedor.telefone + '|' + 
                           fornecedor.email + '|' + fornecedor.categoria + '|' + fornecedor.endereco)                                    
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('Fornecedores.txt') as arq:
            
            cls.forn = arq.readlines()
            
        cls.forn = list(map(lambda x: x.replace('\n', ''), cls.forn))
        cls.forn = list(map(lambda x: x.split('|'), cls.forn)) 
        
        forn = []
        
        for i in cls.forn:   
            forn.append(Fornecedor(i[0], i[1], i[2], i[3], i[4], i[5]))
            
        return forn    
            
class VendaDao:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('Vendas.txt', 'a') as arq:
            
            arq.writelines(venda.itemVendido.nome + '|' + venda.itemVendido.preco + '|' +    
                           venda.itemVendido.categoria + '|' + venda.vendedor + '|' + 
                           venda.comprador + '|' + str(venda.quantidadeVendida) + '|' + venda.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('Vendas.txt', 'r') as arq:
            
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))    
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vend = []
        
        for i in cls.venda:
            
            vend.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], [5], i[6]))
        
        return vend       
   
x = FornecedorDao.ler()

print(x[0].cnpj)

