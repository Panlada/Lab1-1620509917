number = int(input("enter max value : "))
number =number+1
def ca(number):
    for i in range(1, number):
        if( i % 2 == 0 ):
            print("%d is prime number" % i)
        else:
            print("%d is not prime number" % i)


def cal(number):
    for i in range(1, number):
        if( i % 2 == 0 ):
            print("%d is prime number" % i)


def even(number):
    for i in range(1, number):
        if( i % 2 == 0 ):
            print("%d is prime number" % i)
            
def od(number):
    for i in range(1, number):
        if( i % 2 == 1 ):
            print("%d is not prime number" % i)

OEB = str(input ("Odd or Even or Both O/E/B : "))
pr= "y" or "Y"
po ="O" or "o"
pe="E" or "e"
if OEB == 'O':
     od(number)

elif OEB =='E':
     even(number)

elif OEB =='B':
    YN = input("Only Prime? Y/N : ")

    if YN =='Y':
            cal(number)
    elif YN == 'N':
         ca(number)
    else:
         print("error !")
                
else:
        print("error !")