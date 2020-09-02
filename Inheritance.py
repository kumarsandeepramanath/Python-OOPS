# print("Starting Inheritance")

class User:
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with a power of {self.power}')

class Archer(User):
    def __init__(self,name,number_of_arrows):
        self.name = name
        self.number_of_arrows = number_of_arrows
    
    def attack(self):
        print(f'Attacking with arrows : arrows-left: {self.number_of_arrows}')


wizard1 = Wizard('Merlin','50')
archer1 = Archer('Robin','500')
# print(wizard1.attack())
# print(archer1.attack())

def player_attack(char):
    char.attack()

print(player_attack(wizard1))
print(player_attack(archer1))
