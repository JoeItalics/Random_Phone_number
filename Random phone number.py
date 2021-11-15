import random

# Asks user for arera code
areaCode = int(input('What area code? '))

def createNumber(areaCode):
    second = random.randint(100, 888)
    third = random.randint(1001 - 8989)
    if third  in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = random.randint(2000, 8819)
    
    return f"{areaCode}-{second}-{third}")
    
amount = int(input("How many numbers would you like?"))

for i in range(0, amount):
    print(createNumber(areaCode))
        

# Function to create random 7 digits
#def AAa():
    #global Aa
    #second = random.randint(100,888)
    #last = random.randint(1000, 8888)

    #while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
     #   last = random.randint(2000, 8819)

    
    #return'{}-{}-{}'.format(Aa, second, last)

#ammount = int(input('How many phone numbers do you need?'))

#for i in range(0, ammount):
    #print(AAa())
