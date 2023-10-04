def faktorial (bilangan) :
    if bilangan == 0 :
        return (1)
    else :
        return(bilangan*faktorial(bilangan-1))

jawab = 'Y'
while jawab == 'Y' :
    bilangan = int(input("Berapa banyak Bilangan : "))
    for i in range (1,bilangan+1,1) :
        print(i,'!', '=', faktorial(i))
    jawab = input("Ulang program? (y/t) :")

print("aaa");
