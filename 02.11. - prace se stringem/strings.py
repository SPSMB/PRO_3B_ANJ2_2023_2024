pc = "pocitac"
print(pc[0]) #vypise prvni znak
print(pc[2:5]) #vypise znaky od druheho indexu do pateho
print(pc[:3]) #vypise prvni tri znaky
print(pc[3:]) #vypise vsechno krome prvnich tri znaku
print(pc[::-1]) #vypise obracene

druhe_slovo = "kdo chce "
vys = druhe_slovo + pc #spojeni dvou textu
print(vys)
vys2 = druhe_slovo[:4] + pc #spojeni prvnich 4 znaku z druhe_slovo se slovem pc
print(vys2)

count = len(druhe_slovo) #vrati pocet znaku
print(count)

print(pc[-1]) #vypise posledni pismeno
print(pc[-3:]) #vypise posledni tri znaky

escape = "Moje jmeno neni \"Vojta\""
print(escape) #vypise Vojta v uvozovkach

for x in escape: #procykli text v escape
    print(x)

print("a" in pc) #True pokud "a" je ve slove pocitac
print("a" in pc and not "b" in escape) #True pokud "a" je v pc a zaroven "b" neni v escape
 
print(pc.lower())#text bude cely malym pismem
print(pc.upper())#text bude cely velkym pismem
print(escape.title())#kazde slovo bude mit prvni pismeno velke
print(escape.split(" "))#rozdeli slovo vsude, kde je mezera (delimiter)
print(escape.strip())#odstrani mezery na zacatku a na konci
print(escape.replace("j","k"))#nahradi pismeno j za pismeno k
print(escape.find("a"))#vrati index na kterem se nachazi a
