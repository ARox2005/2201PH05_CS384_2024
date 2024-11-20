s = input()
l = []
i = -1
j=0
while j<len(s):
  if(i==-1):
    l.append(s[j])
    i+=1
  # elif(len(l)>0):
  elif(l[i]=='(' and s[j]==')'):
    l.pop(i)
    i-=1
  elif(l[i]=='{' and s[j]=='}'):
    l.pop(i)
    i-=1
  elif(l[i]=='[' and s[j]==']'):
    l.pop(i)
    i-=1
  else:
    l.append(s[j])
    i+=1
  j+=1
if(len(l)==0):
  print("Balanced")
else:
  print("Unbalanced")
