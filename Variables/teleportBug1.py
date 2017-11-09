from mcpi.minecraft import Minecraft


import time


mc = Minecraft.create()

x = 10.0
y = 110.0
z = -12.0

mc.player.setTilePos(x, y, z)
