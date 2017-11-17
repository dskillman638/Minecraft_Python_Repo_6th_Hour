from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = 38.7
buildY = 12.0
buildZ = 24.7
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width, buildY < y < buildY + height, buildZ < z < buildZ + length
mc.postToChat("The Player Is At Home: " + str(inside = True))