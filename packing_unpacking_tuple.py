# packing the tuple
# if we are giving values with comma seperation it will be packing the tuple

packed_tuple = 1,"Pravin",9975050292
print(packed_tuple)
print(type(packed_tuple))


## unpacking the tuple

id,name,phone = packed_tuple
print(f"id is {id}")
print(f"name is {name}")
print(f"phone number is {phone}")


## unpacking with *
numbers = (1,2,3,4,5,6,7,8,9)
first,*middle,second_last,last = numbers
print(first)
print(middle)
print(second_last)
print(last)