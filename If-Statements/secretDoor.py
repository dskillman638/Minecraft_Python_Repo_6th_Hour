from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = 0
y = 11
z = 23
x2 = pos.x
y2 = pos.y
z2 = pos.z
blockType1 = 0
blockType2 = 10
gift = mc.getBlock(-0.3, 11.0, 22.6)
if gift != 0:
    if gift == 57:
        mc.setBlocks(0, 11, 23, 0, 11 - 1, 23, blockType1)
    elif gift != 57:
        mc.setBlock(x2, y2, z2, blockType2)
else:
    mc.postToChat("Place an offering on the pedestal.")
