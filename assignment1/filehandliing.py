
file_path = "/Users/suraj/programming/python/class/classPython/assignment1/answers.txt"



# delete file

# import os
# os.remove(file_path)


# open file

# f = open(file_path, "r")
# print(f.read())


with open(file_path,'r') as f:
    print(f.read(),end=" ")
    
userInput=str(input("Enter the text : "))

with open( file_path,'w') as file:
     file.write(userInput)

    
    



# write in that file

# w =  open (file_path,"w")
# w.write(" I am don \n")



# userInput=str(input("Enter the text : "))

# with open( file_path,'w') as file:
#      file.write(userInput)


# append at last

w =  open (file_path,"a")
w.write("Hello \n")
w.write("Ok")



with open(file_path,'r') as f:
    print(f.read(),end=" ")
    
    
    
