
from stackUsingLL import Stack


s1 = Stack()
s1.push(122)
s1.push(133)
s1.push(144)

while s1.isEmpty() is False:
    print(s1.pop())

s1.top()