#micro:bit (remote)
radio.set_group(241)

#--dragster system deplacement--

#menu_speed
'''def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

#menu_brake
def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B , on_button_pressed_b)
'''
#received string message
def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)
'''
#Brake system 
def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB , on_button_pressed_ab)'''

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)



