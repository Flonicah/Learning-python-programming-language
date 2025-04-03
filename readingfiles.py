#readding files from external file outside the python etc php ot html file to get info or pass
# using python read command

open("employees.txt","r")# this is read mode
'''open("employees.txt","w") # this is the write mode
open("employees.txt","a") # append mode where u just add to the existing info
open("employees.txt","r+")# power to read and write'''

employee_file = open("employees.txt","r")
#print(employee_file.readable()) # checksif it is readable

print(employee_file.read()) # print out all the content found in the file

print(employee_file.readlines()) # reads individual line from the file

 



#using the for loop

for employee in employee_file.readlines():
    print(employee)

employee_file.close()    
