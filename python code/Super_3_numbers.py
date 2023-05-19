#A super -3 number is a number which when cubed and then multiplied by 3, the product has three 3's in succession
import string
Super3_numbers = []
for i in range(1000):
    check = i**3 * 3
    check = str(check)
    if '333' in check:
        Super3_numbers.append(i)

print(Super3_numbers)