from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def water():
    return 9
def wool():
    return 35
def lava():
    return 11
def tnt():
    return 46
def flower():
    return 38
def diamond():
    return 57
def melon():
    return 103

pos = mc.player.getTilePos()

block = flower()
mc.setBlock(pos.x, pos.y, pos.z, block)
