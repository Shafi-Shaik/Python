#Variables 
name ='shafi'
age = 99
isMarried = False
gradePoints = 9.12

print(name)
print(age)
print(isMarried)
print(gradePoints)

#type() to identity the datatype of variable
print(type(name))
print(type(age))
print(type(isMarried))
print(type(gradePoints))

#multiplication table from user input
num = int(input("enter the number for which you want multiplication table\n"))
for n in range(1,11):
    print(f" {num} X {n} = {num*n}")



