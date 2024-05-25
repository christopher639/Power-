#Creating Empty list
my_list = []
#adding items in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#manupulation , inserting 15 in index[1] which is the second postion
my_list.insert(1,15)
#create another list
list_two = [67,45,67,465]
#extending my list
my_list.extend(list_two)
# sorting the extende list which is my_list
my_list.sort()
print(my_list)
#printing the index of value 30
index_of_30 = my_list.index(30)
print(index_of_30)
