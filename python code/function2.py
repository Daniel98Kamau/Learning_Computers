##This function checks if a given nonzero positive number can be expressed
##as (2^x). x is an integer greater than or equal to 0 

def number_expressed_to_base2(n):
    if n == 1:
        return True
    while n > 1:
        if n%2 != 0:
            return False
        else:
            n = n/2
            return number_expressed_to_base2(n)

def power_of_two(num):
    return (num & (num - 1)) == 0

def power_of_two_div(num):
    while num > 1:
        num /= 2
    return num == 1

number = int(input())
print(number_expressed_to_base2(number))

print(power_of_two(number))
print(power_of_two_div(number))

