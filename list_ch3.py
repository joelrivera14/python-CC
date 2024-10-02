#accessing list item through index
l=['bike', 'scooter', 'board']
print(l[0])
print(f'i used to have {l[0].capitalize()} \n{l}')

l[0]='skates'
print(f'i used to have {l[0]} \n{l}')

fstring=f'i used to have a {l[1].capitalize()}'
print(fstring)

#adding items with methods
l.append('tricycle')
l.extend(['banana', 'orange', 'grape']) #remember to add [] if you want to add multiple items
l.insert(0, 'apple')
print(l)

#deleting or removing
del l[0]
l.pop(-1)
l.remove('skates')
print(l)

#sorting
print(sorted(l)) #sorts list temporily
l.sort(reverse=True) #sort() sorts permanently
print(l)

#getting length with len()
print(len(l))