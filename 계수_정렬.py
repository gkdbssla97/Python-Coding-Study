#
# Created by 하윤 on 2022/06/20.
#

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
print(count)
