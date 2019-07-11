#EXAMPLE OF LIST
numInt = 10
numList = []
i=0

while i < numInt:
    num = int(input("Enter integer: "))
    numList = numList + [num]
    i = i + 1

print(numList)

even = 0
odd = 0
i = 0

while i< numInt:
    if numList[i] % 2 ==0:
             even = even + 1
    else:
            odd = odd + 1
    i = i + 1
print("There are", even, "even numbers in the list")
print("There are", odd, "even numbers in the list")
