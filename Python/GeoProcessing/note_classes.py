# Simple class definition with attributes and constructor:
class Simple:                   # obj = Simple(7) 
    x = None                    # obj.x == 7
    def __init__(self, x):
        self.x = x
        
# Subclass which accesses a method of its Superclass
class XY(Simple):               # obj = XY(7, 9)
    y = None                    # obj.x == 7
    def __init__(self, x, y):   # obj.y == 9
        super().__init__(x)
        self.y = y
        
# Class with a method that can be called on instances:
class CalcZ(XY):                # obj = CalcZ(7, 9)
    def do_z(self):             # obj.do_z() == 63
        return self.x * self.y
    
# Class with an automatically computed attribue:
class AutoZ(XY):                # obj = AutoZ(7, 9)
    @property                   # obj.z == 63
    def z(self):
        return self.x * self.y