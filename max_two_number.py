def max_number(a, b):
    '''maximum number of given two varible
    :param :a int
    :param :b int
    '''
    if a > b:
        return a
    else:
        return b


z = max_number(int(input("Enter first number")), int(input("Enter first number")))
print("maiximum number is:", z)
