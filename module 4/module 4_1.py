# dict

empty_dict={}

my_dict={1 : 'one' , 'two': 2, 3:[], 4: {}}
print(my_dict)

#hash
print('one'.__hash__())
#print([1,2,3].__hash__())


#dict methods

print (my_dict.keys())
print(type(my_dict.keys()))
for key in my_dict.keys():
    print(key)

print(80*'#')

for value in my_dict.keys():
    print(value)

#print(80*'#')
#for item in my_dict.item():

#get value

print(my_dict[1])
print(my_dict.get(1))
#print(my_dict[2])
print(my_dict.get(2), 'Not a value')


