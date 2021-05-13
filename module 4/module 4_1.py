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
#print(my_dict.get(2), 'Not a value')

# calculete factorial

#n!=1! * 2! *3!...n!

def factorial(number):
    n=int(number)
    for i in range (1,n):
        n=n*i
    return(n)

    factorial(input())


    def factorial(number):
        result=1
         for i in range(1,number+1):
              result *=1
              return result
def factorial (n):
    if(n<=1):
        return 1
    else:
        return n*factorial(n-1)

for i in range(10):
    print(factorial(i))



#append vs extend

a=[1,2,3]
b=[3,4,5]
print(a.append(b))
print(a)
a.extend


#sets
my_empty_set=set()
print(my_empty_set)


my_set=set([1,2,3])
print(my_set)


set_a=set([1,2,3,4])
set_b=set([3,4,5.6])

#set operations
 set_a.union(set_b)
 set_a.difference(set_b)

 set_b.difference(set_a)

 set_a.difference_update(set_b)
 set_a.symmetric_difference(set_b)

 #local nonlocal #global
  global g_var1
     g_var1=a
     def check_g()
    g_var1='b'
   g_var1 +='c'
   ln_var1='d'
    print(g_var1)
    def check_n():
        print('in n function',g_var1)
        check_n()


check_g()
print(g_var1)
    g_var1='c'
