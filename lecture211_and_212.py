#make a function 'divide'
def divide(a,b):
    try:
        return (a/b)
    except ZeroDivisionError as er:    
        print(divide(4,2))#2

        
print(divide(4,0))# please dont devide by zero (0)..!
print(divide('4',2))#please input numbers only
