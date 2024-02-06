"""
NameError - neexistující proměnná
KeyError - neexistující klíč ve slovníku
ZeroDivisionError - dělení nulou
TypeError - špatný dat. typ
SyntaxError - špatná syntaxe
"""

#print(x) - vyhodí NameError a skript dál nepokračuje

try:
    print("asdas") 
except: #except zachytí NameError a vykoná kód níže
    print("Nastala chyba")
else: #vykoná se v případě, že nenastane žádná chyba
    print("Nenastala zadna chyba")
finally: #vykoná se na konci try except bloku bez ohledu na to, zda se vyhodila chyba nebo ne
    print("Try except blok skoncil")
    
x = -3

#if x < 0:
#    raise Exception("Cislo je mensi nez 0") #vyhozeni vlastni chyby s vlastni chybovou hlaskou


try:
    a = int(input("Cislo 1: "))
    b = int(input("Cislo 2: "))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
except:
    print("Nastala nějaká chyba")