"""
name='Jhon'
age=26

print('name: ',name,'age:',age)

# print='print'
#
# print('name: ','age=',age)

# type function

result=type(name)
print(result)
result=type(age)
print(result)

print(5*name)
result1=5*name
result2=type(result1)



result=id(name)
print (result)


print(8+8)
print((8).__add__(8))

print(8 * '#')
print((8).__mul__('text'))
print((8).__mul__('8'))

print(8-8)
print((8).__sub__(8))
print(8/8)
print((8).__truediv__(8))

print(8**8)
print((8).__pow__(8))
# Float

var=(8).__truediv__(8)
print(type(var))

a=3
b=4
c=5
x=(-b+(b**2)-4*a*c)**(1/2))2*a




#Float


bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)


"""

#Complex


nr1=1.0+1.0j
nr2=3j
print(nr1+nr2)
print(type(nr1+nr2))

# Stringsw
my_str1='My String'
print(my_str1)
my_str1='''My String'''

my_str2=r"My String \n no multi line"
print(my_str2)

my_str2=f"""My String{my_str1}"""
print(my_str2)






#dir
info=dir(my_str2)
print(info)

var1 = 'this is my text'
cap = var1.capitalize()
print(cap)
format=var1.format('Sparta')
print(format)

phone="0747.655.444"
split1 = phone.split("7")
print(split1)


#input
#name=input('Give me your name :')

#slice
text1="MY text"
first_letter="My text"[0]
print(first_letter)
slice1=text1[1:4]
print(slice1)
slice2=text1[0:7:3]
print(slice2)

#
text=input('Enter 10 charcater text here:')
slice1=text[0:5]
splice2=text[5:10]
#print(slice2+slice1)
#print(slice1)
#print(slice2)

#negative step
#reverse=text[::-1]
#print(reverse)

reverse1=slice1[::-1]
reverse2=slice2[::-1]
print(reverse2+reverse1)

#True,False
my_bool=True

print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

print(True+False)
print(dir(True))
x=True.__add__(False)
print(x)

#None

my_none=None
x=print('')
print(x)

# Truth

 print(bool(0+0j))
print(bool(0+0j))