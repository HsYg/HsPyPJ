x = -123
x_r =""
x_str = str(x)
length = len(x_str)

for i in range(len(x_str)):
    print( "index:" , i)
    print( x_str[length-1-i])
    x_r = x_r+ x_str[length-1-i]
    
print (int(x_r))
		
		
