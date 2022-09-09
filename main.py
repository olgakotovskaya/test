

l = []
c = 0


while True:
    user = eval(input('Enter your numbers: '))
    if user == 'end':
        break
    #print(user)
    elif user:
        l.append(user)
        c = c + 1
        print('COUNT',c)
print(f'The number in the list: {l}')
print(f'Total: ',sum(l))
print(f'Avarage: ',sum(l)/c)
print(f'SUM OF COUNT {c}')

print(f'my name is python and i m best programmer')