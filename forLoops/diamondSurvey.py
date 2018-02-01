from mcpi.minecraft import Minecraft
mc = Minecraft.create()

blocks = [1, 3, 7, 56]

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for diamond in blocks(50):
    if blocks == 56:
        mc.postToChat("A diamond ore is" + blocks and pos.y + " below you.")
        break
    else: y - 1
        
else:
    print("There are no diamonds below you")
