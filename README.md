# ESP8266 ve MicroPython

## ESPlorer Programını Çalıştırma
    java -jar ESPlorer.jar C

## ESP8266 için Dosya Yönetimi Yardımcıları
## Utility to interact with a MicroPython board over a serial connection
		https://github.com/dhylands/rshell
		https://github.com/adafruit/ampy
		https://github.com/wendlers/mpfshell



## ampy Örnek Komutları
    sudo ampy --port /dev/ttyUSB0 --baud 115200 ls
    sudo ampy --port /dev/ttyUSB0 --baud 115200 put main.py main.py
    sudo ampy --port /dev/ttyUSB0 --baud 115200 rm  main.py

## ampy Yardım Ekranı
    ampy
    Usage: ampy [OPTIONS] COMMAND [ARGS]...

      ampy - Adafruit MicroPython Tool

      Ampy is a tool to control MicroPython boards over a serial connection.
      Using ampy you can manipulate files on the board's internal filesystem and
      even run scripts.

    Options:
      -p, --port PORT    Name of serial port for connected board.  Can optionally
                         specify with AMPY_PORT environemnt variable.  [required]
      -b, --baud BAUD    Baud rate for the serial connection (default 115200).
                         Can optionally specify with AMPY_BAUD environment
                         variable.
      -d, --delay DELAY  Delay in seconds before entering RAW MODE (default 0).
                         Can optionally specify with AMPY_DELAY environment
                         variable.
      --version          Show the version and exit.
      --help             Show this message and exit.

    Commands:
      get    Retrieve a file from the board.
      ls     List contents of a directory on the board.
      mkdir  Create a directory on the board.
      put    Put a file or folder and its contents on the...
      reset  Perform soft reset/reboot of the board.
      rm     Remove a file from the board.
      rmdir  Forcefully remove a folder and all its...
      run    Run a script and print its output.

## Bağlı I2C Aygıtlarının Listelenmesi
    from machine import Pin, I2C
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    i2c.scan()

## i2c Kullanımı Örnek Kodları
    from machine import Pin, I2C
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

    i2c.readfrom(0x3a, 4)   # read 4 bytes from slave device with address 0x3a
    i2c.writeto(0x3a, '12') # write '12' to slave device with address 0x3a

    buf = bytearray(10)     # create a buffer with 10 bytes
    i2c.writeto(0x3a, buf)  # write the given buffer to the slave

    i2c = I2C(freq=400000) # create I2C peripheral at frequency of 400kHz
                           # depending on the port, extra parameters may be required
                           # to select the peripheral and/or pins to use

    i2c.scan()             # scan for slaves, returning a list of 7-bit addresses

    i2c.writeto(42, b'123')         # write 3 bytes to slave with 7-bit address 42
    i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42

    i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of slave 42,
                                    #   starting at memory-address 8 in the slave
    i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of slave 42
                                    #   starting at address 2 in the slave
 ** KAYNAK: ** https://docs.micropython.org/en/latest/esp8266/library/machine.I2C.html


## tty Portu İçin Aktif Kullanıcıyı Yetkilendirme
		sudo usermod -a -G tty $USER

		After the sudo usermod -a -G tty $USER you have to logout/login to get group addition happens.

    sudo chown $USER:$USER /dev/ttyUSB0


## esptool İle MicroPython Yükleme (flash)
===========================================
		pip3 install --upgrade pip
		pip  install --upgrade pip
		pip install esptool

		Next you can visit micropython website and download the
		latest firmware for the esp8266,
		after downloading it open up a terminal in the same directory
		as the firmware file and then run the below command
		https://micropython.org/download#esp8266

		esptool.py --port /dev/ttyUSB0 erase_flash
		esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20180511-v1.9.4.bin
		You will need to change the port based on you PC.


## REPL Oturumu Açma:
===========================================
		sudo picocom /dev/ttyUSB0 -b115200
		sudo screen /dev/ttyUSB0 115200

		When you're done using screen most versions of it
		allow you to exit by pressing
		Ctrl-a then k then y
		or
		presing Ctrl-a then typing :quit and pressing enter.


## ampy Yükleme ve Kullanımı
===========================================
		KAYNAK: https://github.com/adafruit/ampy
		sudo pip3 install adafruit-ampy
		ampy --help
		sudo ampy --port /dev/ttyUSB0 ls
		export AMPY_PORT=/dev/ttyUSB0
		sudo ampy ls
		sudo ampy --port /dev/ttyUSB0 ls
		sudo ampy --port /dev/ttyUSB0 get boot.py boot.py
		sudo ampy --port /dev/ttyUSB0 run --no-output deneme.py

		By default the run command will wait for the script
		to finish running on the board before printing its output.  
		In some cases you don't want this behavior--
		for example if your script has a main or infinite loop
		that never returns you don't want ampy to sit around
		waiting forever for it to finish.  
		In this case add the --no-output option to the run command.  
		This flag tells ampy not to wait for any output and instead
		just start running the script and return.


## network Bağlantısı Hazırlama
===========================================
		import network
		sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
		sta_if.scan()                             # Scan for available access points
		sta_if.connect("<AP_name>", "<password>") # Connect to an AP
		sta_if.isconnected()                      # Check for successful connection


## Parolanın kaynak kod dışında tutulması için
		f = open("password.txt", 	"r")
		sifre = f.read().strip()
		len(sifre)
		wlan.connect("ağadı", sifre)


## LED YAKMA
		from machine import Pin
		p2  = Pin(2,  Pin.OUT)   # esp8266 üzerindeki MAVİ LED
		p5  = Pin(5,  Pin.OUT)   # GPIO5 ----> D1'e kaşılık geliyor
		p12 = Pin(12, Pin.OUT)   # GPI12 ----> D6'e kaşılık geliyor
		p5.on()
		p5.off()

KAYNAK: https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

		from machine import Pin

		p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
		p0.on()                 # set pin to "on" (high) level
		p0.off()                # set pin to "off" (low) level
		p0.value(1)             # set pin to on/high

		p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
		print(p2.value())       # get value, 0 or 1

		p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
		p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation

		Available pins are: 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16, which
		correspond to the actual GPIO pin numbers of ESP8266 chip.


## Örnek boot.py dosyası
		boot.py
		# This file is executed on every boot (including wake-boot from deepsleep)
		import esp
		esp.osdebug(None)
		import gc

		def do_connect(essid, password):
		    import network
		    sta_if = network.WLAN(network.STA_IF)
		    if not sta_if.isconnected():
		        print('connecting to network...')
		        sta_if.active(True)
		        sta_if.connect(essid, password)
		        while not sta_if.isconnected():
		            pass
		    print('network config:', sta_if.ifconfig())

		do_connect("YARINLAR", "akmanakman")
		#import webrepl
		#webrepl.start()
		gc.collect()

## Networke bağlı mı? IP adresi ne?
		import network
		wlan = network.WLAN(network.STA_IF)
		wlan.isconnected()
		print('network config:', wlan.ifconfig())

## i2c adres taraması
		from machine import Pin, I2C
		i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
		i2c.scan()
		#SONUC: 58 çıktı
		#scl d1
		#sda d2

Kaynak: http://docs.micropython.org/en/v1.9.3/esp8266/library/machine.I2C.html#class-i2c-a-two-wire-serial-protocol

Kaynak: https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#i2c-bus



## 2x16 LCD with I2C BackPack İle LCD Sürülmesi:
		Kaynak: https://github.com/dhylands/python_lcd/tree/master/lcd

		BEYAZ   -- GRNG -- GND
		KIRMIZI -- 3V3  -- VCC
		YESIL   -- D2   -- SDA
		SARI    -- D1   -- SLC

## Dosya oluşturma ve içeriğini okuma
		f = open('dosya.txt', 'w')
		f.write('Merhaba Dunya')
		f.close()

		f = open('dosya.txt', r)
		icerik = f.read().strip()
		f.close()

## GENEL NOTLAR
    MicroPython ESP8266 ADC Documentation

    The ESP8266 has one ADC with 10-bit accuracy and a maximum voltage of 1.0 volt.  
    Be sure not to exceed 1 volt on the ADC input or you could damage the board!


    pcf8591 D/A Converter

# webREPL
		screen ile repl bağlantısı yaptıktan sonra:
		import webrepl_setup
		Yönergeyi izle...

		Şuradan giriş yap:
		http://micropython.org/webrepl/
		IP adresine esp8266'nın IP adresini yaz
		Şifreyi gir. Hoşgeldin!


		Bu adrese doğrudan ERİŞİLEMEZ! Bu bir web socketdir.
		ws://192.168.10.31:8266
