def even_number_greater_than_10(x):
    if x > 10 and x%2 == 0:
        return True
    else:
        return False
  
numbers = [10,100,3,56,76,33,24,4,2,8,101,102]
a = list(filter(even_number_greater_than_10,numbers))
print(a)
