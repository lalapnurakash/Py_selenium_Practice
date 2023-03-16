from abc import ABCMeta,abstractstaticmethod

class Irecords(metaclass=ABCMeta):
    @abstractstaticmethod
    def record_method():
        print("abtract method")
        """ interface method"""
#p1=Irecords()
#p1.record_method()

class student(Irecords):
    def __int__(self):
        self.name="student name"
    # def record_method(self):
    #   print("student record")
s=student()
s.record_method()
