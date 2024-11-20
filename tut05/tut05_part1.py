nums = []
n=int(input("Number of elements : "))
for i in range(n):
    ele = int(input())
    nums.append(ele)
tuples = ()
l=[]
nums.sort()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                l.append((nums[i], nums[j], nums[k]))

for i in range(len(l)):
  if(l[i] not in tuples):
    tuples+=(l[i],)
print(tuples)
