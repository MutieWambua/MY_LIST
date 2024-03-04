# this is the assignment one of week 2 plp

#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.

My_list = []
#appending 10,20,30 and 40
My_list.append(10)
My_list.append(20)
My_list.append(30)
My_list.append(40)

print(My_list)

#insert15
My_list.insert(1,15)
print(My_list)# to confirm
#extending mylist
My_list.extend([50,60,70])
print(My_list)
#remove last-elemnt
del My_list[-1]

My_list.sort() #sorted in ascending

print(My_list) #confirm elemnt deleted and sorted in asc-order
#Finding and printing  the index of 30
print(My_list.index(30))

