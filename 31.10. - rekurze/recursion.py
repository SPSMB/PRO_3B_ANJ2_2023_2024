def sum(number):
    print(number)
    if number < 5:
        sum(number+1) #Zavolame znovu na stejnou funkci
sum(0)
print("------------------")

def aritm(start,diference,maxPocet,pocet=0):
    print(start)
    pocet+=1
    if pocet<maxPocet:
        aritm(start+diference,diference,maxPocet,pocet)
aritm(2,3,5)

print("----------------")

def fibonacci(maxCount,count=2,first=0,second=1):
    count+=1
    third=first+second
    print(third)
    first=second
    second=third
    if count < maxCount:
        fibonacci(maxCount,count,first,second)
print(0)
print(1)
fibonacci(10)