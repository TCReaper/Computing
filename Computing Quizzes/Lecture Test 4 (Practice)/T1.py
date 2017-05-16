

#Q1 Practical Lecture Test4

#Implement parent class IntegerBase10
#Child classes IB8, IB2, IB16 that inherits from IB10

class IntegerBase10():
      #this_is_a_comment

      def data_to_base(self,base):
            if self.__class__ == IntegerBase10:
                  output = ""
                  value = self._data
                  while value > 0:
                        add = value % base #gives corresponding changed base value from the back
                        if add > 9:
                              add -= 10
                              hexalist = ['a','b','c','d','e','f']
                              add = hexalist[add]
                        value = value // base
                        output = str(add) + output
                  return output

            
            if self.__class__ == IntegerBase2:
                  self._data = int(str(self._data),2)
            elif self.__class__ == IntegerBase8:
                  self._data = int(str(self._data),8)
            elif self.__class__ == IntegerBase16:
                  self._data = int(str(self._data),16)
            return self.data_to_base(base)



      def __init__(self,data):
            self._data = data
            #encapsulation
            if self.__class__ == IntegerBase2:
                  self._data = self.data_to_base(2)
            elif self.__class__ == IntegerBase8:
                  self._data = self.data_to_base(8)
            elif self.__class__ == IntegerBase16:
                  self._data = self.data_to_base(16)

      
            
class IntegerBase8(IntegerBase10):
      pass
class IntegerBase16(IntegerBase10):
      pass
class IntegerBase2(IntegerBase10):
      pass
            



#
