def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor
    return conta

def saque(conta,valor):
    conta["saldo"] -= valor
    return conta

c1 = cria_conta(123,"Juan",200,1000)
c2 = cria_conta(321,"Marcia",1000,1000)

print(c1)
c1 =deposita(c1,500)
print(c1)

print(c2)
c2 = deposita(c2,1000)
print(c2)

c1=saque(c1,300)
print(c1)

c2=saque(c2,650)
print(c2)

print("----------------------------------------")