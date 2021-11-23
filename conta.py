from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Você depositou {valor}')
        print(f'Seu saldo é de {self.saldo}')
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: R${self.saldo:.2f} ')

    @abstractmethod
    def sacar(self, valor):
        pass
    
#Conta corrente com limite de saque.
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 1500):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        print(f'Você fez um saque de R${valor}')
        self.detalhes()

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo insuficiente, você tentou sacar R${valor} e o seu saldo é de R${self.saldo}')
            return
            
        self.saldo -= valor
        print(f'Você fez um saque de R${valor:.2f}')
        self.detalhes()
        
