#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#Date: 28 April 2021


"""
Write a Python program to get the largest number from a list.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list with 10 items

largest = 0

for x in my_list:
    if x > largest:
        largest = x

print("The largest number is ", largest)