import random

class gameChar:
    
    def __init__(self, name, life, health, stamina, strength, shield, age):
        self.name = name
        self.life = life
        self.health = health
        self.stamina = stamina
        self.strength = strength
        self.shield = shield
        self.age = age # max age will be set, can be in labirynth for 65 years
        self.steps = 0 #each steps equals % of years
        self.position = (0,0) #character's position to the world
        
        #initialize list if items a character can have
        #name of item, damage/benefit value, available ammo/weapon
        self.weaponItems = {0: ['dagger', 10, 40], 1: ['sundang', 15, 0],
                            2: ['pistol', 20, 0], 3: ['shotgun', 25, 0],
                            4: ['garlic bomb', 40, 0] }        
        
        self.medicineItems ={0: ['ginger', 5, 5], 1: ['potion', 10, 0],
                            2: ['crystal', 15, 0], 3: ['krus', 20, 0],
                            4: ['holy grail', 30, 0] } 
        
        self.foodItems = {0: ['bananaQ', 10, 5], 1: ['tinapay', 15, 0],
                            2: ['isaw', 20, 0], 3: ['adobo', 25, 0],
                            4: ['lechon', 40, 0] } 
        
        self.shieldItems ={0: ['kaldero', 10, 2], 1: ['kawayan', 15, 0],
                            2: ['planggana', 20, 0], 3: ['metal', 25, 0],
                            4: ['mahika', 40, 0] } 
        
        self.items = [self.weaponItems, self.medicineItems, self.foodItems,
                      self.shieldItems, {'life': self.life}
                      ]
        
    def charAttack(self, weaponDamage = 0):
        
        if weaponDamage>0:
            damage = weaponDamage
        else:    
            damage = random.randint(20,self.strength)//(self.age//4)
        return damage
    
    def addLife(self, plus):
        self.life += plus
        return self.life

    def addHealth(self, plus):
        self.health += plus
        return self.health

    def addStamina(self, plus):
        self.stamina += plus
        return self.stamina 

    def addStrength(self, plus):
        self.strength += plus
        return self.strength

    def addShield(self, plus):
        self.shield += plus
        return self.shield 

    def charItem(self):
        pass        


