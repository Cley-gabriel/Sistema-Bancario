"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

"""

class Pessoa: 

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):

    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    # acesso à lista de clientes e de contas que está dentro do banco
    def __repr__(self): 
        return f'Cliente({self.nome})'
