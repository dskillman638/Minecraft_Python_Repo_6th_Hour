from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = [0, 50]
increment = 0

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for item in range(50):
    if mc.getBlock(x, y, z) == 56:
        mc.postToChat("A diamond ore is" + " " + str(pos.y - y) + " blocks below you.")
        break
    else: y -= 1
        
else:
    print("There are no diamonds below you")
