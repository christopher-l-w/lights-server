#
#   Lights server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"OFF" / b"ON" from client, replies with current state of light via b"OFF" / b"ON"
#

from gpiozero import LED
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

light = LED(17)
current_state = "OFF"
light.off()

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    if message == b"ON":
        print("Turning lights ON")
        current_state = "ON"
        light.on()
    elif message == b"OFF":
        print("Turning lights OFF")
        current_state = "OFF"
        light.off()
    else:
        print("Invalid request: %s" % message)
        continue

    #  Send reply back to client
    socket.send(current_state.encode())
