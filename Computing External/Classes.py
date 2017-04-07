

class a():
        def __init__(self):
                self._myA = 1

        def getA(self):
                print(self._myA)

        def setA(self,n):
                self._myA = n

class c():
        def __init__(self):
                self._myC = 3

        def getC(self):
                print(self._myC)

        def setC(self,n):
                self._myC = n

class b(a,c):
        def __init__(self):
                super().__init__()
                self._myB = 2

        def getB(self):
                print(self._myB)

        def setB(self,n):
                self._myB = n



# call to super( parent , x ) -->  excludes "parent" class
