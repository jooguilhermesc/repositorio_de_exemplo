class contaBancaria:
    
    def __init__(self, nome, nr_conta, senha, saldo):
        self.__nome = nome
        self.__nr_conta = nr_conta
        self.__senha = senha
        self.__saldo = saldo
    
    def __verifica_se_existe(self, nr_conta, senha):
        
        if self.__nr_conta == nr_conta and self.__senha == senha:
            return True
        else:
            return False
    
    def consulta_saldo(self, nr_conta, senha):
        if self.__verifica_se_existe(nr_conta=nr_conta, senha=senha):
            return f"O saldo da conta {self.__nr_conta}, de propriedade de {self.__nome}, é de R${self.__saldo}"
        else:
            return "Houve um erro na verificação do saldo da conta"
    
    def transfere_valores(self, nr_conta, senha, valor_a_transferir):
        
        saldo_disponivel = self.__saldo - valor_a_transferir
        
        if self.__verifica_se_existe(nr_conta=nr_conta, senha=senha) and saldo_disponivel >= 0:
            return f"Seu novo saldo é de R${saldo_disponivel}"
        elif self.__verifica_se_existe(nr_conta=nr_conta, senha=senha) and saldo_disponivel < 0:
            return "Saldo insuficiente para esta operação"
        elif not self.__verifica_se_existe(nr_conta=nr_conta, senha=senha):
            return "Os dados da sua conta estão errados"
        else:
            return "Erro desconhecido na operação"