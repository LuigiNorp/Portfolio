class Mathematics:

    def tangent(self,angle, n=20):
        x = self.radians(angle)
        tan = 0
        iter = int(n/2)+1


    def cosine(self, angle, n=20):        
        x = self.radians(angle)
        cos = 0
        iter = int(n/2)+1

        for n in range (0,iter):
            cos += ((-1)**(n))*((x**(2*n))/self.factorial(2*n))
        return cos

    def sine(self, angle, n=8):
        x = self.radians(angle)
        iter = int(n/2)+1
        sin = 0

        for n in range (0,iter):
            sin += ((-1)**n)*((x**((2*n)+1))/self.factorial((2*n)+1))
        return sin
    

    def arctan(self, value, n=16):        
        x = value
        arctan = 0
        iter = int(n) + 1

        for n in range(0, iter):
            arctan += ((-1)**n)*(x**((2*n)+1))/((2*n)+1)
            #print(arctan)
        return self.degrees(arctan)

    
    def degrees(self, radians):
        return 180*(radians/3.1415926535897932384626433832795)


    def radians(self, degrees):
        return degrees * 3.1415926535897932384626433832795/180
    

    def factorial(self, num):
        fact = 1
        for n in range(1, num+1):
            fact *= n
        return fact

    




if __name__ == "__main__":
    m = Mathematics()
    #print (m.cosine(5))
    print(m.arctan(1))
    #print(m.sine(5,6))