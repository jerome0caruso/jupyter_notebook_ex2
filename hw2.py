# Exercise #1
print("Exercise #1")
# Use the following list - [1,11,14,5,8,9]
my_list = [1,11,14,5,8,9]
def under_ten(list):
    print([n for n in list if n < 10])

under_ten(my_list)

print("")
print("-----")
print("Exercise #2")
# # Exercise #2
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def comb_sort(l1, l2):
   l3 = l1 + l2
   l3.sort()
   print(l3)

comb_sort(l_1, l_2)  

print("")
print("-------")  
print("Exercise #3")
# Excercise #3

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

def create_name(l1, l2):
    total_name = []
    for i in range(len(l1)):
        total_name.append(f"{l1[i]} {l2[i]}")
    print(total_name)
create_name(first_name, last_name)

print("--end--")