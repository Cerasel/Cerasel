#function

#general construction

def my_function1(arg1,arg2,arg3,kwarg1='',kwarg2='\n'):
     print(arg1,arg2,arg3,sep=kwarg1,end=kwarg2)
     return arg1 + arg2 + arg3



#create function for determining prime number

def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True
print(is_prime(3))


# list
empty_list=[]
my_list1=[1,2,3]
print(my_list1)
my_list1.append(4)


def primes (limit):
    result=[]

    for i in range(1, limit):
        if (is_prime(i) == True):
            result.append(i)
    return result


print(primes(10))


  # bit operation

  #01010001
  #01110011

  #01110011-OR
  #01010001-AND
  #00100010-XOR
  ################

#00100010
#01110011

#01010001

#numberes in memory

0 # 00000000000...000
1 # 00000000000...001
2 # 00000000000...010

# And
10&11
10# 00000000000...1010
11# 00000000000...1011

# 0000000000000...1010

#OR
print (10|11)
10# 00000000000...1010
11# 00000000000...1011
#00000000000000...1011

#XOR
print (10^11)
10# 00000000000...1010
11# 00000000000...1011
# 0000000000000...0001



#XOR negative number
print (-1^3)
-1 # 11111111111...1111 -1
3  # 00000000000...0011
# 11111111111111...1100

def enc_dec(text, key):
    result = ''
    for letter in text:
        number = ord(letter)
        # print(chr(number ^ key))
        result += chr(number ^ key)
    return result

output = enc_dec("Hello World", 20500)
print(output)
output_dec = enc_dec(output, 20500)
print(output_dec)

#
def add_numbers():
    sum = 0
    num_list =[]
    while sum <= 100 :
        if sum==100:
            break
        nr = int(input("Ad numbers = "))
        if nr  >= 0 :
           sum= sum + nr
           num_list.append(nr)
    else:
        if sum == 100:
            return num_list
        else:
            return sum

    if sum == 100 :
        return num_list
    else :
     return sum
    return num_list
print(add_numbers())




