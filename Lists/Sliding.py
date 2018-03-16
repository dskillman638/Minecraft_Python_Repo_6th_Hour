from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time
import random

position = mc.player.getTilePos

x, y, z = 10, 11, 12

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
