'''
문자열과 내장함수
'''

msg = "It is Time"

print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)
print(msg[-3:-1])
for i in range(len(msg)):
    print(msg[i], end ='')
print()
for x in msg:
    if x.isupper():
        print(x, end = '')
print()
tmp = 'AZ'
for x in tmp:
    print(ord(x))

