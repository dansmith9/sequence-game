from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi.vec3 import Vec3
import time
import random
#import explorerhat

mc = Minecraft.create()

puzzleRoomStart = Vec3(0,35,0)
boardstart = Vec3(0,35,0)
boardend = Vec3(8,35,8)
blue = Vec3(7,36,1)
yellow = Vec3(7,36,3)
red = Vec3(7,36,5)
green = Vec3(7,36,7)
startPos = Vec3(4,36,4)

difficulty=1
sequence = []
blocklist = [blue,yellow,red,green]

correct = 0
currentBlock = 0

def clear():
    mc.setBlocks(boardstart.x-10, boardstart.y-10, boardstart.z-10,boardend.x+10, boardend.y+10, boardend.z+10,block.AIR)


def setup():
    mc.setBlocks(boardstart.x, boardstart.y, boardstart.z,boardend.x, boardend.y, boardend.z,block.DIAMOND_BLOCK)
    mc.setBlocks(boardstart.x, boardstart.y-1, boardstart.z,boardend.x, boardend.y-20, boardend.z,block.AIR)
    mc.setBlocks(boardstart.x, boardstart.y-20, boardstart.z,boardend.x, boardend.y-20, boardend.z,block.LAVA_FLOWING)
    mc.setBlock(blue,block.WOOL.id,11)
    mc.setBlock(yellow,block.WOOL.id,4)
    mc.setBlock(red,block.WOOL.id,14)
    mc.setBlock(green,block.WOOL.id,13)
    mc.player.setPos(startPos)
    time.sleep(2)
    mc.setBlock(blue,block.WOOL.id,15)
    mc.setBlock(yellow,block.WOOL.id,15)
    mc.setBlock(red,block.WOOL.id,15)
    mc.setBlock(green,block.WOOL.id,15)

def createSequence():
    for i in range(0,difficulty):
        sequence.append(blocklist[random.randint(0,len(blocklist)-1)])

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

while True:
    clear()
    setup()
    createSequence()
    print("current block:",currentBlock)
    print(sequence)
    print("Next sequence:",sequence[currentBlock])

    mc.postToChat("Watch the sequence!")

    time.sleep(5)

    showSequence()

    
    #mc.postToChat("Press 1 on the Explorer for a hint!")

    #explorerhat.touch.one.pressed(hint)

    while correct == 0:
        for event in mc.events.pollBlockHits():
            print("Event pos:",event.pos)
            print("Next sequence:",sequence[currentBlock])
            if event.pos.x == sequence[currentBlock].x and event.pos.y == sequence[currentBlock].y and event.pos.z == sequence[currentBlock].z:
                mc.setBlock(event.pos,block.GOLD_BLOCK)
                time.sleep(1)
                mc.setBlock(event.pos,block.WOOL.id,15)
                currentBlock += 1
                print(currentBlock)
            else:
                mc.setBlocks(boardstart,boardend,block.AIR)
                mc.postToChat("That is wrong, you muppet!")
                time.sleep(3)
                currentBlock=0
                setup()
                mc.setBlock(startPos.x, startPos.y, startPos.z,block.WATER_STATIONARY)
                time.sleep(0.5)
                mc.setBlock(startPos.x, startPos.y, startPos.z,block.AIR)
        if currentBlock == len(sequence):
            correct = 1
                
    mc.postToChat("That is correct! Well done you legend!")
    mc.postToChat("Now lets make it harder...")
    correct=0
    currentBlock=0
    difficulty+=1
    sequence = []

print(sequence)
