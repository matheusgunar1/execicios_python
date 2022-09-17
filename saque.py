def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta
def saque(conta,valor):
    conta["saldo"] -= valor
    return conta
c1 = cria_conta(123,"juan",200,1000)
c2 = cria_conta(321,"Marcia",1000,1000)
c1=saque(c1,100)
print(c1)