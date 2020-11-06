def is_palomdrom(x):
    '''take string in varibale x
    :param :x string
    '''
    if x == x[::-1]:
        return True
    else:
        return False


if is_palomdrom(input("enter string: ")):
    print("string palomdron")
else:
    print("not palomdron")          