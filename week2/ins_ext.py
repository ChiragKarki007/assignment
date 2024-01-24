listr = [21,14,31,54,23,73]

print("The list before insert and extend",listr)

l = len(listr)


ins = int(input("Enter a number to insert in the given list: \n"))

ind = int(input(f'Enter an index between 0 and {len(listr)-1} to add the number in: \n'))

listr.insert(ind,ins)

print(f'The list after insert() is {listr}')

listr.extend((56,62))
listr.extend((42,38,66))

print(f'The list after insert() and extend() is {listr}')

