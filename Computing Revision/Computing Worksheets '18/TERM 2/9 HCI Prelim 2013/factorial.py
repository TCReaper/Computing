

def Factorial(n):
      if n == 1:
            return 1
      elif n == 0:
            return 1
      else:
            return n * Factorial(n-1)

print(Factorial(0))
print(Factorial(50))

def Factorial2(n):
      output = 1
      while n>0:
            output = output * n
            n -= 1
      return output

print(Factorial2(1000))
