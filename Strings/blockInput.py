from mcpi.minecraft import Minecraft
mc = Minecraft.create()
try:
    blockType = int(input("Enter a Block Type: "))
    mc.setBlock(x, y, z, blockType)
except:
    mc.postToChat("You did enter a number.")
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
