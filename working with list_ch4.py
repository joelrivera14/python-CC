#for loops
magicians=['Chris Angel', 'David Blane', 'Phil Dunphy']
for magician in magicians:
    print(magician)

#writing multiple lines in for loops
magicians=['Chris Angel', 'David Blane', 'Phil Dunphy']
for magician in magicians:
    print(f'that was a cool {magician}')
    print(f'hey {magician} whats next\n')

#using range()
for value in range(5): #can also be written as range(0,5)
    print(value)

numbers=list(range(6))
print(numbers)

#can skip numbers by adding a 3rd argument
num=list(range(0,11,2))
print(num)

#adding items to a list
ls = []
for item in range(11):
    newItem= item ** 2
    ls.append(newItem)
print(ls)

#list comprehension 
squares=[value**2 for value in range(15)]
print(squares)

ls=[]
for value in range(21):
    ls.append(value **3)
print(ls)

#looping through a slice
peoples=['joel','john','jobort','javid']
for people in peoples[:3]:
    print(people.capitalize())

food=['d','c','f','g','s']
newF=food[:]
print(id(newF),id(food))

#tuple uses () and cant change items
tup=(2,3,4)
print(tup)
