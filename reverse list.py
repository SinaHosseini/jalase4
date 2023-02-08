tol_list = int(input("enter tol list: "))
list = []

for i in range(tol_list):
    list.append(input("enter a thing: "))

print(list)
list.reverse()
print(list)
