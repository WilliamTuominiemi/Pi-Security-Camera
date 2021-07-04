import flask
import RPi.GPIO as GPIO
import time

# Setup app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Setup servo
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50)  # Pin 11, 50Hz

servo1.start(0)


def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11, False)
    servo1.ChangeDutyCycle(0)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/right', methods=['GET'])
def right():
    print('right')
    SetAngle(30)
    # GPIO.cleanup()
    return "<h1>RIGHT</p>"


@app.route('/left', methods=['GET'])
def left():
    print('left')
    SetAngle(130)
    # GPIO.cleanup()
    return "<h1>LEFT</p>"


app.run()
