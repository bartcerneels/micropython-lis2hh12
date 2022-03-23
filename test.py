
# test script for LIS2DH12
from machine import SoftI2C, Pin, Timer
from lis2hh12 import LIS2HH12, SF_G

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

i2c.scan()

sensor = LIS2HH12(i2c, address=0x18, sf=SF_G)

def read_sensor(timer):
    print(sensor.acceleration)

print("LIS2DH12 id: " + hex(sensor.whoami))

sensor.enable_act_int()

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)
