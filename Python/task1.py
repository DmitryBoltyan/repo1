#Write a function that takes an integer as input, and returns the number of bits that are equal to one in
#the binary representation of that number. You can guarantee that input is non-negative.

#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

input1 = input('Enter the number: ')

int_num = format(int(input1), "b")
print(int_num)
count = 0
for i in range(len(int_num)):
    print(int_num[i])
    if int_num[i] == '1':
        count = count+1

print(count)
