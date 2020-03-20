from invoice import Invoice, TaxCE, TaxRJ, TaxSP

if __name__ == "__main__":

    # a variavel invoice recebe uma instancia da classe Invoice e declara a estrategia inicial
    # com o imposto de São Paulo
    invoice = Invoice(TaxSP())

    #exibindo a mensagem com o calculo do valor do imposto em SP
    invoice.print_tax_calculation(100)

    print()

    #definindo a estrategia com o imposto de RJ
    invoice.strategy = TaxRJ()
    #exibindo a mensagem com o calculo do valor do imposto em RJ
    invoice.print_tax_calculation(50)

    print()
    
    #definindo a estrategia com o imposto de CE
    invoice.strategy = TaxCE()
    #exibindo a mensagem com o calculo do valor do imposto em CE
    invoice.print_tax_calculation(45)
