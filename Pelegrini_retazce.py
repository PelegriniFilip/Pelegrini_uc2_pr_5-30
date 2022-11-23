
veta1 = 'Programujeme v Pythone'
veta2 = 'Najdalej som bol v Budči'
for i in range(len(veta1)):
    print(veta1[i],end='')
    print(veta2[i],end='')
    
print('')
print(veta1)
print(veta2)

veta = input('Napíš vetu s interpunkčným znamienkom.')
pocet = 0
if veta[-1] == '!':
    print('Napísal si rozkazovaciu vetu')
elif veta[-1] == '?':
    print('Napísal si opytovaciu vetu')
else:
    print('Napísal si klasik vetu')