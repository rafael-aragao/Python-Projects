class Pagamento:
    def processar(self):
        pass


class Cartao(Pagamento):
    def processar(self):
        print("Pagamento com cartão")


class Boleto(Pagamento):
    def processar(self):
        print("Pagamento com boleto")


class Pix(Pagamento):
    def processar(self):
        print("Pagamento com PIX")


pagamentos = [Cartao(), Boleto(), Pix()]

for p in pagamentos:
    p.processar()