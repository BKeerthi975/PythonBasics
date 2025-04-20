name=input('enter name:')
def countVowels(name):
    count=0
    for c in name:
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            count+=1
    return count
print('The count is:',countVowels(name))


'''number=int(input('enter number:'))
def check(number):
    if number>0: 
        return positive
    elif number<0:
        return negative
    else:
        return zero
print(check(number))'''
    