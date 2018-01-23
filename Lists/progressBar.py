from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

blocks = [0, 10]
barBlock = 22

count = 0
while count <= len(blocks):

    mc.setBlock(x, y, z, blocks[0])
    mc.setBlock(x, y + 1, z, blocks[1])
    mc.setBlock(x, y + 1, z, blocks[2])
    mc.setBlock(x, y + 1, z, blocks[3])
    mc.setBlock(x, y + 1, z, blocks[4])
    mc.setBlock(x, y + 1, z, blocks[5])
    mc.setBlock(x, y + 1, z, blocks[6])
    mc.setBlock(x, y + 1, z, blocks[7])
    mc.setBlock(x, y + 1, z, blocks[8])
    mc.setBlock(x, y + 1, z, blocks[9])
    mc.setBlock(x, y + 1, z, blocks[10])

    count += 1

    del blocks[10]

    blocks.insert(10, 22)
    
                
