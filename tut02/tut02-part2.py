s = input("Enter a string : ")
l = len(s)
s2 = ""
l2 = len(s2)
for i in range(0, l):
  count = 0
  for r in range(0, l2):
    if s[i] == s2[r]:
      count += 1
  if(count == 0):
    count = 0
    for j in range(0,l):
      if s[i] == s[j]:
        count += 1
    s2 = s2+s[i]+str(count)
    l2 = len(s2)
print(s2)
