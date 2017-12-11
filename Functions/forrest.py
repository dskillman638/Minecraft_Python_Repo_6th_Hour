from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    mc.setBlock(x, y, z, 6)
    

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
growTree(x + 2, y, z)
growTree(x + 3, y, z)
growTree(x + 4, y, z)
growTree(x + 5, y, z)
growTree(x + 6, y, z)
growTree(x + 7, y, z)
growTree(x + 8, y, z)
growTree(x + 9, y, z)
