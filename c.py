class Doctor:
    def __init__(self,name,specilization):
        self.name=name
        self.specilization=specilization
    def doSurgery(self):
      print(self.name,'is mainataing the surgery')
d1=Doctor('Priya','cordilogiest')
d2=Doctor('sneha','ent')
d3=Doctor('ramu','neurologist')
d1.doSurgery()
d2.doSurgery()
d3.doSurgery()
