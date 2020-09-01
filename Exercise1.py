class PlayerCharacter:
  def __init__(self,name):
    self.name = name
  
  def run(self):
    print("run")
player1 = PlayerCharacter("Sandeep")
print(player1.run())
    
