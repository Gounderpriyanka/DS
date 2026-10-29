# 1.Create a Stack class in Python using a list to store elements, and implement push(item) and pop() methods
#  that follow the LIFO principle.

'''class stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

s1 = stack()
s1.push(23)
s1.push(45)
s1.push(55)
s1.push(100)
print(s1.stack)
s1.pop()
print(s1.stack)'''


# 2.Implement a Stack class in Python using a list to store elements. Add push(item), pop(), and is_empty() 
# methods, then demonstrate pushing and popping five numbers.

'''
class stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def isempty(self):
        return len(self.stack) == 0

s1 = stack()
print("check list is full or not:",s1.isempty())
s1.push(12)
s1.push(45)
s1.push(22)
s1.push(85)
s1.push(63)
print(s1.stack)
print("check list is full or not:",s1.isempty())

s1.pop()
s1.pop()
print(s1.stack)'''



# 3.Write a function is_playlist_empty(stack) that checks if a user's Spotify playlist stack is
# empty and returns True or False.


'''stack = []
def is_playlist_empty(stack):
    if len(stack) == 0:
        return True
    return False

print(is_playlist_empty(stack))'''



# 4.Build a browser back button simulation: create a stack to keep track of visited URLs (as strings), 
# and write functions to visit a new page (push URL) and go back (pop URL), printing the current page 
# after each action.





# 5.Simulate the undo feature in WhatsApp chat by using a stack: every sent message is pushed onto the stack,
# and undo pops the last message. Demonstrate this with at least 3 messages.

# 6.Write a function is_valid_parentheses(s) that checks if a string of parentheses '(', ')' is valid 
# (all opened are closed in correct order), similar to how Instagram checks for valid hashtags or 
# mentions in a post.Use a stack to track opening parentheses as you loop through the string.


# 7.Build a function is_valid_parentheses(s) that checks if a string of parentheses is valid
# (like '()', '(()())', but not '(()'). Use a stack to solve this.
# Push opening brackets onto the stack, pop when you see a closing bracket,
# and check if the stack is empty at the end.


def is_valid_parentheses(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(is_valid_parentheses("(())"))  
print(is_valid_parentheses("(()"))   
                              








# 8.Given the following broken code for a stack pop operation:

# stack = [1,2,3]
# def pop_item():
# return stack[len(stack)]

# Fix the bug so that pop_item() returns the last element and removes it from the stack.
#  Check the correct index and method to remove the last item in a Python list.


'''stack = [1,2,3]
def pop_item(stack):
    return stack.pop()
print(stack)
print(pop_item(stack))
print(stack)
'''


# 9.Refactor your Stack class to include a peek() method that returns the top element without removing it, 
# and write a short demo showing how peek() works after several push and pop operations.

'''class stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

s1 = stack()
s1.push(90)
s1.push(80)
s1.push(23)
s1.push(15)
s1.push(63)
print("After push:",s1.stack)
s1.pop()
print("After pop:",s1.stack)
print("Peek:",s1.peek()) # Still 15; peek doesn't remove it'''


