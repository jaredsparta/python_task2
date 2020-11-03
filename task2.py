# This runs through the range 0-9 and prints out hello
for num in range(10):
    print("hello")

# Initiates an empty list
# The while loop fills the list with names
list_names = []
while True:
    answer = input("List a name, otherwise type stop: ").title()
    if answer == "Stop":
        break
    list_names.append(answer)
print("\nThe names inputted were:", list_names)

# Creates another list to store the names in lowercase
# The for loop iterates over all the names and adds the lowercase version into the new list
list_names_lower = []
for names in list_names:
    list_names_lower.append(names.lower())
print("The names in lowercase are:", list_names_lower)    
    
# This list should hold all names that are even-numbered
# The for loop checks all the names, if their length is even then it will add it to the list  
r_list = []   
for name in list_names_lower:
    if len(name) % 2 == 0:
        r_list.append(name)
    else:
        continue
print("The names of even length were:", r_list)