# lambda function

addition= lambda a,b: a+b

print(addition(4,5))

# map functions
# map functions takes 2 argument 1 is method and another one is iterable object like list tuple set

in_list= [2,3,4,5,6,7,8,9,10]
print(in_list)

# using lamda function
lambda_list=list(map(lambda x: x**2,in_list))

# using normal function

def square(inp):
    return inp**2

normal_list=list(map(square,in_list))

print(lambda_list)
print(normal_list)