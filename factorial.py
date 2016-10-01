
def Fact(n):
   if( n <= 1):
        return 1
   return n * Fact(n - 1)
 
 
print "Program to find Factorial of a Number"
val = 0
print "Enter a number: ",
val = input()
print val, "! = ", Fact(val)
