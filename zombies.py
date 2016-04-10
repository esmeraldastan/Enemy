#Enemies in the game

#HP OF ZOMBIE
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

        
#HP OF INFECTED
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
    

        
zombie = Zombie()
infected = Infected()
