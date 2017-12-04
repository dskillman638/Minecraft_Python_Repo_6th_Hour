from mcpi.minecraft import Minecraft
mc = Minecraft.create()
message = input("Please enter your username")
mc.postToChat(message)
