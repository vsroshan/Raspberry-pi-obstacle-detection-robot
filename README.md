Raspberry pi obstacle detection robot

This project demonstrates how to build an obstacle-avoiding robot using a Raspberry Pi and an ultrasonic sensor (HC-SR04). The robot detects obstacles in its path and changes direction autonomously using simple logic programmed in Python.

Features

	•	Obstacle Detection: Measures distance using an HC-SR04 ultrasonic sensor and avoids obstacles based on pre-defined thresholds.
	•	Motor Control: Uses an L298N motor driver to control two DC motors for forward, backward, and turning movements.
	•	Simple Wiring: Includes an easy-to-follow wiring diagram for seamless assembly.


How It Works

	1.	The ultrasonic sensor continuously measures the distance to obstacles in front of the robot.
	2.	If an obstacle is detected within a set threshold distance (e.g., 15 cm), the robot stops, moves backward briefly, and turns to avoid the obstacle.
	3.	If no obstacles are detected, the robot continues to move forward.

Getting Started

Prerequisites

	•	Install Raspbian OS on your Raspberry Pi.
	•	Install the required Python libraries:

pip install RPi.GPIO



Setup

	1.	Connect the components as per the wiring diagram provided in this repository.
	2.	Copy the Python script to your Raspberry Pi.
	3.	Run the script using:

robot.py


Bill of Materials in INR


Raspberry Pi	1,	Raspberry Pi 4 or Raspberry Pi Zero W with GPIO support.	
Micro SD Card (16GB or higher)For Raspberry Pi OS.
HC-SR04 Ultrasonic Sensor	1 For obstacle distance measurement.
L298N Motor Driver To control the motors.
DC Motors (6V) For robot movement (gear motors recommended).
Wheels Attach to the DC motors.
Caster Wheel For stability and balance.
Battery Pack (6-12V) Power the motors (e.g., AA battery holder or Li-ion pack).
Connecting Wires	1 Set 	For connections (male-to-female, male-to-male).


Pin Diagram (Without Servo):

Raspberry Pi GPIO	Component
5V	VCC Pin of HC-SR04
GPIO 5	Trigger Pin of HC-SR04
GPIO 6	Echo Pin of HC-SR04
Ground (GND)	GND Pin of HC-SR04
GPIO 8	Left Motor IN1
GPIO 9	Left Motor IN2
GPIO 10	Right Motor IN1
GPIO 11	Right Motor IN2

Powering the Motors and Ultrasonic Sensor:

	1.	5V for Ultrasonic Sensor (HC-SR04):
	•	Connect the VCC pin of the ultrasonic sensor to the Raspberry Pi’s 5V pin.
	•	Connect the GND pin of the ultrasonic sensor to one of the Raspberry Pi’s GND pins.
	2.	Motor Driver Power:
	•	Connect the positive (+) terminal of an external battery to the motor driver’s VCC.
	•	Connect the negative (-) terminal of the battery to the motor driver’s GND.
	•	Connect the motor driver’s GND to the Raspberry Pi’s GND pin to establish a common ground between the battery and the Pi.

This setup will allow the ultrasonic sensor to detect obstacles, and the motor driver will control the motors based on the sensor data. Make sure the motors’ battery voltage is appropriate for the motor driver you’re using.


Code Explanation

	1.	Motor Control Functions: move_forward, move_backward, turn_right, turn_left, and stop control the motors based on the GPIO output.
	2.	Ultrasonic Sensor: measure_distance triggers the ultrasonic sensor and calculates the distance in centimeters.
	3.	Main Loop:
	•	Measures distance using the ultrasonic sensor.
	•	If an obstacle is detected within the threshold (OBSTACLE_THRESHOLD), the robot stops, moves backward briefly, and then turns to the right or left depending on the distances measured on both sides.
	•	If no obstacle is detected, the robot moves forward.

Important Notes:

	•	Be sure to share a common ground between the motor power source and the Raspberry Pi for proper functionality.
	•	Adjust the OBSTACLE_THRESHOLD variable if you want to detect obstacles at a different distance.

License

This project is licensed under the MIT License.

Contributions

Contributions are welcome! Feel free to fork this repository and create pull requests to improve the project.

