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

#product of no
def table(x):
   count=1
   product=1
   # x=int(input())
   while count<=10:
      product=count*x
      print(x,"*",count,"=", product)
      count=count+1

#LCM
def LCM(x,y):
   while(True):
      a=max(x,y)
      if a%x==0 and a%y==0:
         print("LCM= ",a)
      else:
         a=a+1
      break

#Print sterik
def sterik(x):
   k=1
   for i in range(0,x):
      for j in range(0,i+1):
         print("*", end="")
      print()

# for i in range(int(input())):
#         a=[]
#         b=[]
#         name = input()
#         score = float(input())
#         a.append(name)
#         b.append(score)
#         c=[]
#         c.append(a)
#         c.append(b)
#         print(c)
def addition(num):
   integer=0
   check=0
   sum=0
   while(check<num):
      sum+sum+check
      check=check+1
   print(sum)

# swap 
def swap_case(s):
    a=""
    for i in s:
        if i.isupper():
           a+= i.lower()
        else:
           a+= i.upper()
    return(a)

# assign value in string
def mutate_string(s, i, c):
    lis=list(s)
    lis[i]=c
    s = ''.join(lis)
    return(s)
      

if __name__=="__main__":
   # LCM(2,6)
   sterik(5)

