from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    name = input('What is your name ("exit" to quit): ')
    if name == 'exit':
        break
    mc.postToChat("Go!")

    time.sleep(10)

    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat('Your score is' + ' ' + str(blockHitsLength))

    scoreboard[name] = scoreboard

    for names in scoreboard:
        print(scoreboard)
