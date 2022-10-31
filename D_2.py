i = 1
sum = 0
while i <= 15:
    if i == 11:
        break
    print(i)
    sum += i
    i += 1
print(f"Sum is {sum}")

name = "Md Rasel"
for letter in name:
    print(letter)

for n in range(0, 12, 2):
    print(n)

for i in range(13, 40):
    if i % 2 == 1:
        print(i)

num1 = 20
while num1 > 0:
    print(num1)
    num1 -= 1

price = -10
if price:
    print("Yes")
else:
    print("No")
