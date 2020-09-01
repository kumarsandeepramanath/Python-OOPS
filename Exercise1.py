class PlayerCharacter:
  #Class Object Attribute
  membership = True
  def __init__(self,name):
    if(PlayerCharacter.membership):
      self.name = name
      
  @classmethod
  def calculate_sum(cls,num1,num2):
    return num1+num2
  
  def run(self):
    print("run")
    print(f"My name is {PlayerCharacter.membership}")
player1 = PlayerCharacter("Sandeep")
print(player1.run())
print(PlayerCharacter.calculate_sum(5,2))
# print(player1)
    
