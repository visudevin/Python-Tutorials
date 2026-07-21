#faulty calculator
print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print("/,*,+,- : ?")
num3 = input()

if num1==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=="+":
    print("77")
elif num1==56 and num2==6 and num3=="/":
    print("4")
elif num3=='-':
    sub=num2-num1
    print(sub)
else:
    print("Out Of the range:")