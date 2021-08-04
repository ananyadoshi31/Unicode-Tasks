from collections import Counter , OrderedDict
class OrderedCounter (Counter ,OrderedDict):
    pass
list_one=[]
n = int(input("Enter the total number of words: "))
for e in range(0,n):
    number = input("Enter the elements: ")
    list_one.append(number)
element = OrderedCounter(list_one)
list_two = set(list_one)
print(len(list_two))
for z in element:
    print(element[z],end="")










