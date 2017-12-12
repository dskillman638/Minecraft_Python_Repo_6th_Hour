from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def placeBlock(x, y, z):
    mc.setBlock(x, y, z, 103)
    time.sleep(10)
    
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

placeBlock(x, y - 1, z)
placeBlock(x + 5, y, z)
placeBlock(x, y - 1, z + 4)
placeBlock(x + 3, y - 1, z)
placeBlock(x + 2, y - 1, z)
placeBlock(x, y - 1, z + 3)
