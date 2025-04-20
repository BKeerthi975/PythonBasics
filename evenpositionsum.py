n=int(input('enter number:'))
def example(n):
    s=str(n)   #string has index values so converted to string
    sum=0
    for i in range(len(s)):
        if i%2==0:
            sum=sum+int(s[i])   #s is string so converting into int to add , adding string value not the index
    return sum
print(example(n))