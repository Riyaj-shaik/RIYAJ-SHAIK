class Calculator:
    def __init__(self,a,b,operator):
        self.a=a
        self.b=b
        self.operator=operator
    def result(self):
        if(self.operator=='+'):
            return self.a + self.b
        elif(self.operator=='-'):
            return self.a - self.b
        elif(self.operator=='*'):
            return self.a * self.b
        elif(self.operator=='/'):
            if(self.b != 0):
                return self.a / self.b
            else:
                return "Cannot divide with zero"
        else:
            return "Enter a valid operator"    
a=float(input())
b=float(input())
operator=input() 
obj = Calculator(a,b,operator)
print(obj.result())