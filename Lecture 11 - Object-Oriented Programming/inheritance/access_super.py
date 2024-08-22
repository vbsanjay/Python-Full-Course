# class Base(object): 
  
#     # Constructor 
#     def __init__(self, x): 
#         self.x = x     
  
# class Derived(Base): 
  
#     # Constructor 
#     def __init__(self, x, y): 
#         Base.x = x  
#         self.y = y 
  
#     def printXY(self): 
       
#        # print(self.x, self.y) will also work 
#        print(self.x, self.y)
#        print(id(Base.x))
#        print(id(self.x))
  
  
# # Driver Code 
# d = Derived(10, 20) 
# d.printXY() 


class Base(object): 
  
    # Constructor 
    def __init__(self, x): 
        self.x = x     
  
class Derived(Base): 
  
    # Constructor 
    def __init__(self, x, y): 
        super().__init__(x) 
        self.y = y 
  
    def printXY(self): 
       # print(self.x, self.y) will also work 
       print(self.x, self.y)
       print(id(self.x))
       print(id(self.x))
  
  
# Driver Code 
d = Derived(10, 20) 
d.printXY() 