#
#   Lights server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"OFF" / b"ON" from client, replies with current state of light via b"OFF" / b"ON"
#

from gpiozero import LED
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5555")

light = LED(17)
current_state = "OFF"
light.off()

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print("Received request: %s" % message)

    if message == "ON":
        print("Turning lights ON")
        current_state = "ON"
        light.on()
    elif message == "OFF":
        print("Turning lights OFF")
        current_state = "OFF"
        light.off()
    else:
        print("Invalid request: %s" % message)
        continue

