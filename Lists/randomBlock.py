from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

blocks = [1, 3, 6, 8, 7, 17, 26, 23, 33, 35, 39, 41, 42]

mc.setBlock(x, y ,z, random.choice(blocks))
