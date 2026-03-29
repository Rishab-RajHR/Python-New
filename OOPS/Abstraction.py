# Encapsulation is about bundling data and methods together inside a class, and restricting direct access to internal state. 

class Vehicle:
    def __init__(self):
        self.engine = False
        self.brk = False
    
    def start_engine(self):
        self.engine = True
        self.brk = True
        print("Engine started.")

car1 = Vehicle()
car1.start_engine()