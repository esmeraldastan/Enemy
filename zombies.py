#MAIN BOSS 
class Zombie(object):
    def __init__(self, health = 5000, attack = 2000):
        self.health = health
        self.attack = attack
         
    #COMMAND TO ATTACK     
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
         #DAMAGE TAKEN   
    def damage(self, amount):
        self.health -= amount
        
#LOWER THEN BOSS           
class Infected(object):
    def __init__(self, health = 5000, attack = 500):
        self.health  = health 
        self.attack = attack 
        
    #COMMAND ATTACK 
    def attacks(self, target):
        target.damage(self. attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
            
    #DAMAGE TAKEN         
    def damage(self, amount):
        self.health -= amount 
    
class Player(object):
    def __init__(self, health = 8000, attack = 50):
        self.health = health 
        self.attack = attack 
        
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy Down!!"
        else:
            return target.health
            
    def damage(self, amount):
        self.health -= amount
        
zombie = Zombie()
infected = Infected()
me = Player()