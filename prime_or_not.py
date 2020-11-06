def prime(a):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                print("not prime number")
                break
        else:
            print("prime number")
    else:
        print("not prime number")


print(prime(int(input("Enter any number :"))))
