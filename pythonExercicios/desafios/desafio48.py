# s = 0
# n = 0
# for c in range(1, 500):
#     i = c % 2
#     if i == 1:
#         m = c % 3
#         if m == 0:
#             n += 1
#             s += c
# print('A soma dos {} valores é igual a {}'.format(n, s))

s = 0
n = 0
for c in range(1, 500, 2):
    m = c % 3
    if m == 0:
        n += 1
        s += c
print('A soma dos {} valores é igual a {}'.format(n, s))
