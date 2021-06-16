from csv import reader
with open('rezultati.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    rezultati = list(map(tuple, csv_reader))
imena=[]
prezimena=[]
ocjena=[]
for ime, prezime, bodovi in rezultati:
    imena.append(ime)
    prezimena.append(prezime)
    if int(bodovi)>90:
        ocjena.append('5')
    elif int(bodovi)>80:
        ocjena.append('4')
    elif int(bodovi)>65:
        ocjena.append('3')
    elif int(bodovi)>49:
        ocjena.append('2')
    else:
        ocjena.append('1')
studenti=list(zip(prezimena, ocjena))
prezimena.sort()
rijecnik={}
for prezime in prezimena:
    for p,o in studenti:
        if prezime in p:
            rijecnik[prezime]=o
print(rijecnik)



        
