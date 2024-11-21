# #create a list of 5 fruits each fruit on a new line using a for loop.

# fruit_list = [
#     'apple',
#     'mango',
#     'strawberry',
#     'orange',
#     'peer' 
# ]
# print(fruit_list)
#write a function that takes a list of numbers and returns a new list with each number squared.example:[1,2,3] should become [1,4,9]

# def square_numbers():
#     return [number ** 2 for number in numbers]

# numbers = [2, 4, 6, 8]
# squared_numbers = square_numbers()
# print(squared_numbers)


    

    
# #write a python program that takes two lists, list1 = [1,2,3] and list2 = [4,5,6]
# # an combines them into a single list, combined = [1,4,2,5,3,6].

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = list1 + list2
# print(list3)

# #Given a list of numbers,[3,1,4,1,5,9,2], write a program to find and
# # print the two largest numbers in the list without using the max()function 

def two_largest():
    
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return largest, second_largest

numbers = [3, 1, 4, 1, 5, 9, 2]

largest, second_largest = two_largest()
print("The two largest numbers are:", largest, "and", second_largest)
