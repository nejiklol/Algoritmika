class CicleBuff(object):
    
    def __init__(self,Max):
        if type(Max).__name__=='int':
            self.Max = Max
            self.Array = [];
        pass

    def add(self,x):
        if type(x).__name__=='int':
            if len(self.Array)==self.Max:
                self.Array[self.Max-1]=0
                i = self.Max
                i = i - 1
                while i != 0:
                    self.Array[i] = self.Array[i-1]
                    i = i - 1
                self.Array[0] = x
                
            else:
                self.Array.insert(len(self.Array),x)
        else:
            print('need Int')
        pass

    def get(self):
        print(self.Array[self.Max-1])
        self.Array=self.Array[:-1]
        pass

    def print(self):
        print(self.Array)
        pass


if __name__ == "__main__":
    Buffer = CicleBuff(5)
    print(Buffer.Max)
    
    i = 10
    while i != 0:
        Buffer.add(i)
        i = i - 1

    Buffer.print()
    Buffer.get()
