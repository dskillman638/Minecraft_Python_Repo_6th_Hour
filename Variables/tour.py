from mcpi.minecraft import Minecraft


import time


mc = Minecraft.create()

x = 16
y = 110
z = 19

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 4
y = 100
z = 80


mc.player.setTilePos(x, y, z)

