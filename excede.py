# O comando def define uma função. Cria os limites do que est´sendo criado.
def cria_conta(numero,titular,saldo,limite):
    conta={"Número": numero, "Titular": titular, "Saldo": saldo,"Limite": limite}
    return conta
c1 = cria_conta(123, "Juan", 1000, 5000)
c2 = cria_conta(456, "Matheus", 3500, 6000)
print(c1)
print(c2)
