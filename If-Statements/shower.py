from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 44
shwrY = 2 
shwrZ = 44

width = 1
height = 5
length = 1

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
    print("BROKE NERD")
else:
     mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 0)
     print("ALL GOOD!")
