students = ["ali", "bilal", "ayan", "asad"]

print(len(students))
print(students[0]) 
print(students[-1]) 
# print(students[4]



letters = ["a", "b", "c", "d"]

print(letters[2:])   
print(letters[:2])     


my_data = ["ali", 20, "ali@gmail.com"]

my_data[0:2] = ["ibrahim", "khan"] 

# Adding elements
my_data.append(30)             
my_data.insert(2, "danish")    


list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]

list1.extend(list2) 
print(list1)  
