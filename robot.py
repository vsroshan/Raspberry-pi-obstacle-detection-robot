import RPi.GPIO as GPIO
import time

# Pin definitions
MLa = 8  # Left Motor IN1
MLb = 9  # Left Motor IN2
MRa = 10 # Right Motor IN1
MRb = 11 # Right Motor IN2
TRIG_PIN = 5
ECHO_PIN = 6
SERVO_PIN = 7
MAX_DISTANCE = 200  # Maximum distance in cm

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(MLa, GPIO.OUT)
GPIO.setup(MLb, GPIO.OUT)
GPIO.setup(MRa, GPIO.OUT)
GPIO.setup(MRb, GPIO.OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM for servo motor
servo.start(7.5)  # Start with servo in center position

# Function to get distance from HC-SR04 sensor
def read_ping():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Distance in cm
    if distance == 0:
        distance = 250  # Out of range default
    return distance

# Motor control functions
def move_forward():
    GPIO.output(MLa, True)
    GPIO.output(MLb, False)
    GPIO.output(MRa, True)
    GPIO.output(MRb, False)

def move_backward():
    GPIO.output(MLa, False)
    GPIO.output(MLb, True)
    GPIO.output(MRa, False)
    GPIO.output(MRb, True)

def move_stop():
    GPIO.output(MLa, False)
    GPIO.output(MLb, False)
    GPIO.output(MRa, False)
    GPIO.output(MRb, False)

def turn_right():
    GPIO.output(MLa, True)
    GPIO.output(MLb, False)
    GPIO.output(MRa, False)
    GPIO.output(MRb, True)

def turn_left():
    GPIO.output(MLa, False)
    GPIO.output(MLb, True)
    GPIO.output(MRa, True)
    GPIO.output(MRb, False)

# Servo control functions
def look_right():
    servo.ChangeDutyCycle(5)  # Turn servo to the right
    time.sleep(0.4)
    distance = read_ping()
    time.sleep(0.1)
    servo.ChangeDutyCycle(7.5)  # Return servo to center
    return distance

def look_left():
    servo.ChangeDutyCycle(10)  # Turn servo to the left
    time.sleep(0.4)
    distance = read_ping()
    time.sleep(0.1)
    servo.ChangeDutyCycle(7.5)  # Return servo to center
    return distance

# Main loop
try:
    while True:
        distance = read_ping()
        print(f"Distance: {distance} cm")
        time.sleep(0.1)

        if distance <= 15:
            move_stop()
            time.sleep(0.3)
            move_backward()
            time.sleep(0.2)
            move_stop()
            time.sleep(0.3)

            dist_right = look_right()
            time.sleep(0.3)
            dist_left = look_left()
            time.sleep(0.3)

            if dist_right >= dist_left:
                turn_right()
                time.sleep(0.1)
            else:
                turn_left()
                time.sleep(0.1)
            move_stop()
        else:
            move_forward()

except KeyboardInterrupt:
    pass

# Cleanup GPIO settings
finally:
    move_stop()
    servo.stop()
    GPIO.cleanup()
