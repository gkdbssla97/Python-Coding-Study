import random as r

a = []
print(a)
b = list()
print(b)
a = list(range(1,11))
print(a)
r.shuffle(a)
print(a)
#a.sort()
print(a)
a.sort(reverse=True)
print(a)

for x in enumerate(a):
    print(x, end = ' ')
#컴그 강의평좀 보자
if all(9>x for x in a):
    print("yes")
else:
    print("no")
