print('-'*30)
print('LOJAS SUPER BARATÃO')
print('-'*30)
s = cont = mais = maisBarato = 0
maisBaratoNome = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    if cont == 1:
        maisBaratoNome = produto
        maisBarato = preco
    else:
        if preco < maisBarato:
            maisBaratoNome = produto
            maisBarato = preco
    s += preco
    if preco > 1000:
        mais += 1
    # -------------------------------------------------------------------
    opcao = ' '
    while opcao not in 'SN':
        print('-' * 30)
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    # -------------------------------------------------------------------
    if opcao == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi R${:.2f}'.format(s))
print('Temos {} produtos custando mais de R$1000.00'.format(mais))
print('O produto mais barato foi {} que custa R${}'.format(maisBaratoNome, maisBarato))
