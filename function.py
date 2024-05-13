''' Function is a reusable set of instruction created by user ... it can repeat the same 
instruction again and again , and it can take input & it can show output..
'''
# defining a function
def greetings():
    print('Good morning !')
    print('How are you ?')   # now this two lines are not going to printed because the 
                             # function has only defined , now we've to invoke it

greetings() # function has been invoked... now it's going to print 
greetings()

x = int(input('Enter your number : '))
for i in range(x) :   # i is generally use for identation ... we can use '_' instead of i
    greetings()

# As the above code explains the usage of function ...