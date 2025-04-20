'''exceptional handling(EH):the error which are occured during run time is know as exception.to handle those exception we can use EH
 3 types of errors: 1.complile time error(syntax error) 2.run time error 3.logical error 
 key word used is TRY,ELSE,EXCEPT,FINALLY'''
try:
    a=10
    b=0
    print(a/b)
except Exception: #if u know error type give that or else give Exception
    print('divide by zero not possible')

else:
    print('there is no exception in my code')
    