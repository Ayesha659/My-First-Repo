# Find even number
def even_num(x):
   if x%2==0:
      print(x,"is an even number") 
   else:
      print(x,"is an odd number")
   return x

# Find average 
def average(x,y):
   z=(x/y)%2
   return (z)

#Fictorial
def factorial(x):
   for i in range(x):
      fact=0
      fact=fact*i
   return fact

