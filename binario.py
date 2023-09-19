n = int(input('numero a ser binario: '))
m = n
rest = []
while int(n) >= 1:
    rest.append(n%2)
    n = int(n/2)
rest.append(int(n/2))
p = 0
for i in range(len(rest)-1):
    if i != len(rest)-2:
        
        p += rest[i]*2**i
        d = rest[i]*2**i
        print(f'{rest[i]} * 2**{i} = {d}\n    + ')
    else:
        p += rest[i]*2**i
        print(f'{rest[i]} * 2**{i} = {d}')
print(f'{p}')
if m == p:
    print('Tudo certo!')
print('binário: ',end='')
for i in range(len(rest)-1):
    print(f'{rest[i]}',end='')
print(f'\nnatural: {p}')
    
