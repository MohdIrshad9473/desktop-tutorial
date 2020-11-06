def febonic(a):
    # last ke do chahhie to calculate
    x = 0
    y = 0
    series = []
    for i in range(a):
        if i == 0 or i == 1:
            y = i      
       
        x, y = y, x
        y = x + y
        series.append(y)

    return series

i = int(input("enter any number"))
print(febonic(i))