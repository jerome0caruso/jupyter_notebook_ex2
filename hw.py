# Exercise #1
print("Cubed Numbers up to a 1000:")
def cubed():
    num = 0
    while num <= 10:
        print(num ** 3)
        num +=1
        
cubed()        
print("------")

# Exercise # 2
print("Prime Numbers up to a 100:")

def get_prime():
    for num in range(2, 101):    
        if num == 2:
            print(2)
        else:    
            for counter in range(2, num):  
                if num % counter == 0:  
                    break
                elif counter + 1 == num:
                    print(num)

get_prime()

print("------")

# Exercise #3
def is_adult():
    age = int(input("What's your age?"))
    if age < 18:
        print("Kids")
    elif age > 17 and age < 66:
        print("Adults")
    else:
        print("Seniors")     
is_adult()

print("------")