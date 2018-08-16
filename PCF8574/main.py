
#sudo ampy --port /dev/ttyUSB0 --baud 115200 put main.py main.py
#sudo screen /dev/ttyUSB0 115200

import pcf8574
from machine import Pin, I2C

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c.scan()

pcf1 = pcf8574.PCF8574(i2c, 32)
pcf2 = pcf8574.PCF8574(i2c, 33)

#Hepsini söndürelim...
pcf1.set()
pcf2.set()

#Hepsini YAK...
pcf1.clear()
pcf2.clear()

#Yakalım....
pcf1.write(3, 0)
pcf2.write(5, 0)


#Söndürelim....
pcf1.write(1, 1)
pcf2.write(1, 1)


ledMavi    = 2
ledYesil   = 4
ledKirmizi = 16

Led1 = Pin(ledMavi,    Pin.OUT)
#Led2 = Pin(ledYesil,   Pin.OUT)
Led3 = Pin(ledKirmizi, Pin.OUT)


Led1.off() # Aç
#Led2.off() # Aç
Led3.off() # Aç


Led1.on()  # Kapat
#Led2.on()  # Kapat
Led3.on()  # Kapat




'''
def HAREKETVAR():
	print('Buton basıldı!!!')

p6 = Pin(6, Pin.IN)
p6.irq(trigger=Pin.IRQ_FALLING, handler=HAREKETVAR)
'''

