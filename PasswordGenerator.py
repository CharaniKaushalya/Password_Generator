# import modules
import string   #import string: Imports the string module, which contains string-related utilities and constants, like all lowercase and uppercase letters, digits, and punctuation characters.
import random   #import random: Imports the random module, which provides functions for generating random numbers and for shuffling lists.


# store all characters in lists
s1 = list(string.ascii_lowercase)   #s1: A list of all lowercase English letters, retrieved using string.ascii_lowercase. 'abcdefghijklmnopqrstuvwxyz'
s2 = list(string.ascii_uppercase)   #s2: A list of all uppercase English letters, retrieved using string.ascii_uppercase. 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s3 = list(string.digits)            #s3: A list of all digit characters (0-9), retrieved using string.digits. '0123456789'
s4 = list(string.punctuation)       #s4: A list of punctuation characters, like !@#$, etc., retrieved using string.punctuation. '!@#$%^&*()'


# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# check this input is it number? is it more than 8?
while True:

	try:    #try:: Attempts to convert the input to an integer

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break

	except:     #except:: If the conversion to an integer fails (e.g., user entered letters), this block will run.

		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")


# shuffle all lists
# #random.shuffle(s1), etc.: Randomly rearranges the elements in each list (s1, s2, s3, and s4).
# This ensures that the characters used for the password are in a random order
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# The code calculates 30% and 20% of the password length to determine how many characters of each type to include in the final password
#part1: Stores 30% of the total password length. This represents the number of lowercase and uppercase letters that will be used.
part1 = round(characters_number * (30/100))
#part2: Stores 20% of the total password length . This represents the number of digits and punctuation characters that will be used.
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
# Initializes an empty list that will store the selected characters for the password.
result = []

for x in range(part1):  #First for loop:

	result.append(s1[x])        #Adds a lowercase letter (from s1) to the result list.
	result.append(s2[x])        #Adds an uppercase letter (from s2) to the result list.

for x in range(part2):  #Second for loop

	result.append(s3[x])        #Adds a digit (from s3) to the result list.
	result.append(s4[x])        #Adds a punctuation character (from s4) to the result list.


# shuffle result
# Shuffles the characters in the result list to ensure they are in a random order
random.shuffle(result)


# join result
password = "".join(result)              #Joins all characters in the result list into a single string
print("Strong Password: ", password)    # Prints the generated password to the user.



#If the password length is 10, the code will aim to have around:
#3 lowercase letters
#3 uppercase letters
#2 digits
#2 punctuation characters
