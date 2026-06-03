l = int(input("enter teh length"))
b = int(input("enter the breadth"))
if (l<0 or b<0):
    exit("length or breadth cannot be negative")
else:
    print("area is :",l*b)
    print("parameter is :",2*(l+b))
    
