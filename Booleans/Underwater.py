from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y + 1, z)
blockType2 = blockType == 9
mc.postToChat("The player is underwater: " + str(blockType2))
