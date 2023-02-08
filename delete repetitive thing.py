tol_list = int(input("enter tol list: "))
new_list = []

for i in range(tol_list):
    new_list.append(input("enter a thing: "))

print(new_list)
new_list = list(dict.fromkeys(new_list))
print(new_list)
