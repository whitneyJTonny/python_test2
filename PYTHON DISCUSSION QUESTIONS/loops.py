#write a python that prints all even numbers between 1 and 20 using a for loop

def even_numbers():
    for even in range(1,21,2):
        print(even)
even_numbers()

#use a while loop to ask the user to input a number untill they provide a number greater than 10

while True:
    number = int(input("Enter a number: "))
    if number > 10:
        print("You entered a number greate than 10")
        break
    else:
        print("The number must be greater than 10. Try again.")
    
#write a programm that prints the multiplication table (from 1 to 10)for numbers  from 1 to 5 using nested for loops.

for m in range(1,6):
    print(m)
    for j in range(1,11):
        print(f"{m} * {j} = {m * j}")
        
#Given a list of integers,[4,7,2,9,12,15], write a program using a for loop to find the sum of all odd numbers and print the result


numbers = [4,7,2,9,12,15]
sum_of_odd_numbers = 0
for num in numbers:
    if num % 2 != 0:
        sum_of_odd_numbers+=num
print("sum of odd numbers:",sum_of_odd_numbers)

