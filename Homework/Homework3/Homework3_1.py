# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
       result = []
       for i in list_of_objects:
               if type(i) == tuple:
                    j= len(i)
               else :
                   j = int(i)
               result.append(j)
       return sorted(result, reverse=True)


print(ordered_ints([1, True, '123', False, 6, ()]))