


import RPi.GPIO as GPIO
import time

#set GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set variables for GPIO pins
pinMotorAForwards = 7
pinMotorABackwards = 11
pinMotorBForwards = 13
pinMotorBBackwards = 15
#Define Gpio pins used
pinTrigger = 17
pinEcho = 18


Frequency = 20

DutyCycleA = 30
DutyCycleB = 30

Stop = 0


GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

#Distance Variables
HowNear = 15.0
ReverseTime = 0.5
TurnTime = 0.75

# Set GPIO software PWM to Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the PWM software w/ a duty cycle = 0
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorABackwards.start(Stop)

# Turn all motors off