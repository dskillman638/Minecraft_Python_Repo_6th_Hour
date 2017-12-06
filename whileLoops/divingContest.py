from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

while score <= 6:
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    if blockAbove == 9 or blockAbove == 8:
        score = score + 1
        mc.postToChat("Current Score: " + str(score))

mc.postToChat("Final Score: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                     finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
