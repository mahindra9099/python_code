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