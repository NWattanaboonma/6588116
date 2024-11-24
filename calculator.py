class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # if(b>a):
        # i want that number can be negative 
            # return b - a
            # i like a-b
            return a - b
        # else:
        #     return a - b

    def multiply(self,a, b):
        result = 0
        if(a<0 and b<0):
            a = self.subtract(0,a)
            b = self.subtract(0,b)
            if(a>b):
                for i in range(b):
                    result = self.add(result,a)
            else:
                for i in range(a):
                    result = self.add(result,b)
            return result
        if(a>b):
            if(b<0):
                for i in range(a):
                    result = self.add(result,b)
                return result
            else:
                for i in range(b):
                    result = self.add(result,a)
                return result
        else:
            if(a<0):
                for i in range(b):
                    result = self.add(result,a)
                return result
            else:
                for i in range(a):
                    result = self.add(result,b)
                return result

    def divide(self, a, b):  
        result = 0
        if(b == a):
            return 1
        elif(b < 0 and a < 0):
            a = self.subtract(0,a)
            b = self.subtract(0,b)
        if(a<b):
            if(a<0):
                k=a
                while k < b:
                    k = self.add(k, b)
                    result += 1
                    if(k==0):
                        break
            else:
                return result
        else:
            if(b<0):
                while a >=0:
                    k=b
                    if(k<0):
                        k = self.subtract(0,k)
                        a = self.subtract(a, k)
                        if(a<0):
                            break
                        result += 1
            else:
                while a >= b:
                        a = self.subtract(a, b)
                        result += 1

        if (b < 0 or a < 0):
            result = self.subtract(0, result)
        return result
    
    def modulo(self, a, b):
        if(a>b):
            while a >= b:
                a = self.subtract(a,b)
            return a
        elif(a==b):
            return 0
        else:
            return a

        

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(1000, -3))
    print("Example: modulo: ", calc.modulo(10, 3))