n = int(input("Enter the limit :"))
list = []
for x in range(n):
    x = int(input("Enter the number :"))
    if x < 100:
        list.append(x)
    else:
        list.append("over")
print(list)
© 2022 GitHub, Inc.
Terms