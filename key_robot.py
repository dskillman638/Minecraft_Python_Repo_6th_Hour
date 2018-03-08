import curses
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            GPIO.output(7,False)
            GPIO.output(8,True)
            GPIO.output(9,False)
            GPIO.output(10,True)
        elif char == curses.KEY_DOWN:
            GPIO.output(7,True)
            GPIO.output(8,False)
            GPIO.output(9,True)
            GPIO.output(10,False)
        elif char == curses.KEY_LEFT:
            GPIO.output(7,True)
            GPIO.output(8,False)
            GPIO.output(9,False)
            GPIO.output(10,True)
        elif char == curses.KEY_RIGHT:
            GPIO.output(7,False)
            GPIO.output(8,True)
            GPIO.output(9,True)
            GPIO.output(10,False)
        elif char == 10:
            GPIO.output(7,False)
            GPIO.output(8,False)
            GPIO.output(9,False)
            GPIO.output(10,False)
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
