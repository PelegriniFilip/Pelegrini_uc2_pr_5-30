veta = input('Napíš vetu:')
s=' '
for i in range(len(veta)):
    print(s + veta[i])
    s = s + ' '

s = 'Python'
for i in range(len(s)):
    ns = '*'*(len(s)-i)+s[:i+1]
    print(ns)