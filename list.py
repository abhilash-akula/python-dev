lst=[]
j = 2
for i in range (2,100,2):
  lst.append(i)
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

A = "Python Programming Language"
B = "Best In The World"
C = A.index("gram")
print(C)
