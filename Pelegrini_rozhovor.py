from random import *
meno = input('Ako sa voláš?')
print('Ahoj '+meno+' rád Ťa spoznávam :)')
roknarodenia = int(input(meno+', v ktorom roku si sa narodil?'))
rok=int(input('aký je rok?'))
otazka = input('žije sa ti dobre?')
print('To je zaujímavé.')
vek = rok - roknarodenia
chybanie = 100 - vek
vek = str(vek)
chybanie = str(chybanie)
print(meno +' takže máš '+ vek +' rokov a žiješ v divnej dobe.')
print(meno +' do dovŕšenia "stovky" ti chýba ešte '+ chybanie +' rokov.') 
