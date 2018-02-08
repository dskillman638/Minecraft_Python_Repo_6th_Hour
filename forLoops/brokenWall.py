from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []

for wall in range(10):
    brokenWall.append([])
    for inner in range(10):
        brokenWall[wall].append(brokenBlock())
print(brokenWall)

for row in brokenWall:
    for blocks in row:
       mc.setBlock(x, y, z, blocks)
       x += 1
    y += 1
    x = pos.x
