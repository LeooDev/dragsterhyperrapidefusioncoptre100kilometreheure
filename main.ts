// micro:bit (remote)
radio.setGroup(241)
// --dragster system deplacement--
// menu_speed
/** def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

#menu_brake
def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B , on_button_pressed_b)

 */
// received string message
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
/** 
#Brake system 
def on_button_pressed_ab():
    radio.send_number(0)
input.on_button_pressed(Button.AB , on_button_pressed_ab)
 */
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(2)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(3)
})
