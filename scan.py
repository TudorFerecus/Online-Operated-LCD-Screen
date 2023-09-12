import machine
import constants

sda = machine.Pin(constants.I2C_SDA_PIN)
scl = machine.Pin(constants.I2C_SCL_PIN)

i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())