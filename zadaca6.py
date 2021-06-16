def rekurzija(string, n):    
    if n==1:
        return string[0]
    else:
        print(string[n-1], end='')
        return rekurzija(string, n-1)

unos=str(input('Unesite string: '))
duljina=len(unos)

print(rekurzija(unos, duljina))

