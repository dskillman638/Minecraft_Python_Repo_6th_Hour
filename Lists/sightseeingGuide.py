from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {'Beach': (-20.0, 1.0, -9.0), 'Forest': (0.0, 11.0, 6.0), 'Snow': (-46.0, 4.0, 98.0)}

choice = ""

while choice != 'exit':
    choice = input('Enter a location("exit" to close): ')
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
