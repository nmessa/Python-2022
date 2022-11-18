from machine import Pin, Timer

def blink(timer):
    led.toggle()

led = Pin(25, Pin.OUT)
timer = Timer()
timer.init(freq=20, mode=Timer.PERIODIC, callback=blink)