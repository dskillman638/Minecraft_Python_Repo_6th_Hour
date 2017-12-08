from mcpi.minecraft import Minecraft
mc = Minecraft.create()
score = 0
userName = input("Please enter your username:")
while score <= 1:
    message = input("Please enter your message:")
    if message == ("exit"):
        score += 2
    else:
        mc.postToChat(message)
