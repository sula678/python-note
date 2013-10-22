def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]
         
for i in reverse("wonderful"):
    print(i * 33)

print
def t(data):
    for i in data:
        if i in "aeiou":
            yield 1
        if i not in "aeiou":
            yield 0
 
s = "perpetual"
d = []
         
for i in t(s):
    d.append(i)
    print(d)
