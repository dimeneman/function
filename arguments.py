''' functions can also accept one or more values as inputs (also known as arguments or 
parameters). Arguments help us write flexible functions which can perform the same
opearation on different values.
'''

# taking arguments on function

def say_hello(name):
    print("hello {}".format(name))

say_hello('Eman')   # invoking
say_hello('Sumana')

# another example ( a little bit complex but good to go)

def filter_even(number_list):   
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    return result_list

even_list = filter_even([2,4,8,9,3,10])
print(even_list)