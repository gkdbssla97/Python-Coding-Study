class ListStack:
    def __init__(self):
        self.my_list = list()
    def push(self, data):
        self.my_list.append(data)
    def pop(self):
        return self.my_list.pop()

data = ListStack()
data.push(1)
data.push(2)
print(data.pop())
print(data.pop())