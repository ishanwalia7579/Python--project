              # class check project for codetantra
class Check():
  def __init__(self):
    pass
  def count(self,string,char):
    print(string.count(char))
  def reverse(self,string):
    print(string[::-1])
obj=Check()
print("1.count")
print("2.reverse")
choice=int(input("Select: "))
if choice == 1:
  b=input()
  c=input()
  obj.count(a,b)
elif choice ==2:
  a=input()
else:
  print("Invalid")
  
