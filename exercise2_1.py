class GetterSetter():
 def __init__(self,parameter):
    self.parameter = parameter

 @property
 def parameter(self):
    return self.parameter

 @parameter.setter
 def parameter(self,value):
    self.parameter = value

obj = GetterSetter(1)
