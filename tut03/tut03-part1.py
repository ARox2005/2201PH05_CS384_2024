num = int(input("Enter a number : "))

prime = True
if num<=1:
    prime = False
elif num<=3:
    prime = True
elif num%2==0 or num%3==0:
    prime = False
else:
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            prime = False
            break
        i+=6

rotprime = True
if not prime:
      rotprime = False
elif prime:
  s = str(num)
  for i in range(1, len(s)):
    rotnum = int(s[i:]+s[:i])
    # prime = True
    if rotnum<=1:
        rotprime = False
    elif rotnum<=3:
        rotprime = True
    elif rotnum%2==0 or rotnum%3==0:
        rotprime = False
    else:
        j = 5
        while j*j<=rotnum:
          if rotnum%j==0 or rotnum%(j+2)==0:
            rotprime = False
            break
          j+=6

if rotprime:
  print(num, "is a rotated prime number")
else:
  print(num, "is not a rotated prime number")
