#import sys

#Enemies in the game
print "attack"

#HP OF ZOMBIE
class Zombie(object):
    def __init__(self, health = 5000, attack = 1500):
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

life = me.health

while me.health > 0:
    #i += 1
    command = raw_input('>')
    if command == "attack":
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", me.attacks(zombie),"damage."
        

        
    if zombie.health <= 0:
        print
        print
        print "Great, you have defeated the zombie"
        
        break
        
    print #i
    
    if me.health <= 0:
        
        print "Sorry, you died."
        break
        
    

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
        
infected = Infected() 
   
while me.health > 0:
   
    if command == "attack":
        me.health -= infected.attack 
        print "Your health is now", me.health
        print "You attacked your enemy for", me.attacks(infected),"damage."
        
        
    if infected.health <=0:
        print
        print
        print "Great you have diffeted the zombie"
        
        break
        
    print 
    
    if me.health <= 0:
        
        print "sorry you died"
        
zombie = Zombie()

