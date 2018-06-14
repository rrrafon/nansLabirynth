import character, random

class gameEvents:
        
    def __init__(self):
        
        pass
        
    def spawnEnemy(self, name = 'kalaban',life = 1, health = 50, stamina = 30, strength =90, shield = 0, age = 35):
        '''
        this spawns enemy, parameters same as character
        '''
        enemy = character.gameChar(name,life,health,stamina,strength,shield,age)
        return enemy

    def attackChar(self, attacker, defender, wd = 0):
        '''
        this defines attack function, shield will be depleted
        before health, weapon is a multiplier
        wd = weapon damage, if character is using weapon
        '''
        
        damage = attacker.charAttack(wd)
        if defender.health >= 1:
            if defender.shield >= 1:    
                defender.shield -= damage
            else:
                defender.health -= damage
            
            
            print('%s dealt %s damage to %s'%(attacker.name, damage , defender.name ) )    
            print('%s\'s health is %s '%(defender.name, defender.health ) )    
            print('%s\'s shield is %s '%(defender.name, defender.shield ) )    
            
            print('-')*20   
        return defender.shield, defender.health
    
    
    def randomWalkChar(self):
        moveLeft = random.randint(0,1)
        moveRight = random.randint(0, 1)
        moveUp = random.randint(0, 1)
        moveDown = random.randint(0, 1)
        return moveLeft, moveRight, moveUp, moveDown



    def getPosition(self):
        '''
        this will return character's position relative to World
        '''
        pass
    
    
    def winRandomItems(self,user, luckyPick):
        
        '''this script random picks an item from predefined item list'''
        
        if luckyPick == 'food':
            maxNum = 3
            itemWon = user.foodItems[random.randint(0, len(user.foodItems)-1)]
            itemWon[2] += random.randint(1, maxNum)
            
        elif luckyPick == 'medicine':
            maxNum = 4
            itemWon = user.medicineItems[random.randint(0, len(user.medicineItems)-1)]
            itemWon[2] += random.randint(1, maxNum)
                        
        elif luckyPick =='weapon':
            maxNum = 5
            itemWon = user.weaponItems[random.randint(0, len(user.weaponItems)-1)]
            itemWon[2] += random.randint(1, maxNum)
            
        elif luckyPick == 'life':
            if user.life <= 3:
                user.life += 1
                itemWon = ['Life', user.life, 1]
            else:
                itemWon = user.weaponItems[random.randint(0, len(user.weaponItems)-1)]
                itemWon[2] += random.randint(10, 20)
               
        elif luckyPick == 'shield':
            maxNum = 2
            itemWon = user.shieldItems[random.randint(0, len(user.shieldItems)-1)]
            itemWon[2] += random.randint(1, maxNum)
            
        else:
            pass  
        
        return itemWon
        
    def itemLottery(self, user, pick = True, randomItem = ['food', 'medicine','weapon', 'shield','life']):
        
        if pick:
            #choices should be limited to 6 items
            userChoice = input('Choose a number from 1-6: ')
        else:    
            userChoice = random.randint(1,6)

        
        item = [randomItem[0] for i in range(40)]+ [randomItem[1] for i in range(30)]+[randomItem[2] for i in range(12)]+[randomItem[3] for i in range(12)]+[randomItem[3] for i in range(14)]+[randomItem[4] for i in range(6)]
        
        toChoose = [item[random.randint(0, len(item)-1)] for i in range(6)]
        luckyPick = toChoose[userChoice-1]
        itemWon = self.winRandomItems(user, luckyPick)
        
        return 'you won %s %s' % (itemWon[2],itemWon[0] )
    
    
    def normalItemDrop(self, user , pick = False, randomItem = ['food', 'medicine','weapon', 'shield','shield']):
        return self.itemLottery(user,pick, randomItem )
    
    def weaponItemDrop(self, user , pick = False, randomItem = ['weapon', 'weapon','shield', 'shield','shield']):
        return self.itemLottery(user,pick, randomItem )
    
    def medicineItemDrop(self, user , pick = False, randomItem = ['medicine', 'medicine','medicine', 'shield','shield']):
        return self.itemLottery(user,pick , randomItem)
    
    def shieldItemDrop(self, user , pick = False, randomItem = ['shield', 'shield','shield', 'weapon','shield']):
        return self.itemLottery(user,pick , randomItem)
    
charA = character.gameChar('Runan', 1, 100,100, 50, 10, 20)
enemy1 = gameEvents().spawnEnemy('aswang1')
enemy2 = gameEvents().spawnEnemy('aswang2')
enemy3 = gameEvents().spawnEnemy('aswang3')


def addHealthDemo():

    print enemy.health
    enemy.addHealth(20)
    print enemy.health


def battleDemo(attacker, defender):
    
    while defender.health >= 1 or attacker.health >= 1: 
        gameEvents().attackChar(attacker, defender)
        if defender.health <= 0:
            break
        else:
            gameEvents().attackChar( defender, attacker)
            
def raffleDemo(times = 100):
    
    for i in range(times):
        print i, ': ', gameEvents().shieldItemDrop(charA)

print gameEvents().randomWalkChar()


#raffleDemo()
#battleDemo(charA, enemy1)
#battleDemo(charA, enemy2)
#battleDemo(charA, enemy3)
#print charA.health
#print charA.shield
    

