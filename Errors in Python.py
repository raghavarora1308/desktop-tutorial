a = 5
b = 0

try : 
    print(a/b)
except Exception as e:
    print("Hey, you can not divide a number by Zero",e)

    k = int(input("Enter a number"))
    print(k)
try:
    print("Resource Open")
    print(a/b)


except Exception as e:
    print("Hey, you can not divide a number by Zero",e)

finally:
    print("resource closed")
