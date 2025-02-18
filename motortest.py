import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering

# Motor 1 pins (Left motor)
IN1 = 17  # Change this according to your wiring
IN2 = 27  # Change this according to your wiring

# Motor 2 pins (Right motor)
IN3 = 22  # Change this according to your wiring
IN4 = 23  # Change this according to your wiring

# Set up GPIO pins as outputs
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to move robot forward
def move_forward():
    print("Moving forward...")
    
    # Forward for motor 1 (left motor)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    
    # Forward for motor 2 (right motor)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Function to stop the robot
def stop_moving():
    print("Stopping...")
    
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Example of moving the robot forward for 5 seconds
try:
    move_forward()
    time.sleep(5)  # Move forward for 5 seconds
finally:
    stop_moving()
    GPIO.cleanup()  # Clean up GPIO settings
