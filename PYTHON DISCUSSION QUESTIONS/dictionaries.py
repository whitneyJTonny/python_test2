# # #create a dictionary with three key-value pairs representing a student's information:name, 
# # # age and grade. print each key-value pair on a new line.

dict = {
    'name':'Patricia',
    'age':24,
    'grade':'A'
}
print(f"\nThe student name:{dict['name']}")
print(f"The student age :{dict['age']}")
print(f"The student grade :{dict['grade']}",'\n\n')

# # #write a function that takes a dictionary of people's names and their ages,
# # # {'Alice':24, 'Bob':19, 'Charlie':30}, and returns a list of names of people who are 21 or older.

dct = {'Alice':24, 'Bob':19, 'Charlie':30}
adults = [name for name,
          age in dct.items()
          if age >=21]
print(adults)

def adults():
    dict ={'Alice':24, 'Bob':19, 'Charlie':30}
    dict.pop('Bob')
    print(dict)
adults()

# #Given a dictionary representing items in a store with their prices,
# # {'apple':0.5, 'banana':0.3, 'orange':0.7},write a program that takes a list of items bought,
# # ['apple', 'orange', 'banana','banana'], and calculates the total cost.

dict = {'apple':0.5, 'banana':0.3, 'orange':0.7}
list = ['apple', 'orange', 'banana','banana']
total_cost = 0
for character in list:
    total_cost+=dict[character]
print(f"The total cost of items bought is:{total_cost}")
    

    
# # #write a program that counts the occurences of each word in a given sentence.
# # # Example: for the sentence "hello world hello" the output sould be{'hello':2, 'world':1}

def count_word():
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word,  0) + 1
    return word_count
sentence = "hello world hello"
result = count_word()
print(result)