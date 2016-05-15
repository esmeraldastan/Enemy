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

#use for zombie 
while me.health > 0:
    command = raw_input('>')
    if command == "stab":# use of dagger
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", dagger.stab(zombie),"damage."
    elif command == "attack":# basic attack
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", me.attacks(zombie),"damage."
    elif command == "shoot":#use of cross bow
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", cross_bow.shoot(zombie),"damage."     
    elif command == "cut off":#use of sword
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", sword.cut_off(zombie),"damage."
    elif command == "slaughter":#use of axe
        me.health -= zombie.attack 
        print "Your health is now", me.health 
        print "You attacked your enemy for", axe.slaughter(zombie),"damage."

        
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
   
#use for infected 
'''while me.health > 0:
    command = raw_input('>')
    if command == "stab":# use of dagger
        me.health -= infected.attack  
        print "Your health is now", me.health 
        print "You attacked your enemy for", dagger.stab(zombie),"damage."
    elif command == "attack":# basic attack
        me.health -= infected.attack  
        print "Your health is now", me.health 
        print "You attacked your enemy for", me.attacks(zombie),"damage."
    elif command == "shoot":#use of cross bow
        me.health -= infected.attack  
        print "Your health is now", me.health 
        print "You attacked your enemy for", cross_bow.shoot(zombie),"damage."     
    elif command == "cut off":#use of sword
        me.health -= infected.attack  
        print "Your health is now", me.health 
        print "You attacked your enemy for", sword.cut_off(zombie),"damage."
    elif command == "slaughter":#use of axe
        me.health -= infected.attack  
        print "Your health is now", me.health 
        print "You attacked your enemy for", axe.slaughter(zombie),"damage."
    
        
    if infected.health <=0:
        print
        print
        print "Great you have diffeted the zombie"
        
        break
        
    print 
    
    if me.health <= 0:
        
        print "sorry you died"
        '''


