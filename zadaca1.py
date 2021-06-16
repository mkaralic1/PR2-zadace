import random

imena=['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']


rijecnik={}

for ime in imena:
    rijecnik[ime]=random.randint(1,5)

#print (rijecnik)

jedan=0
dva=0
tri=0
cetiri=0
pet=0
brojstudenata=0

for student in rijecnik:
    brojstudenata+=1
    if rijecnik[student]==1:
        jedan+=1
    if rijecnik[student]==2:
        dva+=1
    if rijecnik[student]==3:
        tri+=1
    if rijecnik[student]==4:
        cetiri+=1
    if rijecnik[student]==5:
        pet+=1
    
print(pet, 'studenata ima ocjenu 5,',cetiri,'studenata ima ocjenu 4,',tri,'studenata ima ocjenu 3,',dva,'studenata ima ocjenu 2 i',jedan,'studenata ima ocjenu 1.')
prolaz=(dva+tri+cetiri+pet)/brojstudenata*100
print (prolaz,'% studenata ima prolaznu ocjenu.')

