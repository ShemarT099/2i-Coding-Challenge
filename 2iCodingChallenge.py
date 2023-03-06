
# Assume duplicates have been artificially added to the lists
# Import random module to help with generating random Numbers
import random

#Numbers have to be between 1 and 100 
num_list = random.sample(range(100),9)

#Get a number from the list to duplicate
duplicate = num_list[1]

#Add duplicate numbers to the list to have 4 duplicates

num_list[7:9] = [duplicate,duplicate,duplicate]
print("Original List:", num_list)

#Create a new list by using dict.fromkeys because dictionaries do not allow duplicate keys
def read_list(num_list):
    newlist = list(dict.fromkeys(num_list))
    newlist.sort(reverse=True)
    print("Sorted List:",newlist)
read_list(num_list)
