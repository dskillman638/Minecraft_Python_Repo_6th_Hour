from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 6
y = 5
z = 28
blockType = 103



y = y + 1

mc.setBlock(x, y, z, blockType)
