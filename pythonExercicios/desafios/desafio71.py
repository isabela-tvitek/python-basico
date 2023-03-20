print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
# c50 = c20 = c10 = c1 = 0
# while True:
#     if total >= 50:
#         total -= 50
#         c50 += 1
#     elif total >= 20:
#         total -= 20
#         c20 += 1
#     elif total >= 10:
#         total -= 10
#         c10 += 1
#     elif total >= 1:
#         total -= 1
#         c1 += 1
#     else:
#         break
# print('Total de {} cédulas de R$50'.format(c50))
# print('Total de {} cédulas de R$20'.format(c20))
# print('Total de {} cédulas de R$10'.format(c10))
# print('Total de {} cédulas de R$1'.format(c1))

ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed += 1
    else:
        print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break

print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
