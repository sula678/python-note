class Demo:
    x = 0
     
    def __init__(self, i):
        self.i = i
        Demo.x += 1
     
    def __str__(self):
        return str(self.i)
          
    def hello(self):
        print("hello", self.i)
 
print("There are", Demo.x, "instances.")
a = Demo(1122)
a.hello()
print("a.x =", a.x)
b = Demo(3344)
b.hello()
print("b.x =", b.x)
c = Demo(5566)
c.hello()
print("c.x =", c.x)
d = Demo(7788)
d.hello()
print("d.x =", d.x)
e = Demo(9900)
e.hello()
print("e.x =", e.x)
print("After all, there are", Demo.x, "instances.")
