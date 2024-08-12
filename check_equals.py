# Fix the Error: Value vs. Reference Types
# Create a function that returns True if two lists contain identical values, and False otherwise.

# To solve this question, your friend writes the following code:

# def check_equals(lst1, lst2):
#     if lst1 is lst2:
#         return True
#     else:
#         return False
# But testing the code, you see that something is not quite right. Running the code yields the following results:

# check_equals([1, 2], [1, 3]) ➞ False
# # Good so far...

# check_equals([1, 2], [1, 2]) ➞ False
# # Yikes! What happened?


# Rewrite your friend's code so that it correctly checks if two lists are equal. 
# To be equal, the lists must have the same elements in the same order. 
# The tests below should pass:

# Examples
# check_equals([1, 2], [1, 3]) ➞ False

# check_equals([1, 2], [1, 2]) ➞ True

# check_equals([4, 5, 6], [4, 5, 6]) ➞ True



# Fix this broken code!
def check_equals(lst1, lst2):
	if lst1 is lst2:
		return True
	else:
		return False
print(check_equals([1, 2], [1, 2]))


# The issue with the code provided is that it uses the is operator to compare lst1 and lst2. The is operator checks if two references point to the same object in memory, not if they have the same content.

# To compare the contents of two lists, you should use the == operator, which checks for value equality, meaning it will compare the elements of the lists rather than their memory addresses.

def check_equals(lst1, lst2):
    return lst1 == lst2

print(check_equals([1, 2], [1, 3])) 
print(check_equals([1, 2], [1, 3]))  # Output: False
print(check_equals([1, 2], [1, 2]))  # Output: True
