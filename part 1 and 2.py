#Exam-Q3: Write a program to create a Python dictionary (the dictionary data type). 

#1) Add two entries to the dictionary: Associate the key ‘Exam’ with the value ‘Python’, and 
# associate the key ‘Day’ with ‘Tuesday’. 
# You need to print the final elements in your dictionary on the display.

#2) Search for the key 'room' in your dictionary and return None if it is not exist.#

#part 1
dictionary = {}
dictionary["Exam"] = "Python"
dictionary["Day"] = "Tuesday"
print(dictionary)

#part 2
print(dictionary.get("room" , None))
