from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def placeBlock(x, y, z):
    pos = mc.player.getPos()
    x = pos.x
    y = pos.z
    z = pos.z
    mc.setBlock(x, y, z)
    time.sleep(10)

placeBlock(x, y - 1, z, 103)
placeBlock(x + 5, y, z, 103)
placeBlock(x, y - 1, z + 4, 103)
placeBlock(x + 3, y - 1, z, 103)
placeBlock(x + 2, y - 1, z - 2, 103)
placeBlock(x, y - 1, z + 3, 103)
