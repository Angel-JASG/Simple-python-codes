
print("Introduce le numero: ")
num = int(input())

primo = True

for i in range(2,num):
    
    if num % i == 0:
        primo = False
        break


if primo == True:
    print(num," es un numero primo")
else:
    print(num," no es un numero primo")