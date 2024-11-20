n = input("Enter a number : ")
l=len(n)
while(l>1):
  a = 0
  for i in range(0, l):
    a=a+int(n[i])
  n = str(a)
  l = len(n)
print(n)
