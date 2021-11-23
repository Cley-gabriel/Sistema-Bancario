from banco import Banco
from conta import ContaCorrente, ContaPoupanca
from cliente import Cliente



contap1 = ContaPoupanca (237, 32902, 9.8)
contap2 = ContaPoupanca (209, 90444, 10.6) # Não cadastrada
contac1 = ContaCorrente (211, 50333, 2.5)

cliente1 = Cliente ('Cley', 19, contap1)
# cliente2 = Cliente ('Gabriel', 20, contac1)
cliente3 = Cliente ('Santos', 25, contap2) # Não cadastrado
cliente4 = Cliente('G', 19, contac1)


banco = Banco()

banco.inserir_agencia(237)
banco.inserir_agencia(211)
banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente4)
# banco.inserir_conta(32902)
# banco.inserir_conta(50333)



#AUTENTICAÇÃO DOS CLIENTES 
print('*'*40)

print(cliente1.nome)
if banco.autenticar(cliente1):
    cliente1.conta.depositar(20)

    cliente1.conta.sacar(15)
else:
    print('Autenticação inválida!')
print()


print('*'*40)

print(cliente4.nome)
if banco.autenticar(cliente4):
    cliente4.conta.depositar(100)

    cliente4.conta.sacar(100)
    
    cliente4.conta.sacar(1)
else:
    print('Autenticação inválida!')
print()

print('*'*40)


print(cliente3.nome)
if banco.autenticar(cliente3):
    cliente3.conta.sacar(20)
else:
    print('Autenticação inválida!')
print()

print('*'*40)

# print(banco.clientes)
# print(banco.agencias)