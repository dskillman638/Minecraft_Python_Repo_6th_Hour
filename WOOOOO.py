Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> print("Woooooo Minecraft")
Woooooo Minecraft
>>> print("Adventure")
Adventure
>>> from mcpi.m1necraft import Minecraft
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    from mcpi.m1necraft import Minecraft
ImportError: No module named 'mcpi.m1necraft'
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mc = Minecraft.create()
  File "/usr/lib/python3/dist-packages/mcpi/minecraft.py", line 171, in create
    return Minecraft(Connection(address, port))
  File "/usr/lib/python3/dist-packages/mcpi/connection.py", line 17, in __init__
    self.socket.connect((address, port))
ConnectionRefusedError: [Errno 111] Connection refused
>>> mc = Minecraft.create()
>>> mc.player.setTilePos(0, 120, 0)
>>> pickaxes = 12
>>> bread = 145
>>> 
>>> bread
145
>>> pickaxes = 12
>>> iron = 30
>>> cobblestone = 25
>>> cobblestone iron
SyntaxError: invalid syntax
>>> 
>>> cobblestone
25
>>> cats = 5
>>> cats
5
>>> cats = 10
>>> cats
10
>>> pigs = 5
>>> tempertaure = -5
>>> temperature = -5
>>> 
