a = int(input())
b = int(input())
a1 = a
b1 = b
while a1 != 0 and b1 != 0:
    if a1>b1:
        a1 = a1 % b1
    else:
        b1 = b1 % a1
d = a1 + b1
for x in range(-500, 500):
    for y in range(-500, 500):
        if a*x + b*y ==d:
            print(x,y)
print(d)