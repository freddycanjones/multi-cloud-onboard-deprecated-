from random import randint, choice
from string import ascii_lowercase
#my_dict = {'py': 'python', 'rb':'ruby', 'js':'javascript'}

#for key, value in my_dict.items(): # just when the the iterator returns tuples
    #print(f"key is {key}, value is {value}")

#l1= [randint(1,100) for num in range(1000)]

#l1 = [choice(ascii_lowercase) for num in range(100)]

#i = 0
#num_to_search = 25
#Don't use while loops when you ussualy know when the loops will stop
#while i < len(l1):
    #if l1[i] == num_to_search:
        #print(f"{num_to_search} found at index {i}")
        #break
    #i +=1

#Enumerate function is used when you want to create tuple with index and value in an iterator
#for index, num in enumerate(l1):
    #if num == num_to_search:
        #print(f"{num_to_search} found at index {index}")
        #break

#This a better use of while loops, because the user will determine when a program will be stopped
#while True: 
    #print("Please choose one option")
    #print("Press 1 for selection 1")
    #print("Press 2 for selection 2")
    #print("Press 3 for quit")
    #selection = input("Enter your choice ->")
    #if int(selection) == 3:
        #break

#Using zip function to create list of tuples       
l1 = ['.py', '.js', '.rb', '.java', '.c']
l2 = ['python', 'javascript', 'ruby', 'java', 'c']

tupled_list = list(zip(l2,l1))
print(tupled_list)