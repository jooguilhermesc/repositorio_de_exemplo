from conta_bancaria import contaBancaria as CB

#conta_do_joao = CB(nome="João", nr_conta="6589-4",senha="1234",saldo=150.89)

saldo_joao = CB(nome="João", nr_conta="6589-4",senha="1234",saldo=150.89).consulta_saldo(nr_conta="6589-4",senha="1234")

transfere_joao = CB(nome="João", nr_conta="6589-4",senha="1234",saldo=150.89).transfere_valores(nr_conta="6589-4",senha="1234",valor_a_transferir=20)

print(saldo_joao)
print(transfere_joao)