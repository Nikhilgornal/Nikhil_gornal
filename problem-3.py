a = int(input("Enter a number: "))
if a % 2 == 0:
    limit = a - 1
else:
    limit = a

result = []
for i in range(limit):
    result.append(2 * i + 1)

print(*result, sep=", ")
