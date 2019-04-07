class Waterjug:


    def __init__(self,am,bm,a,b,g):
        self.a_max = am;
        self.b_max = bm;
        self.a = a;
        self.b = b;
        self.goal = g;


    def fillA(self):
        self.a = self.a_max;
        print ('(', self.a, ',',self.b, ')')


    def fillB(self):
        self.b = self.b_max;
        print ('(', self.a, ',', self.b, ')')


    def emptyA(self):
        self.a = 0;
        print ('(', self.a, ',', self.b, ')')


    def emptyB(self):
        self.b = 0;
        print ('(', self.a, ',', self.b, ')')


    def transferAtoB(self):
        while (True):

            self.a = self.a - 1
            self.b = self.b + 1
            if (self.a == 0 or self.b == self.b_max):
                break
        print ('(', self.a, ',', self.b, ')')


    def main(self):
        while (True):

            if (self.a == self.goal or self.b == self.goal):
                break
            if (self.a == 0):
                self.fillA()
            elif (self.a > 0 and self.b != self.b_max):
                self.transferAtoB()
            elif (self.a > 0 and self.b == self.b_max):
                self.emptyB()



waterjug=Waterjug(5,3,0,0,1);
waterjug.main();
