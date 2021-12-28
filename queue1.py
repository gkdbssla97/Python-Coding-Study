#import queue
# command + / = 주석처리

class SomeClass :
    def __init__(self, something): #생성자 첫번째 인자 self 정형
        self.something = something
    
    def some_function1(self): #메소드
        print(self.something)
    
    def some_function2(self): #메소드
        print(self.something)    

a = SomeClass("some_value")
a.some_function1()

# 스택은 리스트 사용가능 pop(), 큐(queue),덱(deque) pop(0)
class ListQueue:
    def __init__(self):
        self.my_list = list()
    def put(self, element):
        self.my_list.append(element)
    def get(self):
        return self.my_list.pop(0)
    def qsize(self):
        return len(self.my_list)

data = ListQueue()
data.put(2)
print(data.get())
print(data.qsize())
    