def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - n

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-'*20)
n = int(input('Em que ano você nasceu? '))
print(voto(n))
