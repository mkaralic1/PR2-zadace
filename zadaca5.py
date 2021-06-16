def brojevi(broj):   
    if n%2==0:
        yield print('  Parni broj:',n)
    else:
        yield print('Neparni broj:',n)

broj=int(input('Unesite broj:' ))

for n in range(1,broj): 
    next(brojevi(n))


