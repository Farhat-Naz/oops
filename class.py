class Complex:
    def  __init__(self,real,imaginary):
       
       self.real=real
       self.imaginary=imaginary

    def showNumbers(self):
         print(self.real,"i+" ,self.imaginary, "j")

    def  __addNumbers__(self, num2):  #dunder function
        self.real=self.real + num2.real
        self.imaginary=self.imaginary + num2.imaginary
        return Complex(self.real, self.imaginary)     

num1 = Complex(2,4) 
num1.showNumbers()
num2 = Complex(3,6)
num2.showNumbers()

result = num1+ num2
result.showNumbers()
