# list
arr = []
# 대괄호
arr.append(30)
arr.append(20)
arr.append(10)

print(arr)
print(1 in arr)
for i, num in enumerate(arr):
    print(i, num)

# hash set
s = set()
# 중괄호 
s.add(10)
s.add(20)
s.add(30)

s.remove(20)
print(s)

print(10 in s)
print(40 in s)

m = dict()
m['a'] = 100
m['b'] = 200

print(m)
print(m.get('a')) # value 출력
print('a' in m) # key값 확인

for num in m.values():
    print(num)
for num in m.items():
    print(num)    
