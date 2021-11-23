class Banco:
    def __init__(self):
        self.agencias = []
        self.contas = []
        self.clientes = []
        
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente.nome)
        self.contas.append(cliente.conta)

    def inserir_agencia(self, agencia): 
        self.agencias.append(agencia)  

    
    def autenticar(self, cliente):
        if cliente.conta.agencia not in self.agencias:
            print(f'Agência {cliente.conta.agencia} não pertence a esse banco')
            return False
        
        if cliente.nome not in self.clientes:
            print(f'Cliente {cliente.nome} não pertence a esse banco.')
            return False

        if cliente.conta not in self.contas:
            print(f'Conta {cliente.conta.conta} não pertence a este banco.')

            return False

        return True






