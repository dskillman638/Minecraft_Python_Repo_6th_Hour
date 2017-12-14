from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def getWoolState(color):
    if color == "pink":
        blockstate = 6
    elif color == "white":
        blockstate = 0
    elif color == "orange":
        blockstate = 1
    elif color == "magenta":
        blockstate = 2
    elif color == "light blue":
        blockstate = 3
    elif color == "yellow":
        blockstate = 4
    elif color == "lime":
        blockstate = 5
    elif color == "gray":
        blockstate = 7
    elif color == "light gray":
        blockstate = 8
    elif color == "cyan":
        blockstate = 9
    elif color == "purple":
        blockstate = 10
    elif color == "blue":
        blockstate = 11
    elif color == "brown":
        blockstate = 12
    elif color == "green":
        blockstate = 13
    elif color == "red":
        blockstate = 14
    elif color == "black":
        blockstate = 15
    else:
        blockstate = 16
    return blockstate
        
colorString = input("Enter A Block Color: ")
state = getWoolState(colorString)
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)