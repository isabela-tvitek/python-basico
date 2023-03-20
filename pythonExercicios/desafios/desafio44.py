print('{:=^40}'.format(' LOJAS GUANABARA '))

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor = preco - (preco * (10/100))
elif opcao == 2:
    valor = preco - (preco * (5/100))
elif opcao == 3:
    valor = preco
    vp = valor / 2
    print('Sua compra será parcelada em 2X SEM JUROS de R${:.2f}'.format(vp))
elif opcao == 4:
    valor = preco + (preco * (20/100))
    parcela = int(input('Quantas parcelas? '))
    vp = valor/parcela
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(parcela, vp))
else:
    valor = preco
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
