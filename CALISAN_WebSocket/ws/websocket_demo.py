from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient


##########################################################################################################
##########################################################################################################
def OKU():
    import machine
    import ds18x20
    import onewire

    # the device is on GPIO12
    dat = machine.Pin(12)

    # create the onewire object
    ds = ds18x20.DS18X20(onewire.OneWire(dat))

    # scan for devices on the bus
    roms = ds.scan()
    # print('found devices:', roms)

    rom=roms[0]

    return str( int( ds.read_temp(rom) * 1000 ) );

def SICAKLIKOKU():
    cevap = str( int( ds.read_temp(rom) * 1000 ) )
    return cevap


##########################################################################################################
##########################################################################################################

import machine

# prepare pins
pinM = machine.Pin( 2, machine.Pin.OUT, value=1)
pinY = machine.Pin( 4, machine.Pin.OUT, value=1)
pinK = machine.Pin(16, machine.Pin.OUT, value=1)

pinR1 = machine.Pin(15, machine.Pin.OUT, value=1)
pinR2 = machine.Pin(13, machine.Pin.OUT, value=1)

stateY = 0
stateK = 1
stateM = 1

stateR1 = 1
stateR2 = 1


pinY.value(stateY)
pinK.value(stateK)
pinM.value(stateM)

pinR1.value(stateR1)
pinR2.value(stateR2)


##########################################################################################################
##########################################################################################################


class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode("utf-8")
            items = msg.split(" ")
            cmd = items[0]
            if cmd != "":
                self.connection.write(cmd)
                print("Command: " + cmd + "!")

            if cmd == "1111SICAKLIK":
                #SICAKLIK = SICAKLIKOKU()
                SICAKLIK = str( int( ds.read_temp(rom) * 1000 ) )
                self.connection.write( SICAKLIK )
                print("SICAKLIK: " + SICAKLIK)

            if cmd == "r1":
                stateR1 = 0
                pinR1.value(stateR1)
            if cmd == "R1":
                stateR1 = 1
                pinR1.value(stateR1)

            if cmd == "r2":
                stateR2 = 0
                pinR2.value(stateR2)
            if cmd == "R2":
                stateR2 = 1
                pinR2.value(stateR2)

            if cmd == "y":
                stateY = 1
                pinY.value(stateY)
            if cmd == "Y":
                stateY = 0
                pinY.value(stateY)

            if cmd == "m":
                stateM = 0
                pinM.value(stateM)
            if cmd == "M":
                stateM = 1
                pinM.value(stateM)

            if cmd == "k":
                stateK = 0
                pinK.value(stateK)
            if cmd == "K":
                stateK = 1
                pinK.value(stateK)

        except ClientClosedError:
            self.connection.close()


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("test.html", 2)

    def _make_client(self, conn):
        return TestClient(conn)


server = TestServer()
server.start()
try:
    while True:
        server.process_all()
except KeyboardInterrupt:
    server.stop()
    pass
