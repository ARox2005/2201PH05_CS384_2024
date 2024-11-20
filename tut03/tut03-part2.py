s = input("Enter a string : ")

n = len(s)

p = s

c = [0]*n
i=0

for i in range(0, n):
  for j in range(i, n):
    t = p[j:]+p[:j]
    print(t)
