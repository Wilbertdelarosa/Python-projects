#Search phone list
#Given: A list of phone numbers, a list of names, a phone number to search for
#Find: Name associated with the phone number

# Get the lists
nameList = []
phoneList = []

listSize = int(input("How many phone numbers are there? " ))

for i in range(listSize):
         name = input("Enter name: ")
         Phone = input("Enter phone number")
         nameList.append(name)
         phoneList.append(Phone)

# Get phone number to seach for
searchPhone = input("Enter phone number to search for: ")

# Loop through phoneList looking for searchPhone
i = 0
found = false
while i< listSize and found == false:
    # Is this the phone number im looking for
    if searchPhone == phoneList[i]:
        print(nameList[i])
        found = True

if found == false:
    print("number not found")
        
    
    i + i + 1
                     
