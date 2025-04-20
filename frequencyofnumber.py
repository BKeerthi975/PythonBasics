nums=[1,7,2,3,2,1,8,4,3,8,8]
'''count=0
for n in nums:
    if n==nums(i):
        n+=1
        print(nums[i]':'n)'''

d={}
for n in nums:
    if n not in d.keys():
        d[n]=1
    else:
        d[n]+=1
for k,v in d.items():
    print(k,':',v)

