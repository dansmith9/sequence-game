from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi.vec3 import Vec3
import time
import random
#import explorerhat

mc = Minecraft.create()

puzRoomStart = Vec3(0,0,0)

puzRoomLength = 12
puzRoomWidth = 12
puzRoomHeight = 8

puzRoomFloorStart = Vec3(2,0,2)
puzRoomFloorEnd = Vec3(puzRoomLength-2,1,puzRoomWidth-2)

print(puzRoomFloorEnd)

blue = Vec3(3,2,4)
yellow = Vec3(5,2,4)
red = Vec3(7,2,4)
green = Vec3(9,2,4)
startPos = Vec3(6,2,10)

difficulty=1
sequence = []
blocklist = [blue,yellow,red,green]

correct = 0
currentBlock = 0

lives = 4

def clear():
    mc.setBlocks(puzRoomStart.x-10, puzRoomStart.y-10, puzRoomStart.z-10,puzRoomStart.x+30, puzRoomStart.y+30, puzRoomStart.z+30,block.AIR)

def setup():
    ##create puzzle room outer TNT skin
    mc.setBlocks(puzRoomStart.x,puzRoomStart.y-20,puzRoomStart.z,puzRoomStart.x+puzRoomLength,puzRoomStart.y+puzRoomHeight,puzRoomStart.z+puzRoomWidth,block.TNT,1)
    ##patterned inner layer of wall
    pattern=[block.WOOL,block.WOOL,block.WOOL.id,11,block.WOOL,block.WOOL.id,4,block.WOOL,block.WOOL.id,14,block.WOOL,block.WOOL.id,13,block.WOOL,block.WOOL]
    pattern=[0,0,11,0,4,0,14,0,13,0,0]
    for i in range(0,len(pattern)):
        mc.setBlocks(puzRoomStart.x+i+1,puzRoomStart.y+1,puzRoomStart.z+1,puzRoomStart.x+i+1,puzRoomStart.y+puzRoomHeight,puzRoomStart.z+puzRoomWidth-1,block.WOOL.id,pattern[i])


    ##make centre of room hollow
    mc.setBlocks(puzRoomStart.x+2,puzRoomStart.y+2,puzRoomStart.z+2,puzRoomStart.x+puzRoomLength-2,puzRoomStart.y+puzRoomHeight,puzRoomStart.z+puzRoomWidth-2,block.AIR)

    ## make pit hollow
    mc.setBlocks(puzRoomStart.x+2,puzRoomStart.y-1,puzRoomStart.z+2,puzRoomStart.x+puzRoomLength-2,puzRoomStart.y-19,puzRoomStart.z+puzRoomWidth-2,block.AIR)

    ##make lava pit
    mc.setBlocks(puzRoomStart.x,puzRoomStart.y-19,puzRoomStart.z,puzRoomStart.x+puzRoomLength,puzRoomStart.y-19,puzRoomStart.z+puzRoomWidth,block.LAVA)
    
    ##make glass roof
    mc.setBlocks(puzRoomStart.x,puzRoomStart.y+puzRoomHeight,puzRoomStart.z,puzRoomStart.x+puzRoomLength,puzRoomStart.y+puzRoomHeight,puzRoomStart.z+puzRoomWidth,block.GLASS)
    
    ##place coloured wool blocks
    mc.setBlock(blue,block.WOOL.id,11)
    mc.setBlock(yellow,block.WOOL.id,4)
    mc.setBlock(red,block.WOOL.id,14)
    mc.setBlock(green,block.WOOL.id,13)
    ##place player
    mc.player.setPos(startPos)
    time.sleep(2)
    mc.setBlock(blue,block.WOOL.id,15)
    mc.setBlock(yellow,block.WOOL.id,15)
    mc.setBlock(red,block.WOOL.id,15)
    mc.setBlock(green,block.WOOL.id,15)

    mc.player.setPos(startPos)

def createSequence():
    for i in range(0,difficulty):
        sequence.append(blocklist[random.randint(0,len(blocklist)-1)])
    print("CS Seq:",sequence)

def showSequence():
    for i in sequence:
        if i == blue:
            mc.setBlock(i,block.WOOL.id,11)
        elif i == yellow:
            mc.setBlock(i,block.WOOL.id,4)
        elif i == red:
            mc.setBlock(i,block.WOOL.id,14)
        elif i == green:
            mc.setBlock(i,block.WOOL.id,13)
        time.sleep(1)
        mc.setBlock(blue,block.WOOL.id,15)
        mc.setBlock(yellow,block.WOOL.id,15)
        mc.setBlock(red,block.WOOL.id,15)
        mc.setBlock(green,block.WOOL.id,15)
        time.sleep(1)

##def hint(channel,event):
##    if sequence[currentBlock] == blue:
##        explorerhat.light.blue.on()
##        time.sleep(1)
##        explorerhat.light.blue.off()
##    elif sequence[currentBlock] == yellow:
##        explorerhat.light.yellow.on()
##        time.sleep(1)
##        explorerhat.light.yellow.off()
##    elif sequence[currentBlock] == red:
##        explorerhat.light.red.on()
##        time.sleep(1)
##        explorerhat.light.red.off()
##    elif sequence[currentBlock] == green:
##        explorerhat.light.green.on()
##        time.sleep(1)
##        explorerhat.light.green.off()

clear()
setup()

while True:

    mc.postToChat("Please wait...")

    time.sleep(5)
    
    lives=4
    difficulty=1
    sequence=[]

    mc.postToChat("Lives: "+str(lives))
    
    createSequence()
    print(sequence)

    mc.postToChat("Watch the sequence!")

    time.sleep(5)

    showSequence()

    #mc.postToChat("Press 1 on the Explorer for a hint!")

    #explorerhat.touch.one.pressed(hint)

    while lives!=0:
            
        for event in mc.events.pollBlockHits():
            print("Event pos:",event.pos)
            print("Next sequence:",sequence[currentBlock])
            if (event.pos.x == blue.x and event.pos.y == blue.y and event.pos.z == blue.z) or (event.pos.x == yellow.x and event.pos.y == yellow.y and event.pos.z == yellow.z) or (event.pos.x == red.x and event.pos.y == red.y and event.pos.z == red.z) or (event.pos.x == green.x and event.pos.y == green.y and event.pos.z == green.z):
                if event.pos.x == sequence[currentBlock].x and event.pos.y == sequence[currentBlock].y and event.pos.z == sequence[currentBlock].z:
                    mc.setBlock(event.pos,block.GOLD_BLOCK)
                    time.sleep(1)
                    mc.setBlock(event.pos,block.WOOL.id,15)
                    currentBlock += 1
                else:
                    mc.setBlocks(puzRoomFloorStart,puzRoomFloorEnd,block.AIR)
                    mc.postToChat("That is wrong, you muppet!")
                    lives-=1
                    mc.postToChat("Lives left: "+str(lives))
                    time.sleep(3)
                    print("Current block",currentBlock)
                    currentBlock=0
                    print("Current block",currentBlock)
                    setup()
                    mc.setBlock(startPos.x, startPos.y, startPos.z,block.WATER_STATIONARY)
                    time.sleep(0.5)
                    mc.setBlock(startPos.x, startPos.y, startPos.z,block.AIR)

        if currentBlock == len(sequence):
            correct = 1
            mc.postToChat("That is correct! Well done you legend!")
            mc.postToChat("Now lets make it harder...")
            currentBlock=0
            difficulty+=1
            sequence = []
            clear()
            setup()
            createSequence()
            print(sequence)

            mc.postToChat("Watch the sequence!")

            time.sleep(5)

            showSequence()

                

