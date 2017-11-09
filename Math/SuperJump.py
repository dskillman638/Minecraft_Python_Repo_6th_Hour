from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
x = x + 5
position = mc.player.setTilePos(x, y, z)
