c = str(input("Em que cidade você nasceu? ")).strip()
separa = c.split()
isEqual = 'santo' in separa[0].lower()
print('A cidade que você nasceu come com Santo? {}'.format(isEqual))

