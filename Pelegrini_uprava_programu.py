from random import *
a = input('Zadaj slovo, raf:')
b = input('Zadaj druhe slovo, temere:')
s = a + b
novy = ''
for i in range(len(s)):
    ktory = randrange(len(s))
    print('Odstraňujem znak', s[ktory])
    novy = novy+s[ktory]
    print('Zatiaľ som vytvoril:', novy)
    s = s[:ktory]+s[ktory+1:]
    print('Ešte zostali tieto znaky:', s)
print('Zamiešané slovo:', novy)
