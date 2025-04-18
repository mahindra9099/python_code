numbers=[1,1,2,3,4,5,2,4,5,9,9,9,9,9,9,9,9,0,0]
# use a dictionary to count the frequency of each number

num_frequency = {number:numbers.count(number) for number in numbers }

print(num_frequency)