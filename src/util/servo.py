import flask
import RPi.GPIO as GPIO
import time

# Setup app
app = flask.Flask(__name__)

# Setup servo
servoPort = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPort, GPIO.OUT)
servo1 = GPIO.PWM(servoPort, 50)  # Pin 11, 50Hz

servo1.start(0)

currentAngle = 90  # Set the starting angle
rotationAmount = 15  # How much to rotate camera per request


def SetAngle(angle):  # Function to rotate servo to angle specified in parameter
    print(angle)
    duty = angle / 18 + 2  # Convert angle to what servo understands
    GPIO.output(servoPort, True)
    servo1.ChangeDutyCycle(duty)  # Rotate servo to angle
    time.sleep(1)
    GPIO.output(servoPort, False)
    servo1.ChangeDutyCycle(0)


@app.route('/right', methods=['GET'])  # Rotate towards right
def right():
    print('right')
    global currentAngle
    # Angle can't go under 0
    if currentAngle > 0:
        currentAngle -= rotationAmount
        print(currentAngle)
        SetAngle(currentAngle)
    return "<h1>RIGHT</p>"


@app.route('/left', methods=['GET'])  # Rotate towards left
def left():
    global currentAngle
    print('left')
    # My servo would spaz out if it went over 180
    if currentAngle < 180 - rotationAmount:
        currentAngle += rotationAmount
        print(currentAngle)
        SetAngle(currentAngle)
    # It would also spaz at 180, 179 is highest it goes
    elif currentAngle == (180 - rotationAmount):
        currentAngle = 180
        print(currentAngle)
        SetAngle(179)
    return "<h1>LEFT</p>"


# Set default angle at 90 when server started
SetAngle(currentAngle)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
