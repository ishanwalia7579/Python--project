                  # Class and object define in python
class Student: 
  def __init__(self,name,marks,address): # name,marks,address
    self.name= name  #name
    self.marks= marks #marks
    self.address = address #address
    
s1=Student("Kotlin",100,"village ...etc")
print(s1.name,s1.marks,s1.address) #s1

s2=Student("Python",99,"Mandi...etc")
print(s2.name,s2.marks,s2.address) #s2

s3=Student("Javascript",99.5,"Delhi")
print(s3.name,s3.marks,s3.address) #s3


