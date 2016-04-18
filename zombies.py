#Enemies in the game
#print "attack"

#command = raw_input('>')




#HP OF ZOMBIE
class Zombie(object):
    def __init__(self, health = 5000, attack = 15000):
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
        
zombie = Zombie()


#player status 
class player(object):
    
    def __init__(self, health = 50000, attack = 500):
        self.attack = attack 
        self.health = health 
        
        
    def attacks(self, target):
        target.damage(self.attack)
        if target.health <= 0:
            return "Enemy down!"
        else:
            return target.health
            
    def damage(self, amount):
        self.health -= amount
        
me = player()        


        
                
                                
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
