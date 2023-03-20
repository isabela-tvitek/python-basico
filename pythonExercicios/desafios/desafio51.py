print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

ut = pt+(10-1)*r
for pa in range(pt, ut+r, r):
    print('{}'.format(pa), end=' -> ')
print('ACABOU')