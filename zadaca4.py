import re

while True:
    mail=input('Unesite mail: ')
    regex1='^[a-z]*.[a-z]*@(fpmoz.sum.ba)$'
    rezultat1=re.match(regex1, mail)
    if rezultat1:
        print('Uspješno unesen e-mail.')
        break
    else:
        print('Pogrešno Ste unjeli e-mail.')

while True:
    eduId=input('Unesite eduId: ')
    regex2='^[a-z]*([0-9]*)?(@sum.ba)$'
    rezultat2=re.match(regex2, eduId)
    if rezultat2:
        print('Uspješno unesen eduId.')
        break
    else:
        print('Pogrešano Ste unjeli eduId.')       
