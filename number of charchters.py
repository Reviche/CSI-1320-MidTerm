#Exam-Q5: Write a program to take a sentence as input and count the number of letters in this string, 
# the space between words should not be counted. 
# You need to print the result on the screen.

#Example: 

#Sentence: Hello world

#The number of letters is 10.



# I wrote "Hi there" for input
sentence = input("Write a sentence: ")
words = sentence.split()

joined = "".join(words)
charachters = len(joined)
print(charachters)

#Result was 7
