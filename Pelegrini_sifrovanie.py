vstup = input('Zadaj text:')
posun = int(input('Zadaj počet posunutí:'))
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+posun)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print('Zašifrované slovo:'+sifra)

sifra2 = sifra
sifra = ''

for znak in sifra2:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)-posun)
    if znak == 'a':
        novyznak = 'z'
    sifra = sifra+novyznak
print('Odšifrované slovo:'+sifra)